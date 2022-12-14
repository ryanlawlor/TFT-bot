"""
Team composition used by the bot
Comps come from https://tftactics.gg/tierlist/team-comps
Items are in camel case and a-Z
"""

COMP = {"Ezreal": {"board_position": 0,
                   "items": ["InfinityEdge", "BlueBuff", "JewledGauntlet"],
                   "level": 3,
                   "final_comp": True},
        "Twitch": {"board_position": 1,
                   "items": [],
                   "items": [],
                   "level": 2,
                   "final_comp": True},
        "Xayah": {"board_position": 6,
                  "items": ["GiantSlayer", "RunaansHurricane"],
                  "level": 2,
                  "final_comp": True},
        "Varus": {"board_position": 2,
                  "items": [],
                  "level": 2,
                  "final_comp": True},
        "Rakan": {"board_position": 15,
                 "items": ["SunfireCape"],
                 "level": 2,
                 "final_comp": True},
        "Nasus": {"board_position": 23,
                 "items": [],
                 "level": 3,
                 "final_comp": True},
        "Leona": {"board_position": 24,
                   "items": ["WarmogsArmor", "DragonsClaw"],
                   "level": 3,
                   "final_comp": True},
        "Braum  ": {"board_position": 25,
                    "items": [],
                    "level": 3,
                    "final_comp": True},
        }

# No logic for certain augments meaning the bot won't know what to do if they are included in here
# (Anything that changes gameplay or adds something to the bench).
AUGMENTS = ["Guild Heart", "Press the Attack", "Weakspot", "Celestial Blessing", "Stand United", "Electrocharge",
            "Cybernetic Uplink", "Cybernetic Implants",
            "Cybernetic Shell", "Tri Force",
            "Gadget Expert", "Metabolic Accelerator", "Second Wind",
            "Luden's Echo", "Last Stand", "Ascension",
            "Tiny Titans", "Sunfire Board", "Wise Spending",
            "Component Grab Bag", "Featherweights", "Thrill of the Hunt",
            "Preparation", "Blue Battery", "Hustler", "Windfall",
            "Verdant Veil", "First Aid Kit", "Rich Get Richer", "New Recuit",
            "Combat Training", "Meditation", "Axiom Arc", "Band of Thieves", "Item Grab Bag","Level Up", "High End Shopping", "Future Sight", "Heart"]


def champions_to_buy() -> list:
    """Creates a list of champions to buy during the game"""
    champs_to_buy = []
    for champion, champion_data in COMP.items():
        if champion_data['level'] == 1:
            champs_to_buy.append(champion)
        elif champion_data['level'] == 2:
            champs_to_buy.extend([champion] * 3)
        elif champion_data['level'] == 3:
            champs_to_buy.extend([champion] * 9)
        else:
            raise Exception(
                "Comps.py | Champion level must be a valid level (1-3)")
    return champs_to_buy


def get_unknown_slots() -> list:
    """Creates a list of slots on the board that don't have a champion from the team composition"""
    container = []
    for _, champion_data in COMP.items():
        container.append(champion_data["board_position"])
    return [n for n in range(27) if n not in container]
