import enum

class SlotTitles(enum.Enum):
    INFORM = 0
    REFUSE = 1
    REASSURE = 2
    APOLOGIZE = 3

class IntentProfile:
    _apologize : float
    _inform : float
    _refuse : float
    _reassure : float

    def __init__(self, apologize : float = 1, inform : float = 1, refuse : float = 1, reassure : float = 1) -> None:
        self._apologize = apologize
        self._inform = inform
        self._refuse = refuse
        self._reassure = reassure

    def average_difference(self, other : "IntentProfile") -> float:
        """
        Returns the average difference between this profile and `other` profile
        """
        a = self._apologize - other._apologize
        b = self._inform - other._inform
        c = self._refuse - other._refuse
        d = self._reassure - other._reassure

        return (a + b + c + d)/4
