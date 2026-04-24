import tkinter as tk
from scripts.midi_manager import MidiManager


class MergeWindow(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("test")
        self.geometry('400x200')

    def create_widgets(self):
        pass

    def add_file(self, event: tk.Event) -> None:
        pass

    def remove_file(self, event: tk.Event) -> None:
        pass

    def move_up(self, event: tk.Event) -> None:
        pass

    def move_down(self, event: tk.Event) -> None:
        pass

    def merge(self, event: tk.Event) -> None:
        pass



class FileListElement(tk.Frame):

    def __init__(self, master: tk.Tk, file_path: str) -> None:
        pass


# app = MergeWindow()
# app.mainloop()