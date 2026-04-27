import tkinter as tk
from scripts.midi_manager import MidiManager


class MergeWindow(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('Midi File Merging')
        self.geometry('640x320')
        self.resizable(width=False, height=True)
        self.file_widgets: list[FileListElement] = []
        self.create_widgets()

    def create_widgets(self):
        
        add_file_btn = tk.Button(self, text='Add File')
        add_file_btn.bind('<Button-1>', self.add_file)
        add_file_btn.pack(fill=tk.X)

        self.merge_btn = tk.Button(self, text='Merge')
        self.merge_btn.bind('<Button-1>', self.merge)
        self.merge_btn.pack(side=tk.BOTTOM, fill=tk.X)

        # Creates a tk.Frame object that can be scrolled vetically using the scrollbar
        canvas = tk.Canvas(self)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.configure(yscrollcommand=scrollbar.set)
        self.list_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=self.list_frame, anchor=tk.CENTER, width=620)
        self.list_frame.bind('<Configure>', lambda event: canvas.configure(scrollregion=canvas.bbox(tk.ALL)))


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