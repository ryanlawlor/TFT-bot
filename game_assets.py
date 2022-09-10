"""
Contains static item & champion data
"""

COMBINED_ITEMS = {"BFSword", "ChainVest", "GiantsBelt", "NeedlesslyLargeRod",
                  "NegatronCloak", "RecurveBow", "SparringGloves", "Spatula", "TearoftheGoddess",
                  "ArchangelsStaff", "BansheesClaw", "Bloodthirster",
                  "BlueBuff", "BrambleVest", "CavalierEmblem", "ChaliceofPower",
                  "Deathblade", "DragonmancerEmblem", "DragonsClaw", "EdgeofNight",
                  "GargoyleStoneplate", "GiantSlayer", "GuardianEmblem", "GuinsoosRageblade", 
                  "HandofJustice", "HextechGunblade", "InfinityEdge", "IonicSpark", "JeweledGauntlet",
                  "LagoonEmblem", "LastWhisper", "LocketoftheIronSolari", "MageEmblem", "MirageEmblem",
                  "Morellonomicon", "ProtectorsVow", "Quicksilver", "RabadonsDeathcap",
                  "RapidFirecannon", "Redemption", "RunaansHurricane", "ShimmerscaleEmblem",
                  "ShroudofStillness", "SpearofShojin", "StatikkShiv", "SunfireCape", "SwiftshotEmblem",
                  "TacticiansCrown", "ThiefsGloves", "TitansResolve", "WarmogsArmor",
                  "ZekesHerald", "Zephyr", "ZZRotPortal"}
                

ELUSIVE_ITEMS = {"AssassinEmblem", "BruiserEmblem", "CannoneerEmblem", "DarkflightEmblem",
                 "DragonmancersBlessing", "EvokerEmblem", "GuildEmblem",
                 "JadeEmblem", "MysticEmblem", "RagewingEmblem"
                 "ScalescornEmblem",
                 "TempestEmblem", "WarriorEmblem"}

SHIMMERSCALE_ITEMS = {"CrownOfChampions", "DeterminedInvestor", "DiamondHands",
                      "DravensAxe", "GamblersBlade", "GoldmancersStaff",
                      "MogulsMail", "NeedlesslyBigGem"}

ORNN_ITEMS = {"AnimaVisage", "DeathsDefiance", "EternalWinter",
              "GoldCollector", "InfinityForce",
              "Manazane", "ObsidianCleaver", "RaduinsSanctum",
              "RocketPropelledFist", "ZhonyasParadox"}

RADIANT_ITEMS = {"Absolution", "BansheesSilence", "BlessedBloodthirster",
                 "BlueBlessing", "BrinkofDawn", "BulwarksOath", "ChaliceofCharity",
                 "CovalentSpark", "DemonSlayer", "DragonsWill",
                 "DvarapalaStoneplate", "EternalWhisper", "FistofFairness",
                 "GlamorousGauntlet", "GuinsoosReckoning",
                 "HextechLifeblade", "LocketofTargonPrime", "LuminousDeathblade",
                 "Mistral", "MoreMoreellonomicon", "Quickestsilver",
                 "RabadonsAscendedDeathcap", "RadiantRedemption", "RapidLightcannon",
                 "RascalsGloves", "RosethornVest", "RunaansTempest",
                 "ShroudofReverance", "SpearofHirana", "StatikkFavor",
                 "SunlightCape", "TitansVow", "UrfAngelsStaff",
                 "WarmogsPride", "ZekesHarmony", "ZenithEdge",
                 "ZzRotsInvitation"}

ITEMS = COMBINED_ITEMS.union(ELUSIVE_ITEMS).union(
    SHIMMERSCALE_ITEMS).union(ORNN_ITEMS).union(RADIANT_ITEMS)

CHAMPIONS = {
    "Ao Shin": {"Gold": 8, "Board Size": 2},
    "Aphelios": {"Gold": 2, "Board Size": 1},
    "Aurelion Sol": {"Gold": 8, "Board Size": 2},
    "Bard": {"Gold": 5, "Board Size": 1},
    "Braum": {"Gold": 2, "Board Size": 1},
    "Daeja": {"Gold": 7, "Board Size": 2},
    "Diana": {"Gold": 3, "Board Size": 1},
    "Dragon Tyrant Swain": {"Gold": 7, "Board Size": 2},
    "Ezreal": {"Gold": 1, "Board Size": 1},
    "Gnar": {"Gold": 2, "Board Size": 1},
    "Graves": {"Gold": 4, "Board Size": 1},
    "Hecarim": {"Gold": 4, "Board Size": 1},
    "Heimerdinger": {"Gold": 3, "Board Size": 1},
    "Idas": {"Gold": 7, "Board Size": 2},
    "Jax": {"Gold": 2, "Board Size": 1},
    "Jayce": {"Gold": 4, "Board Size": 1},
    "Kai'Sa": {"Gold": 2, "Board Size": 1},
    "Karma": {"Gold": 1, "Board Size": 1},
    "Lee Sin": {"Gold": 3, "Board Size": 1},
    "Leona": {"Gold": 1, "Board Size": 1},
    "Lillia": {"Gold": 2, "Board Size": 1},
    "Lulu": {"Gold": 3, "Board Size": 1},
    "Lux": {"Gold": 2, "Board Size": 1},
    "Malphite": {"Gold": 1, "Board Size": 1},
    "Nasus": {"Gold": 1, "Board Size": 1},
    "Nidalee": {"Gold": 1, "Board Size": 1},
    "Nilah": {"Gold": 4, "Board Size": 1},
    "Nomsy": {"Gold": 6, "Board Size": 2},
    "Nunu": {"Gold": 3, "Board Size": 1},
    "Olaf": {"Gold": 3, "Board Size": 1},
    "Pantheon": {"Gold": 4, "Board Size": 1},
    "Qiyana": {"Gold": 2, "Board Size": 1},
    "Rakan": {"Gold": 3, "Board Size": 1},
    "Rell": {"Gold": 2, "Board Size": 1},
    "Rengar": {"Gold": 3, "Board Size": 1},
    "Sejuani": {"Gold": 1, "Board Size": 1},
    "Senna": {"Gold": 1, "Board Size": 1},
    "Seraphine": {"Gold": 3, "Board Size": 1},
    "Sett": {"Gold": 1, "Board Size": 1},
    "Shi Oh Yu": {"Gold": 7, "Board Size": 2},
    "Shyvana": {"Gold": 8, "Board Size": 2},
    "Skarner": {"Gold": 1, "Board Size": 1},
    "Sohm": {"Gold": 7, "Board Size": 2},
    "Soraka": {"Gold": 5, "Board Size": 1},
    "Syfen": {"Gold": 7, "Board Size": 2},
    "Sylas": {"Gold": 3, "Board Size": 1},
    "Taliyah": {"Gold": 1, "Board Size": 1},
    "Terra": {"Gold": 8, "Board Size": 2},
    "Tristana": {"Gold": 3, "Board Size": 1},
    "Twitch": {"Gold": 2, "Board Size": 1},
    "Varus": {"Gold": 3, "Board Size": 1},
    "Vladmir": {"Gold": 1, "Board Size": 1},
    "Volibear": {"Gold": 3, "Board Size": 1},
    "Wukong": {"Gold": 1, "Board Size": 1},
    "Xayah": {"Gold": 4, "Board Size": 1},
    "Yasuo": {"Gold": 5, "Board Size": 1},
    "Yone": {"Gold": 2, "Board Size": 1},
    "Zac": {"Gold": 2, "Board Size": 1},
    "Zeri": {"Gold": 3, "Board Size": 1},
    "Zippy": {"Gold": 6, "Board Size": 2},
    "Zoe": {"Gold": 5, "Board Size": 1},
    "Zyra": {"Gold": 2, "Board Size": 1}}

ROUNDS = {"1-1", "1-2", "1-3", "1-4",
          "2-1", "2-2", "2-3", "2-4", "2-5", "2-6", "2-7",
          "3-1", "3-2", "3-3", "3-4", "3-5", "3-6", "3-7",
          "4-1", "4-2", "4-3", "4-4", "4-5", "4-6", "4-7",
          "5-1", "5-2", "5-3", "5-4", "5-5", "5-6", "5-7",
          "6-1", "6-2", "6-3", "6-4", "6-5", "6-6", "6-7",
          "7-1", "7-2", "7-3", "7-4", "7-5", "7-6", "7-7"}

CAROUSEL_ROUND = {"1-1", "2-4", "3-4", "4-4", "5-4", "6-4", "7-4"}

PVE_ROUND = {"1-2", "1-3", "1-4", "2-7", "3-7", "4-7", "5-7", "6-7", "7-7"}

PVP_ROUND = {"2-1", "2-2", "2-3", "2-5", "2-6",
             "3-1", "3-2", "3-3", "3-5", "3-6",
             "4-1", "4-2", "4-3", "4-5", "4-6",
             "5-1", "5-2", "5-3", "5-5", "5-6",
             "6-1", "6-2", "6-3", "6-5", "6-6",
             "7-1", "7-2", "7-3", "7-5", "7-6"}

PICKUP_ROUNDS = {"2-1", "3-1", "4-1", "5-1", "6-1", "7-1"}

AUGMENT_ROUNDS = {"2-1", "3-2", "4-2"}

ITEM_PLACEMENT_ROUNDS = {"2-1", "3-1", "4-1", "5-1",
                         "6-1", "7-1", "2-5", "3-5", "4-5", "5-5", "6-5", "7-5"}

# ITEM_PLACEMENT_ROUNDS = {"2-2", "3-2", "4-2", "5-2",
#                          "6-2", "7-2", "2-5", "3-5", "4-5", "5-5", "6-5", "7-5"}

FINAL_COMP_ROUND = "4-5"

FULL_ITEMS = {"ArchangelsStaff": ("NeedlesslyLargeRod", "TearoftheGoddess"),
              "BansheesClaw": ("GiantsBelt", "SparringGloves"),
              "Bloodthirster": ("BFSword", "NegatronCloak"),
              "BlueBuff": ("TearoftheGoddess", "TearoftheGoddess"),
              "BrambleVest": ("ChainVest", "ChainVest"),
              "CavalierEmblem": ("ChainVest", "Spatula"),
              "ChaliceofPower": ("NegatronCloak", "TearoftheGoddess"),
              "Deathblade": ("BFSword", "BFSword"),
              "DragonmancerEmblem": ("NeedlesslyLargeRod", "Spatula"),
              "DragonsClaw": ("NegatronCloak", "NegatronCloak"),
              "EdgeofNight": ("BFSword", "ChainVest"),
              "GargoyleStoneplate": ("ChainVest", "NegatronCloak"),
              "GiantSlayer": ("BFSword", "RecurveBow"),
              "GuardianEmblem": ("GiantsBelt", "Spatula"),
              "GuinsoosRageblade": ("NeedlesslyLargeRod", "RecurveBow"),
              "HandofJustice": ("SparringGloves", "TearoftheGoddess"),
              "HextechGunblade": ("BFSword", "NeedlesslyLargeRod"),
              "InfinityEdge": ("BFSword", "SparringGloves"),
              "IonicSpark": ("NeedlesslyLargeRod", "NegatronCloak"),
              "JeweledGauntlet": ("NeedlesslyLargeRod", "SparringGloves"),
              "LagoonEmblem": ("SparringGloves", "Spatula"),
              "LastWhisper": ("RecurveBow", "SparringGloves"),
              "LocketoftheIronSolari": ("ChainVest", "NeedlesslyLargeRod"),
              "MageEmblem": ("TearoftheGoddess", "Spatula"),
              "MirageEmblem": ("NegatronCloak", "Spatula"),
              "Morellonomicon": ("GiantsBelt", "NeedlesslyLargeRod"),
              "ProtectorsVow": ("ChainVest", "TearoftheGoddess"),
              "Quicksilver": ("NegatronCloak", "SparringGloves"),
              "RabadonsDeathcap": ("NeedlesslyLargeRod", "NeedlesslyLargeRod"),
              "RapidFirecannon": ("RecurveBow", "RecurveBow"),
              "Redemption": ("GiantsBelt", "TearoftheGoddess"),
              "RunaansHurricane": ("NegatronCloak", "RecurveBow"),
              "ShimmerscaleEmblem": ("BFSword", "Spatula"),
              "ShroudofStillness": ("ChainVest", "SparringGloves"),
              "SpearofShojin": ("BFSword", "TearoftheGoddess"),
              "StatikkShiv": ("RecurveBow", "TearoftheGoddess"),
              "SunfireCape": ("ChainVest", "GiantsBelt"),
              "SwiftshotEmblem": ("RecurveBow", "Spatula"),
              "TacticiansCrown": ("Spatula", "Spatula"),
              "ThiefsGloves": ("SparringGloves", "SparringGloves"),
              "TitansResolve": ("ChainVest", "RecurveBow"),
              "WarmogsArmor": ("GiantsBelt", "GiantsBelt"),
              "ZekesHerald": ("BFSword", "GiantsBelt"),
              "Zephyr": ("GiantsBelt", "NegatronCloak"),
              "ZzRotPortal": ("GiantsBelt", "RecurveBow")
              }


def champion_board_size(champion: str) -> int:
    """Takes a string (champion name) and returns board size of champion"""
    return CHAMPIONS[champion]["Board Size"]


def champion_gold_cost(champion: str) -> int:
    """Takes a string (champion name) and returns gold of champion"""
    return CHAMPIONS[champion]["Gold"]
