import json
import re
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2"

def ask_ollama(prompt: str) -> str:
    response = requests.post(OLLAMA_URL, json={
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
    }, timeout=120)
    response.raise_for_status()
    return response.json().get("response", "")

def parse_music_spec(prompt: str) -> dict:
    instruction = (
        "Voce e um produtor musical. Converta o pedido em JSON com as chaves: "
        "style, key, bpm, bars, instruments (lista), mood. "
        "Responda APENAS com JSON valido. Pedido: " + prompt
    )
    try:
        text = ask_ollama(instruction)
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            return json.loads(match.group(0))
    except Exception:
        pass
    return {
        "style": "ballad",
        "key": "D minor",
        "bpm": 80,
        "bars": 16,
        "instruments": ["piano", "bass", "drums"],
        "mood": "emotional",
    }
