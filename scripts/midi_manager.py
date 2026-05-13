import mido as md
import os
from pathlib import Path

class MidiManager:

    @classmethod
    def merge(cls, file_paths : list[str], output_path : str) -> None:
        """
        Creates a new .mid file by merging a len(file_paths) amount of midi files, by adding them one after the other while respecting the bpm changes between each other. 
        Time signatures must be 4/4 for every file. 
        ---
        Parameter:
        file_paths: list of strings, with the file path of each midi files
        output_path: string of the file path for the output midi file
        """


        #time_past and last_tempo are the time and tempo of the mid file just before the one used in the for loop 
        time_past = 0 
        last_tempo = md.MidiFile(file_paths[0]).ticks_per_beat
        
        #set the new file with a tbp of the first input       
        new = md.MidiFile(ticks_per_beat=last_tempo)
        
        
        for i in range(len(file_paths)): 
            
            temp = md.MidiFile(file_paths[i])
            temp_tempo = temp.ticks_per_beat
            
            #Get the ratio between the current and the tempo just before to allow bpm changes
            tempo_ratio = last_tempo/temp_tempo
            #set the tempo just before to the current one (used in the next loop iteration)
            last_tempo = temp_tempo
            
            
            for track in temp.tracks:
                temp_track = md.MidiTrack()
                
                #get the length of the current midi file
                track_ticks = sum(msg.time for msg in track)   
                first = True
                for msg in track:
                    #change the length of each note to appropriate one depending on the bpm 
                    temp_time = int(round(msg.time*tempo_ratio))
                    temp_msg = msg.copy(time=temp_time)
                    
                    #if the message is the first, the time it starts is right after the last midi file
                    if first:
                        temp_msg.time += time_past
                        first = False
                        
                    temp_track.append(temp_msg)
                    
                new.tracks.append(temp_track)
                
            #add the used file length to the total time since the start of the output file           
            time_past += track_ticks

        new.save(output_path)
                

    @classmethod
    def verify(cls, filepath: str, channel_assignments : dict[int, set[int]]) -> tuple[list[str]]:
        pass
    
    
