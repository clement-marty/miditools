import tkinter as tk
from .channel_assignment import ChannelAssignmentWindow
from scripts.sysex import SysExConfiguration
from tkinter import scrolledtext
import tkinter.messagebox as mb


class ConfigurationWindow(tk.Tk):

    def __init__(self) -> None:
        '''A Tkinter window handling the graphical interface part of verifying the validity of a MIDI file
        '''
        super().__init__()
        self.geometry("450x300")
        self.title("Configuration Window")
        self.create_widgets()
        self.configure(bg="#1e1e2f")
        self.assignments={}

    def create_widgets(self) -> None:
        '''Creates and places all the window's widgets
        '''
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

        vcmd=self.register(self.verify_entry)
        self.duty_0=tk.Entry(self, validate='all', validatecommand=(vcmd,'%P'))
        self.duty_0.grid(row=1, column=1)
        self.duty_0.insert(tk.END,'0.05')
        self.duty_1=tk.Entry(self, validate='all', validatecommand=(vcmd,'%P'))
        self.duty_1.grid(row=2, column=1)
        self.duty_1.insert(tk.END,'0.05')
        self.duty_2=tk.Entry(self, validate='all', validatecommand=(vcmd,'%P'))
        self.duty_2.grid(row=3, column=1)
        self.duty_2.insert(tk.END,'0.08')

        self.ontime_0=tk.Entry(self, validate='all', validatecommand=(vcmd,'%P'))
        self.ontime_0.grid(row=1, column=2)
        self.ontime_0.insert(tk.END,'40')
        self.ontime_1=tk.Entry(self, validate='all', validatecommand=(vcmd,'%P'))
        self.ontime_1.grid(row=2, column=2)
        self.ontime_1.insert(tk.END,'40')
        self.ontime_2=tk.Entry(self, validate='all', validatecommand=(vcmd,'%P'))
        self.ontime_2.grid(row=3, column=2)
        self.ontime_2.insert(tk.END,'30')

        btn_channel=tk.Button(self, text='Assign channel', bg="#4f46e5", fg="#f5f5f9", font=("TimesNewRoman", 10, "bold"))
        btn_channel.bind('<Button-1>', self.assign_channels)
        btn_channel.grid(row=4, column=1)

        btn_config=tk.Button(self, text='Generate Configuration', bg="#4f46e5",fg="#f5f5f9", font=("TimesNewRoman", 10, "bold"))
        btn_config.bind('<Button-1>', self.generate_config)
        btn_config.grid(row=4, column=2)

        self.text_area = scrolledtext.ScrolledText(self, wrap = tk.WORD, width=54, font = ("Calibri", 12), bg="#1e1e2f", fg="#f5f5f9")
        self.text_area.grid(row=5, column=0, columnspan=3)

    def assign_channels(self, event: tk.Event) -> None:
        '''Opens a ChannelAssignmentWindow instance
        
        :param tkinter.Event event: The event that triggered the function's execution
        '''
        ChannelAssignmentWindow(self, self.assignments)

    def generate_config(self, event: tk.Event) -> None:
        '''Generate the configuration associated to the parameters chosen 
        
        :param tkinter.Event event: The event that triggered the function's execution
        '''
        if self.duty_0.get()=='' or self.duty_1.get()=='' or self.duty_2.get()=='' or self.ontime_0.get()=='' or self.ontime_1.get()=='' or self.ontime_2.get()=='':
            mb.showerror('Error', 'Please make sure that all parameters are set.')
        else: 
            para={0:{}, 1:{}, 2:{}}
            para[0]={'duty':self.duty_0.get(), 'ontime':self.ontime_0.get()}
            para[1]={'duty':self.duty_1.get(), 'ontime':self.ontime_1.get()}
            para[2]={'duty':self.duty_2.get(), 'ontime':self.ontime_2.get()}
            sysex=SysExConfiguration(self.assignments, para)
            commands=sysex.get_syfoh_commands()
            self.text_area.delete(1.0, tk.END) 
            self.text_area.insert(tk.INSERT,'\n'.join(commands))

    def verify_entry (self, value:str):
        '''Verify that the value chosen by the user is a number 
        
        :param float value : The value that the user want to enter
        '''
        try:
            if value!= '':
                float(value)
            return True 
        except: 
            return False

