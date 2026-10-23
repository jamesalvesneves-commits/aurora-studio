import sys
from pathlib import Path
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel,
                               QTextEdit, QPushButton, QProgressBar, QMessageBox)
from PySide6.QtCore import Qt, QThread, Signal

from aurora.ollama_client import parse_music_spec
from aurora.music_engine import generate_project
from aurora.ardour_bridge import open_ardour, send_transport

PROJECTS_DIR = Path.home() / "AuroraStudio" / "projects"

class GenerateWorker(QThread):
    finished = Signal(str)
    failed = Signal(str)

    def __init__(self, prompt):
        super().__init__()
        self.prompt = prompt

    def run(self):
        try:
            spec = parse_music_spec(self.prompt)
            project = generate_project(spec, PROJECTS_DIR)
            self.finished.emit(str(project))
        except Exception as error:
            self.failed.emit(str(error))

class AuroraWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aurora Studio")
        self.resize(720, 520)
        self.project_path = None
        self.worker = None

        layout = QVBoxLayout()
        title = QLabel("Aurora Studio — produção musical por IA")
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(title)

        self.prompt = QTextEdit()
        self.prompt.setPlaceholderText("Ex.: crie uma balada em Ré menor com piano, bateria e baixo, 80 BPM")
        layout.addWidget(self.prompt)

        self.generate_button = QPushButton("Gerar música")
        self.generate_button.clicked.connect(self.generate)
        layout.addWidget(self.generate_button)

        self.progress = QProgressBar()
        self.progress.setRange(0, 1)
        self.progress.setValue(0)
        layout.addWidget(self.progress)

        self.status = QLabel("Pronto.")
        layout.addWidget(self.status)

        self.open_button = QPushButton("Abrir no Ardour")
        self.open_button.setEnabled(False)
        self.open_button.clicked.connect(self.open_project)
        layout.addWidget(self.open_button)

        controls = QWidget()
        controls_layout = QVBoxLayout(controls)
        play_button = QPushButton("Play no Ardour")
        play_button.clicked.connect(lambda: send_transport("play"))
        stop_button = QPushButton("Stop no Ardour")
        stop_button.clicked.connect(lambda: send_transport("stop"))
        controls_layout.addWidget(play_button)
        controls_layout.addWidget(stop_button)
        layout.addWidget(controls)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def generate(self):
        prompt = self.prompt.toPlainText().strip()
        if not prompt:
            QMessageBox.warning(self, "Aurora Studio", "Escreva um prompt musical.")
            return
        self.generate_button.setEnabled(False)
        self.progress.setValue(0)
        self.status.setText("Interpretando e gerando...")
        self.worker = GenerateWorker(prompt)
        self.worker.finished.connect(self.on_success)
        self.worker.failed.connect(self.on_failure)
        self.worker.start()

    def on_success(self, path):
        self.project_path = path
        self.progress.setValue(1)
        self.status.setText("Projeto criado em: " + path)
        self.open_button.setEnabled(True)
        self.generate_button.setEnabled(True)

    def on_failure(self, message):
        self.progress.setValue(0)
        self.status.setText("Falha: " + message)
        self.generate_button.setEnabled(True)
        QMessageBox.critical(self, "Aurora Studio", "Falha ao gerar: " + message)

    def open_project(self):
        try:
            open_ardour(Path(self.project_path) if self.project_path else None)
            self.status.setText("Ardour aberto. Edite livremente com o mouse.")
        except Exception as error:
            QMessageBox.critical(self, "Aurora Studio", str(error))

def main():
    app = QApplication(sys.argv)
    window = AuroraWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
