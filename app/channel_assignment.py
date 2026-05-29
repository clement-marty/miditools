import tkinter as tk


class ChannelAssignmentRow(tk.Frame):

    def __init__(self, master: tk.Tk, coil_id: int, coil_name: str) -> None:
        '''Tkinter widget representing a file

        :param tkinter.Tk master: The widget's parent
        :param int coil_id: The tesla coil's id
        :param str coil_name: The tesla coil's name
        '''
        super().__init__(master, height=30)
        self.coil_id, self.coil_name = coil_id, coil_name
        self.buttons: list[tk.Button] = []
        self.create_widgets()

    def create_widgets(self) -> None:
        '''Creates and places all the window's widgets
        '''
        id_label = tk.Label(self, text=f'[coil_{self.coil_id}]')
        id_label.place(relx=0, rely=0, relwidth=0.1, relheight=1)
        name_label = tk.Label(self, text=self.coil_name)
        name_label.place(relx=0.1, rely=0, relwidth=0.1, relheight=1)

        for i in range(16):
            btn = tk.Button(self, text='', bg='red', activebackground='orange')
            btn.bind('<Button-1>', self.toggle_btn_state)
            btn.place(relx=0.2+(i*0.05), rely=0, relwidth=0.05, relheight=1)
            self.buttons.append(btn)

    def toggle_btn_state(self, event: tk.Event):
        '''Toggles a button on/off and updates the associated ChannelAssignmentWindow object
        
        :param tkinter.Event event: The event that triggered the function's execution
        '''
        btn: tk.Button = event.widget
        value: bool
        if btn['bg'] == 'red':
            btn.config(bg='green')
            value = True
        else:
            btn.config(bg='red')
            value = False
        self.master.update_assignments(self.coil_id, self.buttons.index(btn), value)



class ChannelAssignmentWindow(tk.Toplevel):
    
    def __init__(self, master: tk.Tk, bound_var: dict[str, set[int]]) -> None:
        '''A Tkinter window handling the assignement of MIDI channels on tesla coils

        :param tkinter.Tk master: The window's parent
        :param dict[str, set[int]] bound_var: A mutable variable bound to the class that is updated when the window is closed
        '''
        super().__init__(master)
        self.title('MIDI Channel Assignment')
        self.resizable(width=False, height=False)
        self.assignments: dict[int, set[int]] = {
            0: set(), 1: set(), 2: set()
        }
        self.rows: list[ChannelAssignmentRow] = []
        self.bound_var = bound_var

        self.create_widgets()
        self.wait_visibility()
        self.grab_set()

    def create_widgets(self) -> None:
        '''Creates and places all the window's widgets
        '''

        column_labels_frame = tk.Frame(self, width=600, height=30)
        for i in range(16):
            channel_label = tk.Label(column_labels_frame, text=i, width=4)
            channel_label.place(relx=0.2+(i*0.05), rely=0, relwidth=0.05, relheight=1)
        column_labels_frame.pack(fill=tk.X)

        self.rows = [
            ChannelAssignmentRow(self, 0, 'Posipi'),
            ChannelAssignmentRow(self, 1, 'Negapi'),
            ChannelAssignmentRow(self, 2, 'Genepi')
        ]
        for row in self.rows:
            row.pack(fill=tk.X)

        close_btn = tk.Button(self, text='Close')
        close_btn.bind('<Button-1>', self.close)
        close_btn.pack(side=tk.BOTTOM, fill=tk.X)

    def update_assignments(self, coil: int, channel: int, value: bool) -> None:
        '''Updates the assignments dictionary for a given coil and MIDI channel
        
        :param int coil: The tesla coil's id
        :param int channel: The MIDI channel's id
        :param bool value: The new value to be set
        '''
        if value is True:
            self.assignments[coil].add(channel)
        elif channel in self.assignments[coil]:
            self.assignments[coil].remove(channel)

    def close(self, event: tk.Event) -> None:
        '''Closes the window
        '''
        for k, v in self.assignments.items():
            self.bound_var[k] = v
        self.destroy()
