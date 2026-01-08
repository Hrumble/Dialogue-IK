from globals import IntentProfile, SlotTitles


class Structure:
    _required_slots : list[SlotTitles]
    _value : IntentProfile

    def __init__(self, required : list[SlotTitles], value : IntentProfile) -> None:
        self._required_slots = required
        self._value = value

