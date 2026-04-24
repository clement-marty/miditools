import mido as md
import os
from pathlib import Path

class MidiManager:

    @classmethod
    def merge(cls, file_paths: list[str]) -> None:
        """
        new = md.MidiFile()
        track = md.MidiTrack() 
        for file in file_paths:
            temp = md.MidiFile(file)
            for i, track in enumerate(temp.tracks):
                for msg in track:
                    new.tracks.append(msg)
        new.save("new_file.mid")
        """
        time_past = 0 
        new = md.MidiFile()
        for i in range(len(file_paths), -1, -1): 
            temp = md.MidiFile(file_paths[i-1])
            temp_tempo = temp.tracks[0][0].tempo
            time_past += temp.length
            new.tracks += temp.tracks
            print(temp)
            new.tracks[i+1][0] = md.MetaMessage("set_tempo", temp_tempo, new.ticks_per_beat)
        new.save("midi_tests/new_file.mid")

    @classmethod
    def verify(cls, filepath: str, channel_assignments : dict[int, set[int]]) -> tuple[list[str]]:
        pass
    
f1 = "midi_tests/148BPM_chords.mid"
f2 = "midi_tests/125BPM_mel.mid"
mid1 = md.MidiFile(f1)
mid2 = md.MidiFile(f2)
MidiManager.merge([mid1, mid2])
a = md.MidiFile("midi_tests/new_file.mid")
print(a)
"""
print(mid2)
print("------")
print(a)
print("------")
a.tracks[1][0] = md.MetaMessage("set_tempo", tempo=405405, time=md.second2tick(mid1.length, 96, 405405))
print(a)
a.save("midi_tests/a.mid")
print("---")
"""