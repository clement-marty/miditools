import tkinter as tk
from .merge import MergeWindow
from .verification import VerificationWindow
from .configuration import ConfigurationWindow


class StartWindow(tk.Tk):

    def __init__(self) -> None:
        pass

    def create_widgets(self) -> None:
        pass

    def open_merge_window(self, event: tk.Event) -> None:
        pass

    def open_verification_window(self, event: tk.Event) -> None:
        pass

    def open_configuration_window(self, event: tk.Event) -> None:
        pass
