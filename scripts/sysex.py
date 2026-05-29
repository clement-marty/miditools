import os
import sys
import mido


class SysExConfiguration:

    def __init__(self, channel_assignments: dict[int, set[int]], parameters: dict[int, dict[str, any]]) -> None:
        '''Creates a SysExConfiguration instance
        
        :param dict[int, set[int]] channel assignments: The dictionnary of channel assignments. 
            It associates to each tesla coil id the set of its assigned channels
            {coil_id: {channel_ids}}
        :param dict[int, dict[str, any]] parameters: The tesla coils' parameters
            It associates to each tesla coil id the dictionnary of its parameters.
            {coil_id: {parameter: value}}
        '''
        self.channel_assignments = channel_assignments
        self.parameters = parameters

    def get_syfoh_commands(self) -> list[str]:
        '''Returns the configuration's commands in the SyFoh format
        '''
        commands = [
            'set enable for mode midi-live to 1' # Default configuration command required for all midi files
        ]

        # Assign the channels
        for coil_id, channels in self.channel_assignments.items():
            # Channels are assigned using a decimal number obtained from a 16-digit binary number,
            # in which the n-th digit is set to 1 if the n-th channel is assigned to the considered tesla coil.
            # For example:
            #   dec(5) = bin(0000 0000 0000 0101)
            #   Here we assign the channels 0 and 2
            chn_bin = 0
            for chn in channels:
                chn_bin += 2 ** chn
            commands.append(f'set midi-coil-chns for mode midi-live and coil {coil_id} to {chn_bin}')

        # Set the parameters if specified:
        allowed_parameters = ['duty', 'ontime']
        for p in allowed_parameters:
            for coil_id, params in self.parameters.items():
                value = params.get(p, None)
                if value is not None:
                    commands.append(f'set {p} for mode midi-live and coil {coil_id} to {value}')

        return commands

    def get_sysex_events(self) -> list[mido.Message]:
        '''Creates and returns the configuration's SysEx events
        
        :return list[mido.Message]: The list of SysEx events corresponding to the configuration
        '''
        commands = self.get_syfoh_commands()
        events = []

        python_path = sys.executable
        syfoh_path = 'Syfoh/Syfoh.py'
        tempfile_path = 'scripts/temp.txt'
        for cmd in commands:

            # Convert the textual command to a list of bytes, using the SyFoh format
            # The -i option is used to specify the command
            # the -m option specifies that the output must be in hexadecimal format,
            # and the -o option specifies the temporary output file we use
            os.system(f'{python_path} {syfoh_path} -i "{cmd}" -m HEX -o {tempfile_path}')
            with open(tempfile_path, 'r') as f:
                # Load the hexadecimal data from the temporary file, and convert it to a list of integers
                # We also remove the first and last byte, which are the start and end bytes of the SysEx message,
                #   as they are automatically added by mido when creating the message
                hex_data = f.read().split(' ')[1:-1]

                # Convert the hexadecimal data to a list of integers
                int_data = [int(x, 16) for x in hex_data]

                # Create the SysEx message and add it to the list of events
                event = mido.Message('sysex', data=int_data)
                events.append(event)

        return events