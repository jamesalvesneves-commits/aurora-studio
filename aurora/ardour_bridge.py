import os
import subprocess
from pathlib import Path
from pythonosc.udp_client import SimpleUDPClient

ARDOUR_OSC_HOST = "127.0.0.1"
ARDOUR_OSC_PORT = 3819

def find_ardour() -> str | None:
    candidates = [
        Path(os.environ.get("ProgramFiles", "C:/Program Files")) / "Ardour" / "bin" / "ardour.exe",
        Path(os.environ.get("LOCALAPPDATA", "")) / "Programs" / "Ardour" / "bin" / "ardour.exe",
    ]
    for path in candidates:
        if path.exists():
            return str(path)
    return None

def open_ardour(project_dir: Path | None = None) -> str:
    ardour = find_ardour()
    if not ardour:
        raise FileNotFoundError("Ardour nao encontrado. Instale em https://ardour.org/download.html")
    args = [ardour]
    if project_dir:
        args.append(str(project_dir))
    subprocess.Popen(args)
    return ardour

def send_transport(command: str):
    client = SimpleUDPClient(ARDOUR_OSC_HOST, ARDOUR_OSC_PORT)
    if command == "play":
        client.send_message("/ardour/transport_play", [])
    elif command == "stop":
        client.send_message("/ardour/transport_stop", [])
