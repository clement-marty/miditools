import tkinter as tk
from scripts.midi_manager import MidiManager
from tkinter import filedialog as fd


class VerificationWindow(tk.Tk):

    def __init__(self) -> None:
        pass

    def create_widgets(self) -> None:
        pass

    def select_file(self, event: tk.Event) -> None:
        pass

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
