import mido as md
import os
from pathlib import Path

class MidiManager:

    @classmethod
    def merge(cls, file_paths: list[str], output_path: str) -> None:
        new = md.MidiFile()
        track = md.MidiTrack() 
        for file in file_paths:
            temp = md.MidiFile(file)
            for i, track in enumerate(temp.tracks):
                for msg in track:
                    new.tracks.append(msg)

    @classmethod
    def verify(cls, filepath: str) -> tuple[list[str]]:
        pass
    
f1 = "midi_tests/148BPM_chords.mid"
f2 = "midi_tests/148BPM_mel.mid"
mid1 = md.MidiFile(f1)
mid2 = md.MidiFile(f2)
print(mid1,mid2)
