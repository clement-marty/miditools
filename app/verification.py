import tkinter as tk
from scripts.midi_manager import MidiManager
from tkinter import filedialog as fd
from .channel_assignment import ChannelAssignmentWindow

class VerificationWindow(tk.Tk):

    def __init__(self) -> None:
        super().__init__()
        self.geometry("450x300")
        self.title("Verification Window")
        self.configure(bg="#1e1e2f")
        self.create_widgets()
        self.assignments={}

    def create_widgets(self) -> None:
        btn_file=tk.Button(self, text="Select file")
        btn_file.bind('<Button-1>',self.select_file)
        btn_file.pack(side=tk.TOP, fill=tk.X)
        
        tk.Label(self, text="file chosen:",fg="#f5f5f9", bg="#1e1e2f").pack(side=tk.TOP)
        self.name_file=tk.Label(self, text="", fg="#fafafa", bg="#1e1e2f")
        self.name_file.pack(side=tk.TOP)

        btn_channel=tk.Button(self, text='assign channel')
        btn_channel.bind('<Button-1>', self.assign_channels)
        btn_channel.pack(side=tk.TOP, fill=tk.X)
        
        btn_ver=tk.Button(self, text='verify')
        btn_ver.bind('<Button-1>', self.verify)
        btn_ver.pack(side=tk.TOP, fill=tk.X)

        # Creates a tk.Frame object that can be scrolled vetically using the scrollbar
        canvas = tk.Canvas(self)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.configure(yscrollcommand=scrollbar.set)
        self.list_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=self.list_frame, anchor=tk.N, width=620)
        self.list_frame.bind('<Configure>', lambda event: canvas.configure(scrollregion=canvas.bbox(tk.ALL)))

    def select_file(self, event: tk.Event) -> None:
        print(self.assignments)
        filename=fd.askopenfilenames(filetypes=[('Midi Files', '*.mid *.midi')])

        self.name_file.config(text=filename)

    def assign_channels(self, event: tk.Event) -> None:
        ChannelAssignmentWindow(self, self.assignments)

    def verify(self, event: tk.Event) -> None:
        file=self.name_file.cget("text")
        if file!='':
            res=MidiManager.verify(file, channel_assignments=self.assignments)
            for e in res[0]:
                mess=SuccessMessage(master=self.list_frame, text=e)
                mess.pack(side=tk.TOP)
            for e in res[1]:
                mess=ErrorMessage(master=self.list_frame, text=e)
                mess.pack(side=tk.TOP)
            for e in res[2]:
                mess=WarningMessage(master=self.list_frame, text=e)
                mess.pack(side=tk.TOP)


class Message(tk.Frame):

    def __init__(self, master: tk.Tk, text: str) -> None:
        super().__init__()
        self.verif_wnd=master
        self.text=text
        self.bg_color = None
        self.label=tk.Label(text=self.text)
        self.label.pack(fill=tk.BOTH)



class SuccessMessage(Message):

    def __init__(self, master: tk.Tk, text: str) -> None:
        super().__init__(master, text)
        self.label.config(bg='green')



class ErrorMessage(Message):

    def __init__(self, master: tk.Tk, text: str) -> None:
        super().__init__(master,text)
        self.label.config(bg='red')



class WarningMessage(Message):

    def __init__(self, master: tk.Tk, text: str) -> None:
        super().__init__(master,text)
        self.label.config(bg='orange')
