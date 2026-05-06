import tkinter as tk
import tkinter.filedialog as fd
from scripts.midi_manager import MidiManager


class FileListElement(tk.Frame):

    def __init__(self, master: tk.Tk, file_path: str) -> None:
        super().__init__(master)
        self.file_path = file_path
        self.filename = file_path.split('/')[-1]
        btn_width = 6
        self.config(
            highlightbackground='grey',
            highlightthickness=1
        )

        filename_label = tk.Label(self, text=self.filename)
        filename_label.pack(side=tk.LEFT, fill=tk.X, padx=20)

        self.move_up_btn = tk.Button(self, text='Up', width=btn_width)
        self.move_down_btn = tk.Button(self, text='Down', width=btn_width)
        self.remove_btn = tk.Button(self, text='Remove', width=btn_width)

        self.remove_btn.pack(side=tk.RIGHT)
        self.move_down_btn.pack(side=tk.RIGHT)
        self.move_up_btn.pack(side=tk.RIGHT)



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
        canvas.create_window((0, 0), window=self.list_frame, anchor=tk.N, width=620)
        self.list_frame.bind('<Configure>', lambda event: canvas.configure(scrollregion=canvas.bbox(tk.ALL)))

    def add_file(self, event: tk.Event) -> None:
        filenames = fd.askopenfilenames(filetypes=[('Midi Files', '*.mid *.midi')])

        if len(filenames) != 0:

            # Reactivate the last FileListElement's move down button
            if len(self.file_widgets) != 0:
                self.file_widgets[-1].move_down_btn.config(state='normal')

            # Add all new widgets
            for filename in filenames:
                widget = FileListElement(self.list_frame, filename)
                self.file_widgets.append(widget)

                # Bind the widget's buttons to the MergeWindow methods
                widget.move_up_btn.bind('<Button-1>', self.move_up)
                widget.move_down_btn.bind('<Button-1>', self.move_down)
                widget.remove_btn.bind('<Button-1>', self.remove_file)
                
                widget.pack(fill=tk.X)

            # Deactivate the last FileListElement's move down button
            self.file_widgets[-1].move_down_btn.config(state='disabled')
            # Deactivate the first element's move up button
            self.file_widgets[0].move_up_btn.config(state='disabled')

    def remove_file(self, event: tk.Event) -> None:
        obj: FileListElement = event.widget.master # Get the FileListElement object that triggered the event
        self.file_widgets.remove(obj)
        obj.destroy()

    def move_up(self, event: tk.Event) -> None:
        obj: FileListElement = event.widget.master # Get the FileListElement object that triggered the event
        i = self.file_widgets.index(obj)
        if i > 0 and len(self.file_widgets) >= 2:
            self.swap_files(i-1, i)

    def move_down(self, event: tk.Event) -> None:
        obj: FileListElement = event.widget.master # Get the FileListElement object that triggered the event
        i = self.file_widgets.index(obj)
        if i < len(self.file_widgets)-1 and len(self.file_widgets) >= 2:
            self.swap_files(i, i+1)

    def swap_files(self, index1: int, index2: int) -> None:
        # Invert the two elements in the list
        self.file_widgets[index1], self.file_widgets[index2] = self.file_widgets[index2], self.file_widgets[index1]

        # Repack all instances of FileListElement
        for obj in self.file_widgets:
            obj.pack_forget()
            obj.move_up_btn.config(state='normal')
            obj.move_down_btn.config(state='normal')
        for i, obj in enumerate(self.file_widgets):
            obj.pack(fill=tk.X)
            # Disable the move up button if the object is at the start of the list
            if i == 0: obj.move_up_btn.config(state='disabled')
            # Disable the move down button if the object is at the end of the list
            elif i == len(self.file_widgets)-1: obj.move_down_btn.config(state='disabled')

    def merge(self, event: tk.Event) -> None:
        pass
