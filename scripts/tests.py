import mido as md
import os
from pathlib import Path
from midi_manager import MidiManager

def get_messages(filepath: str) -> list[tuple]:
    """
    Returns all MIDI messages with their absolute time.

    Parameters:
     - filepath: string,  which contains the path of the midi file

    Returns: 
     - messages: list of tuples, which contains the discrition parameters of midi file 
    """
    midi_file = md.MidiFile(filepath)
    messages = []
    for track_index, track in enumerate(midi_file.tracks):
        absolute_time = 0
        for message in track:
            absolute_time += message.time
            if message.type != 'end_of_track':
                midi_message = (track_index, absolute_time, message.type,  getattr(message, 'note', None), getattr(message, 'velocity', None), getattr(message, 'channel', None))
                messages.append(midi_message)
    return messages


def compare_files(file_1: str, file_2: str):
    """
    Compares two MIDI files. Returns boolean as a result

    Parameters: 
     - file_1: string, containing the path for file 1
     - file_2: string, containing the path for file 2
    
     Retuns:
     - same: boolean, that contains the result that is due to the comparison of two files
    """
    messages_1 = get_messages(file_1)
    messages_2 = get_messages(file_2)
    same = True
    if len(messages_1) != len(messages_2):
        print('The files do not contain the same number of messages.')
        same = False
    else:
        for i in range(len(messages_1)):
            if messages_1[i] != messages_2[i]:
                print(f'Difference found at message {i}')
                print('Generated file:')
                print(messages_1[i])
                print('Reference file:')
                print(messages_2[i])
                same = False
    return same


def print_timeline(filepath: str) -> None:
    """
    Displays all MIDI messages with their time.

    Parameters:
     - filepath: string,  which contains the path of the midi file

    Returns:
      Nothing
      Prints the time of the midi file
    """
    midi_file = md.MidiFile(filepath)
    print(f'\nTimeline of {filepath}\n')
    for track_index, track in enumerate(midi_file.tracks):
        print(f'Track {track_index}')
        absolute_time = 0
        for message in track:
            absolute_time += message.time
            if message.type != 'end_of_track':
                print(absolute_time, message)
        print()


def test_merge(input_files: list[str], generated_file: str, reference_file: str) -> None:
    """
    Tests the merge function.

    Parameters:
     - input_files: list of strings, contains the paths of the mido files to test
     - generated_file: string, the path of generated file
     - reference_file: string, the path of the reference file
    """
    MidiManager.merge(input_files, generated_file)
    result = compare_files(generated_file, reference_file)
    print('\nTest result:')
    if result:
        print('SUCCESS')
    else:
      print('ERROR')

    print_timeline(generated_file)
    print_timeline(reference_file)


if __name__ == '__main__':

    input_files = ["midi_tests/125BPM_mel.mid", "midi_tests/125BPM_mel.mid"]
    generated_file = "midi_tests/generated.mid"
    reference_file = "midi_tests/reference.mid"
    test_merge(input_files, generated_file, reference_file)
