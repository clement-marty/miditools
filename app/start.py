import tkinter as tk
from .merge import MergeWindow
from .verification import VerificationWindow
from .configuration import ConfigurationWindow


class StartWindow(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("MIDI Tools")
        self.geometry("600x450")
        self.configure(bg="#1e1e2f")
        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(self, text="MIDI Tools", font=("Helvetica", 24, "bold"), fg="white", bg="#1e1e2d")
        title.pack(pady=(20, 10))

        subtitle = tk.Label(self, text="Utilities for MIDI files", font=("TimesNewRoman", 12), fg="#b8b8d1", bg="#1e1e2d")
        subtitle.pack(pady=(0, 30))

        button_frame = tk.Frame(self, bg="#1e1e2d")
        button_frame.pack(pady=10)

        self.create_menu_button(button_frame, text="Configuration", command=self.open_configuration_window).pack(pady=10)
        self.create_menu_button(button_frame, text="Verification", command=self.open_verification_window).pack(pady=10)
        self.create_menu_button(button_frame, text="Merge Files", command=self.open_merge_window).pack(pady=10)
        
        footer = tk.Label(self,text="INSA Clubelek Project",font=("TimesNewRoman", 10, "italic"),fg="#7a7a99",bg="#1e1e2d")
        footer.pack(side="bottom", pady=20)

    def create_menu_button(self, parent, text, command):
        btn = tk.Button(
            parent,
            text=text,
            font=("TimesNewRoman", 14, "bold"),
            width=20,
            height=2,
            bg="#4f46e5",
            fg="white",

        )

        return btn
            
        
