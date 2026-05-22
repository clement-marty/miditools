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
        pass
