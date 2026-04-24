import mido as md


class MidiManager:

    @classmethod
    def merge(cls, file_paths: list[str], output_path: str) -> None:
        pass

    @classmethod
    def verify(cls, filepath: str) -> tuple[list[str]]:
        pass
    
    
f1 = "../midi tests/148BPM chords.midi"
f2 = "../midi tests/148BPM mel.midi"
mid1 = md.MidiFile(f1)
mid2 = md.MidiFile(f2)
print(mid1,mid2)
