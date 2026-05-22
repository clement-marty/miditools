import tkinter as tk
from .channel_assignment import ChannelAssignmentWindow
from scripts.sysex import SysExConfiguration


class ConfigurationWindow(tk.Tk):

    def __init__(self) -> None:
        super().__init__()
        self.geometry("450x300")
        self.title("Configuration Window")
        self.create_widgets()

    def create_widgets(self) -> None:
        btn_channel=tk.Button(self, text='assign channel')
        btn_channel.bind('<Button-1>', self.assign_channels)
        btn_channel.pack(side=tk.TOP, fill=tk.X)

    def assign_channels(self, event: tk.Event) -> None:
        ChannelAssignmentWindow(self, self.assignments)

    def generate_config(self, event: tk.Event) -> None:
        pass
