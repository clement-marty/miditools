import unittest
import mido as md
from pathlib import Path
from .midi_manager import MidiManager 

class Test:

    def __init__(cls, file_paths : list[str], output_path : str):
        """
        Initialising fuction that defines the variables used in the class
        """
        self.coherent_merge = False
       
    def verif(coherent_merge):
        """
        The function that verifies if the merging of the chosen files was made correctly
        """
        mid1 = md.MidiFile('a.mid')
        mid2 = md.MidiFile('125BPM_mel.mid')
        """ using function merge and by calculating the tempo -- knowing what we are supposed to obtain -- verify if the two match"""
