import mido as md
import os
from pathlib import Path

class MidiManager:

    @classmethod
    def merge(cls, file_paths : list[str], output_path : str) -> None:
        """
        Creates a new .mid file by merging a len(file_paths) amount of midi files, by adding them one after the other while respecting the bpm changes between each other.  
        ---
        Parameter:
            file_paths: list of strings, with the file path of each midi files
        Output:
            output_path: string of the file path for the output midi file
        """


        #time_past and last_tempo are the time and tempo of the mid file just before the one used in the for loop 
        time_past = 0 
        last_tempo = md.MidiFile(file_paths[0]).ticks_per_beat
        
        #set the new file with the ticks per beat of the first input       
        new = md.MidiFile(ticks_per_beat=last_tempo)
        
        
        for i in range(len(file_paths)): 
            
            temp = md.MidiFile(file_paths[i])
            temp_tempo = temp.ticks_per_beat
            #Get the ratio between the current and the tempo just before to allow bpm changes
            tempo_ratio = last_tempo/temp_tempo
            #set the tempo just before to the current one (used in the next loop iteration)
            last_tempo = temp_tempo
            time_sig = (temp.tracks[0][1].numerator, temp.tracks[0][1].denominator)

            
            for track in temp.tracks:
                bar_len = time_sig[0]*temp_tempo*(4/time_sig[1])
                temp_track = md.MidiTrack()
                temp_time = 0
                #get the length of the current midi file
                track_ticks = sum(msg.time for msg in track)   
                time2add = time_sig[1]*temp_tempo-track_ticks%(time_sig[1]*temp_tempo)              
                first = True
                for i in range(len(track)-1):
                    #change the length of each note to appropriate one depending on the bpm 
                    temp_time = int(round(track[i].time*tempo_ratio))
                    temp_msg = track[i].copy(time=temp_time)
                    
                    #if the message is the first, the time it starts is right after the last midi file
                    if first:
                        temp_msg.time += time_past
                        first = False
                        
                    temp_track.append(temp_msg)
                    
                #if last note does not end at the end of a bar, we lengthen it
                
                
                #if track_ticks > 0 & time2add<time_sig[1]*temp_tempo:
                #    print(track[i].time)
                #    print("v")
                #    print(time2add)
                #    temp_time = int(round((track[i].time+time2add)*tempo_ratio))
                #    temp_msg = track[i].copy(time=temp_time)
                #    temp_track.append(temp_msg)
                    
                
                new.tracks.append(temp_track)
                
            #add the used file length to the total time since the start of the output file           
            time_past += track_ticks
            time_past = int(((time_past+bar_len-1)//bar_len)*bar_len) # adds empty space between 2 files if the first one does not end at a bar. 
        print(new)
        
        new.save(output_path)
                

    @classmethod
    def verify(cls, filepath: str, channel_assignments : dict[int, set[int]]) -> tuple[list[str]]:
        """
        Verifies a few constraints to allow the Tesla coils to work properly. There should be at most 4 notes at the same time for a given coil
        ---
        Parameters:
            filepath : str contaning the relative path for the midi file to verify.
            channel_assigments : dictionnary with int key and set of int value.
        Output:
        """
        mid = md.Midifile(filepath)


   

  
# #time added = k*numerator/bpm


# #trouver dernière time signature du fichier et ajouter a time_past le temps du fichier actuel modulo temps d'une mesure (denominator*beatpertick) - temps du fichier
# print(4*96)
