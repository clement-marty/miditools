import mido


class SysExConfiguration:

    def __init__(self, channel_assignments: dict[int, set[int]], parameters: dict[str, int|float]) -> None:
        pass

    def get_syfoh_commands(self) -> list[str]:
        pass

    def get_sysex_events(self) -> list[mido.Message]:
        pass
