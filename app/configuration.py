import tkinter as tk
from .channel_assignment import ChannelAssignmentWindow
from scripts.sysex import SysExConfiguration
from tkinter import scrolledtext


class ConfigurationWindow(tk.Tk):

    def __init__(self) -> None:
        super().__init__()
        self.geometry("450x300")
        self.title("Configuration Window")
        self.create_widgets()
        self.configure(bg="#1e1e2f")
        self.assignments={}

    def create_widgets(self) -> None:
        lbl_duty=tk.Label(self, text='Duty', bg="#1e1e2f", fg="#f5f5f9")
        lbl_duty.grid(row=0, column=1)
        lbl_ontime=tk.Label(self, text='On Time', bg="#1e1e2f", fg="#f5f5f9")
        lbl_ontime.grid(row=0, column=2)

        lbl_t1=tk.Label(self, text='Posipi', bg="#1e1e2f", fg="#f5f5f9")
        lbl_t1.grid(row=1, column=0)
        lbl_t2=tk.Label(self, text='Negapi', bg="#1e1e2f", fg="#f5f5f9")
        lbl_t2.grid(row=2, column=0)
        lbl_t3=tk.Label(self, text='Genepi', bg="#1e1e2f", fg="#f5f5f9")
        lbl_t3.grid(row=3, column=0)

        self.duty_1=tk.Entry(self)
        self.duty_1.grid(row=1, column=1)
        self.duty_2=tk.Entry(self)
        self.duty_2.grid(row=2, column=1)
        self.duty_3=tk.Entry(self)
        self.duty_3.grid(row=3, column=1)

        self.ontime_1=tk.Entry(self)
        self.ontime_1.grid(row=1, column=2)
        self.ontime_2=tk.Entry(self)
        self.ontime_2.grid(row=2, column=2)
        self.ontime_3=tk.Entry(self)
        self.ontime_3.grid(row=3, column=2)

        btn_channel=tk.Button(self, text='Assign channel', bg="#4f46e5", fg="#f5f5f9", font=("TimesNewRoman", 10, "bold"))
        btn_channel.bind('<Button-1>', self.assign_channels)
        btn_channel.grid(row=4, column=1)

        btn_config=tk.Button(self, text='Generate Configuration', bg="#4f46e5",fg="#f5f5f9", font=("TimesNewRoman", 10, "bold"))
        btn_config.bind('<Button-1>', self.generate_config)
        btn_config.grid(row=4, column=2)

        self.text_area = scrolledtext.ScrolledText(self, wrap = tk.WORD, width=54, font = ("Calibri", 12), bg="#1e1e2f", fg="#f5f5f9")
        self.text_area.grid(row=5, column=0, columnspan=3)

    def assign_channels(self, event: tk.Event) -> None:
        ChannelAssignmentWindow(self, self.assignments)

    def generate_config(self, event: tk.Event) -> None:
        pass
