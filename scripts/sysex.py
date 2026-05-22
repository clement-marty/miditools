import mido


class SysExConfiguration:

    def __init__(self, channel_assignments: dict[int, set[int]], parameters: dict[int, dict[str, int|float]]) -> None:
        '''Creates a SysExConfiguration instance
        
        :param dict[int, set[int]] channel assignments: The dictionnary of channel assignments. 
            It associates to each tesla coil id the set of its assigned channels
            {coil_id: {channel_ids}}
        :param dict[int, dict[str, int|float]] parameters: The tesla coils' parameters
            It associates to each tesla coil id the dictionnary of its parameters.
            {coil_id: {parameter: value}}
        '''
        self.channel_assignments = channel_assignments
        self.parameters = parameters

    def get_syfoh_commands(self) -> list[str]:
        pass

    def get_sysex_events(self) -> list[mido.Message]:
        pass
