import tkinter as tk
from scripts.midi_manager import MidiManager
from tkinter import filedialog as fd


class VerificationWindow(tk.Tk):

    def __init__(self) -> None:
        super().__init__()
        self.geometry("450x300")
        self.title("Verification Window")
        self.create_widgets()

    def create_widgets(self) -> None:
        btn_file=tk.Button(self, text="Select file", command=self.select_file)
        btn_file.pack()
        
        tk.Label(self, text="file chosen").pack()
        self.name_file=tk.Label(self, text="")
        self.name_file.pack()

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
        filetypes = (('midi files', '*.mid *.midi'))
        filename = fd.askopenfilename(title='Open a file',initialdir='/',filetypes=filetypes)

        self.name_file.config(text=filename)

    def assign_channels(self, event: tk.Event) -> None:
        pass

    def verify(self, event: tk.Event) -> None:
        pass



class Message(tk.Frame):

    def __init__(self, master: tk.Tk, text: str) -> None:
        super().__init__()
        self.verif_wnd=master
        self.text=text
        self.bg_color = None
        self.label=tk.Label(text=self.text)
        self.label.pack(fill='both')



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
