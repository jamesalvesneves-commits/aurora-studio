#include <QApplication>
#include <QMainWindow>
#include <QWidget>
#include <QVBoxLayout>
#include <QHBoxLayout>
#include <QLabel>
#include <QPushButton>
#include <QPlainTextEdit>
#include <QStatusBar>
#include <QTimer>

int main(int argc, char *argv[]) {
    QApplication app(argc, argv);
    app.setApplicationName("AURORA Studio");
    QMainWindow window;
    window.setWindowTitle("AURORA Studio — Fundação 0.1.0");
    window.resize(1200, 800);
    auto *central = new QWidget(&window);
    auto *layout = new QVBoxLayout(central);
    layout->addWidget(new QLabel("AURORA Studio | Nenhum projeto aberto", central));
    auto *modules = new QHBoxLayout;
    for (const auto &name : {"Ardour", "ACE-Step", "Demucs", "Ollama", "Biblioteca"}) {
        auto *button = new QPushButton(QString::fromUtf8(name), central);
        button->setEnabled(false);
        button->setToolTip("Integração ainda não implementada nesta versão de desenvolvimento.");
        modules->addWidget(button);
    }
    layout->addLayout(modules);
    layout->addWidget(new QLabel("Área do projeto — nenhuma faixa carregada", central), 1);
    auto *prompt = new QPlainTextEdit(central);
    prompt->setPlaceholderText("Comandos em linguagem natural serão habilitados após integração e testes do Ollama.");
    prompt->setReadOnly(true);
    layout->addWidget(prompt);
    layout->addWidget(new QLabel("Tarefas: nenhuma | Componentes: não verificados", central));
    window.setCentralWidget(central);
    window.statusBar()->showMessage("Versão de desenvolvimento: interface inicial, sem motores musicais integrados.");
    window.show();
    if (app.arguments().contains("--smoke-test")) {
        QTimer::singleShot(250, &app, [&window, &app]() {
            app.exit(window.isVisible() && window.centralWidget() ? 0 : 1);
        });
    }
    return app.exec();
}
