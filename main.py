from globals import IntentProfile, SlotTitles
from slot_realization import SlotRealization
from structure import Structure

slot_realization : dict = {
    SlotTitles.REFUSE : [
        SlotRealization(SlotTitles.REFUSE, "i can't let you do that", profile=IntentProfile(refuse=.8)),
        SlotRealization(SlotTitles.REFUSE, "that's impossible", profile=IntentProfile(refuse=1)),
        SlotRealization(SlotTitles.REFUSE, "no, that won't do", profile=IntentProfile(refuse=.5)),
    ],
    SlotTitles.APOLOGIZE : [
        SlotRealization(SlotTitles.APOLOGIZE, "i'm sorry", profile=IntentProfile(apologize=.5)),
        SlotRealization(SlotTitles.APOLOGIZE, "unfortunately", profile=IntentProfile(apologize=.3)),
        SlotRealization(SlotTitles.APOLOGIZE, "forgive me", profile=IntentProfile(apologize=.8)),
    ],
    SlotTitles.REASSURE : [
        SlotRealization(SlotTitles.REASSURE, "it's going to be okay", profile=IntentProfile(reassure=.9)),
        SlotRealization(SlotTitles.REASSURE, "don't worry", profile=IntentProfile(reassure=.5)),
        SlotRealization(SlotTitles.REASSURE, "fear not", profile=IntentProfile(reassure=.4)),
    ]
}

structures : dict = {
    "refusal" : Structure(required=[SlotTitles.REFUSE], value=IntentProfile(refuse=1)),
    "soft_refusal" : Structure(required=[SlotTitles.APOLOGIZE, SlotTitles.REFUSE], value=IntentProfile(refuse=1, apologize=.3)),
    "reassure" : Structure(required=[SlotTitles.REASSURE], value=IntentProfile(reassure=1)),
}

def generate(profile : IntentProfile) -> str:
    struct : Structure | None = None
    prev_avg_diff : float = 100

    for s in structures.values():
        mean_diff = abs(s._value.average_difference(profile))
        print(f"Testing {s._required_slots}, diff: {mean_diff}")

        if struct == None or mean_diff < prev_avg_diff:
            struct = s
            prev_avg_diff = mean_diff

    assert(struct != None)

    sentence = ""
    current_avg_diff : float = prev_avg_diff

    for req in struct._required_slots:
        slot = ""
        prev_avg_diff = 100

        for s in slot_realization[req]:
            mean_diff = abs(current_avg_diff + s._profile.average_difference(profile))
            if slot == "" or mean_diff < prev_avg_diff:
                slot = s._value

        sentence += slot
    return sentence

print(generate(IntentProfile(reassure=1)))
