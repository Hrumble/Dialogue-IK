from globals import IntentProfile, SlotTitles

class SlotRealization:
    _type : SlotTitles
    _value : str
    _profile : IntentProfile

    def __init__(self, type : SlotTitles, value : str, profile : IntentProfile) -> None:
        self._type = type
        self._value = value
        self._profile = profile
        
