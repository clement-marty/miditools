import tkinter as tk
from .merge import MergeWindow
from .verification import VerificationWindow
from .configuration import ConfigurationWindow


class StartWindow(tk.Tk):

    def __init__(self) -> None:
        super().__init__()
        self.title("MIDI TOOLS")
        self.geometry("400x200")
        self.create_widgets()

    def create_widgets(self):
        lbl_1 = tk.Label(self, text = "Configuration")
        lbl_1.grid(row =1, column = 1)
        lbl_1.button.bind("<Button-1>", self.open_configuration_window)

        lbl_2 = tk.Label(self, text = "Verification")
        lbl_2.grid(row =2, column = 1)
        lbl_2.button.bind("<Button-1>", self.open_verification_window)

        lbl_3 = tk.Label(self, text = "Merge")
        lbl_3.grid(row =3, column = 1)
        lbl_3.button.bind("<Button-1>", self.open_merge_window)

    def open_merge_window(self, event: tk.Event):
        merge_window = tk.Toplevel()  # creates a second window
        merge_window.title("Merge Window")

    def open_verification_window(self, event: tk.Event):
        verification_window = tk.Toplevel()  # creates a second window
        verification_window.title("Verification Window")

    def open_configuration_window(self, event: tk.Event) -> None:
        configuration_window = tk.Toplevel()  # creates a second window
        configuration_window.title("Configuration Window")
        

