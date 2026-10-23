import os
from datetime import datetime
from pathlib import Path
from mido import MidiFile, MidiTrack, Message, MetaMessage, bpm2tempo

NOTE_MAP = {"C": 0, "C#": 1, "Db": 1, "D": 2, "D#": 3, "Eb": 3, "E": 4, "F": 5,
            "F#": 6, "Gb": 6, "G": 7, "G#": 8, "Ab": 8, "A": 9, "A#": 10, "Bb": 10, "B": 11}

SCALE_MINOR = [0, 2, 3, 5, 7, 8, 10]
SCALE_MAJOR = [0, 2, 4, 5, 7, 9, 11]

def _parse_key(key: str):
    parts = key.strip().split()
    root = NOTE_MAP.get(parts[0].capitalize() if len(parts[0]) <= 2 else parts[0], 2)
    mode = SCALE_MINOR if "minor" in key.lower() else SCALE_MAJOR
    return root, mode

def _add_track(mid: MidiFile, channel: int, program: int, notes, velocity=90):
    track = MidiTrack()
    mid.tracks.append(track)
    track.append(Message("program_change", channel=channel, program=program, time=0))
    for note, start, duration in notes:
        track.append(Message("note_on", channel=channel, note=note, velocity=velocity, time=start))
        track.append(Message("note_off", channel=channel, note=note, velocity=0, time=duration))

def generate_project(spec: dict, base_dir: Path) -> Path:
    bpm = int(spec.get("bpm", 80))
    bars = int(spec.get("bars", 16))
    key = spec.get("key", "D minor")
    root, scale = _parse_key(key)
    mid = MidiFile()
    mid.tracks.append(MidiTrack())
    mid.tracks[0].append(MetaMessage("set_tempo", tempo=bpm2tempo(bpm), time=0))
    mid.tracks[0].append(MetaMessage("time_signature", numerator=4, denominator=4, time=0))

    beat = 480
    bar = beat * 4
    chords = []
    for i in range(bars):
        degree = [0, 5, 3, 4][i % 4]
        chord_root = root + scale[degree]
        chords.append(chord_root)

    bass_notes = []
    chord_notes = []
    for i, chord_root in enumerate(chords):
        start = i * bar
        bass_notes.append((chord_root - 24, start, bar))
        for interval in (0, 3 if "minor" in key.lower() else 4, 7):
            chord_notes.append((chord_root + interval, start, bar))

    melody_notes = []
    for i in range(bars * 2):
        degree = scale[(i * 2) % len(scale)]
        note = root + 12 + degree
        melody_notes.append((note, i * beat, beat))

    _add_track(mid, 0, 0, chord_notes)          # piano
    _add_track(mid, 1, 33, bass_notes)          # bass
    _add_track(mid, 2, 73, melody_notes, 100)   # flute/melody

    drums = MidiTrack()
    mid.tracks.append(drums)
    drums.append(Message("program_change", channel=9, program=0, time=0))
    for i in range(bars * 4):
        time = i * beat
        if i % 4 == 0:
            drums.append(Message("note_on", channel=9, note=36, velocity=110, time=time if i == 0 else 0))
            drums.append(Message("note_off", channel=9, note=36, velocity=0, time=beat))
        elif i % 4 == 2:
            drums.append(Message("note_on", channel=9, note=38, velocity=100, time=0))
            drums.append(Message("note_off", channel=9, note=38, velocity=0, time=beat))
        else:
            drums.append(Message("note_on", channel=9, note=42, velocity=70, time=0))
            drums.append(Message("note_off", channel=9, note=42, velocity=0, time=beat))

    project_dir = base_dir / ("project_" + datetime.now().strftime("%Y%m%d_%H%M%S"))
    project_dir.mkdir(parents=True, exist_ok=True)
    mid.save(project_dir / "aurora_song.mid")
    (project_dir / "spec.json").write_text(str(spec), encoding="utf-8")
    return project_dir
