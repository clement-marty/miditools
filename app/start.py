import tkinter as tk
from .merge import MergeWindow
from .verification import VerificationWindow
from .configuration import ConfigurationWindow

class StartWindow(tk.Tk):

    def __init__(self):
        '''Initialising the Start window and calling function create_widgets() to create widgets
        '''
        super().__init__()
        self.title("MIDI Tools")
        self.geometry("600x450")
        self.configure(bg="#1e1e2f")
        self.create_widgets()

    def create_widgets(self):
        '''Creating buttons and labels to comunicate with the user
        '''
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
        '''Function that creates a 'parent' button and then binds it with the event indicated
        '''
        btn = tk.Button(
            parent,
            text=text,
            font=("TimesNewRoman", 14, "bold"),
            width=20,
            height=2,
            bg="#4f46e5",
            fg="white",
        )
        btn.bind("<Button-1>", command)
        return btn

    def open_merge_window(self, event: tk.Event):
        '''Function that destroys the Start window and opens Merge window when clicking on the attributed button

        :param tkinter.Event event: The event that triggered the function's execution
        '''
        self.destroy()
        merge_window = MergeWindow()
        merge_window.protocol("WM_DELETE_WINDOW", lambda: self.subwindow_closed(merge_window))
        merge_window.mainloop()

    def open_verification_window(self, event: tk.Event):
        '''Function that destroys the Start window and opens Verification window when clicking the attributed button

        :param tkinter.Event event: The event that triggered the function's execution
        '''
        self.destroy()
        verification_window = VerificationWindow()
        verification_window.protocol("WM_DELETE_WINDOW", lambda: self.subwindow_closed(verification_window))
        verification_window.mainloop()

    def open_configuration_window(self, event: tk.Event):
        '''Function that destroys the Start window and opens Configuration window when clicking the attributed button

        :param tkinter.Event event: The event that triggered the function's execution
        '''
        self.destroy()
        configuration_window = ConfigurationWindow()
        configuration_window.protocol("WM_DELETE_WINDOW", lambda: self.subwindow_closed(configuration_window))
        configuration_window.mainloop()

    def open_configuration_window(self, event: tk.Event):
        '''Function that destroys the Start window and opens Configuration window when clicking the attributed button

        :param tkinter.Event event: The event that triggered the function's execution
        '''
        self.destroy()
        configuration_window = ConfigurationWindow()
        configuration_window.protocol("WM_DELETE_WINDOW", lambda: self.subwindow_closed(configuration_window))
        configuration_window.mainloop()

    def subwindow_closed(self, window: tk.Tk):
        '''Opens the Start window when the subwindow is closed

        :param tkinter.Tk window: The subwindow that was closed
        '''
        window.destroy()
        StartWindow().mainloop()
        
