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
        Verifies a few constraints to allow the Telsa coils to work properly:
        -There should be at most 4 notes at the same time for a given coil (channel),
        -There should not be a note played in a channel not in parameter channel_assignments,
        -The enveloppes used should be the ones used by the Clubelek, from id 0 to 9.
        ---
        Parameters:
            filepath : str contaning the relative path for the midi file to verify.
            channel_assigments : dictionnary with integer key which is the index t_ind of the Tesla and values that are sets of integer corresponding to the channels it is assigned to.
        Output:
            results : tuple of 3 lists of strings, corresponding to errors messages, warning messages and success messages.
        """
        errors = []
        warnings = []
        successes = []
        
        #we change the data structure to link a channel to a tesla instead
        channel_to_t_ind = {}
        for t_ind, channels in channel_assignments.items():
            for channel in channels:
                channel_to_t_ind[channel] = t_ind
                
        active_count = {}
        max_count = {}
        active_notes = {}
        unassigned_channel = []
        curr_time = -1
        midi = md.MidiFile(filepath[1:-1])
        for msg in midi.merged_track:
            if hasattr(msg, "channel") and msg.channel in channel_to_t_ind:
                channel = msg.channel
                t_ind = channel_to_t_ind[channel]
                
                if t_ind not in active_count:
                    active_count[t_ind] = 0
                    max_count[t_ind] = 0
                    active_notes[t_ind] = {}
                
                note_counts = active_notes[t_ind]
                if msg.type == "note_on" and msg.velocity > 0:
                    note_counts[msg.note] = note_counts.get(msg.note, 0) + 1
                    active_count[t_ind] += 1

                    max_count[t_ind] = max(max_count[t_ind],active_count[t_ind])

                elif msg.type == "note_off" or (msg.type == "note_on" and msg.velocity == 0):
                    if msg.note in note_counts:
                        note_counts[msg.note] -= 1
                        active_count[t_ind] -= 1
            
            # we verify if a note is played in a non assigned channel. it gives an error if that is the case
            elif hasattr(msg, "channel") and msg.channel not in channel_to_t_ind and msg.type == "note_on" and msg.channel not in unassigned_channel: 
                unassigned_channel.append(msg.channel)
                
                
            if hasattr(msg, "program") and msg.program > 9:
                errors.append(f"Error : Enveloppe chosen n°{msg.program} is invalid.")

        for t_ind in sorted(channel_assignments):
            peak = max_count.get(t_ind, 0)

            if peak > 3:
                errors.append(f"Error : Tesla n°{t_ind} uses {peak} simultaneous notes.")
            elif peak == 3:
                warnings.append(f"Warning : Tesla n°{t_ind} uses 3 simultaneous notes.")
            else:
                successes.append(f"Success : Tesla n°{t_ind} uses at most {peak} simultaneous notes.")
        
        for chann in unassigned_channel:
            errors.append(f"Error : Bad channel assignment. Channel n°{chann} used when it is not assigned.")

        return (errors, warnings, successes)
            


   
#f1 = "midi_tests/tst.mid"
#f2 = "midi_tests/148BPM_mel.mid"
#f3 = "miditools/midi_tests/148BPM_chords.mid"

#a = MidiManager.merge([f1, f2], "miditools/midi_tests/svppp.mid")
#assigmnt = dict()
#assigmnt[1] = set([1])
#print(MidiManager.verify(f1, assigmnt))
# #time added = k*numerator/bpm
