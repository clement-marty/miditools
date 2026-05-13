import tkinter as tk
from scripts.midi_manager import MidiManager
from tkinter import filedialog as fd


class VerificationWindow(tk.Tk):

    def __init__(self) -> None:
        super().__init__()
        self.geometry("450x300")
        self.title("Verification Window")

    def create_widgets(self) -> None:
        btn_file=tk.Button(self, text="Select file", command=self.select_file)
        btn_file.grid(row=0, column=0, columnspan=2)
        
        tk.Label(self, text="file chosen").grid(row=1, column=1)
        self.name_file=tk.Label(self, text="")
        self.name_file.grid(row=2, column=1)

    def select_file(self, event: tk.Event) -> None:
        filetypes = (('midi files', '*.mid *.midi'))
        filename = fd.askopenfilename(title='Open a file',initialdir='/',filetypes=filetypes)

        self.name_file.config(text=filename)

    def assign_channels(self, event: tk.Event) -> None:
        pass

    def verify(self, event: tk.Event) -> None:
        pass



class Message(tk.Frame):

    def __init__(self, master: tk.Tk, text: str) -> None:
        pass



class SuccessMessage(Message):

    def __init__(self, master: tk.Tk, text: str) -> None:
        pass



class ErrorMessage(Message):

    def __init__(self, master: tk.Tk, text: str) -> None:
        pass



class WarningMessage(Message):

    def __init__(self, master: tk.Tk, text: str) -> None:
        pass
