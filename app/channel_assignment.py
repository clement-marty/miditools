import tkinter as tk


class ChannelAssignmentRow(tk.Frame):

    def __init__(self, master: tk.Tk, coil_id: int, coil_name: str) -> None:
        '''Tkinter widget representing a file

        :param tkinter.Tk master: The widget's parent
        :param int coil_id: The tesla coil's id
        :param str coil_name: The tesla coil's name
        '''
        pass

    def create_widgets(self) -> None:
        '''Creates and places all the window's widgets
        '''
        pass

    def toggle_btn_state(self, event: tk.Event):
        '''Toggles a button on/off and updates the associated ChannelAssignmentWindow object
        
        :param tkinter.Event event: The event that triggered the function's execution
        '''
        pass



class ChannelAssignmentWindow(tk.Toplevel):
    
    def __init__(self, master: tk.Tk) -> None:
        '''A Tkinter window handling the assignement of MIDI channels on tesla coils

        :param tkinter.Tk master: The window's parent
        '''
        pass

    def create_widgets(self) -> None:
        '''Creates and places all the window's widgets
        '''
        pass

    def update_assignments(self, coil: int, channel: int, value: bool) -> None:
        '''Updates the assignments dictionary for a given coil and MIDI channel
        
        :param int coil: The tesla coil's id
        :param int channel: The MIDI channel's id
        :param bool value: The new value to be set
        '''
        pass

    def close(self, event: tk.Event) -> None:
        '''Closes the window
        '''
        pass
