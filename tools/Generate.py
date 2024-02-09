import random
import json
from datetime import datetime

# Predefined lists for character attributes
genders = [
    'Male', 
    'Female'
]
races = [
    'Drow', 'Elf (Wood)', 'High Elf', 'Half-Orc', 'Human', 'Air Genasi', 'Dragonborn', 
    'Gnome', 'Forest Gnome', 'Rock Gnome', 'Deep Gnome (Svirfneblin)', 'Hill Dwarf', 
    'Mountain Dwarf', 'Halfling', 'Lightfoot Halfling', 'Stout Halfling', 'Dwarf', 
    'Scourge Aasimar', 'Fallen Aasimar', 'Earth Genasi', 'Fire Genasi', 'Water Genasi', 
    'Goblin', 'Loxodon', 'Minotaur', 'Simic Hybrid', 'Kalashtar', 'Beasthide', 
    'Longtooth', 'Swiftstride', 'Wildhunt', 'Owlin', 'Fairy', 'Rabbitfolk (Harengon)', 
    'Centaur', 'Aasimar', 'Orc', 'Tiefling', 'Kenku', 'Goliath', 'Aarakocra', 'Triton', 
    'Firbolg', 'Tabaxi', 'Lizardfolk', 'Yuan-ti Pureblood', 'Satyr', 'Warforged', 
    'Changeling', 'Kobold', 'Bugbear', 'Githyanki', 'Githzerai', 'Hobgoblin', 
    'Leonin', 'Vedalken', 'Tortle'
]
race_details = {
    'Drow': {
        'last_names': ['Nightbreeze', 'Shadowend', 'Darkweaver', 'Silkshadow', 'Moonfall', 'Frostweb', 'Ravenhold', 'Gloomstalker', 'Spiderkiss', 'Darkspire', 'Nightwhisper', 'Venomstar', 'Shadowveil', 'Webstrider', 'Silentwhisper', 'Deathweaver', 'Starless', 'Voidwalker', 'Sablestalker', 'Obsidianheart', 'Grimshade', 'Duskgloom', 'Blackveil', 'Ironweb', 'Thornspire', 'Moonshadow', 'Darkmantle', 'Twilightveil', 'Nightshade', 'Silentdusk', 'Cobweb', 'Sableweb', 'Onyxheart', 'Twilightshroud', 'Shadowsong', 'Gloomweaver', 'Nightserpent', 'Darkmoon', 'Silverweb', 'Shadowdance', 'Gloomsinger', 'Whisperwind', 'Duskweaver', 'Shadowthorn', 'Frostshadow', 'Twilightthorn', 'Starweaver', 'Nightraven', 'Shadowflame', 'Dusksinger', 'Sablecloak', 'Darkwhisper', 'Nightfall', 'Shadowcry', 'Gloomblade', 'Veilwalker', 'Spidersong', 'Duskshadow', 'Stargloom', 'Darkbloom', 'Nightbloom', 'Shadowbloom', 'Frostveil', 'Darkfrost', 'Gloomfrost', 'Shadowgale', 'Nightgale', 'Darkgale', 'Stormshadow', 'Shadowstorm', 'Darkstorm', 'Nightstorm', 'Veilstorm', 'Stormveil', 'Gloomstorm', 'Froststorm', 'Icewhisper', 'Iceshadow', 'Shadowice', 'Darkice', 'Nightice', 'Gloomice', 'Frostbite', 'Icebite', 'Shadowbite', 'Nightbite', 'Darkbite'],
        'archetypes': ['Rogue', 'Sorcerer', 'Warlock', 'Cleric', 'Assassin', 'Enchanter', 'Necromancer', 'Blade Singer'],
        'backgrounds': ['Spy', 'Noble', 'Exile', 'Priestess', 'Underdark Scout', 'House Agent', 'Renegade', 'Shadow Merchant', 'Arcane Scholar'],
        'innate_abilities': ['Superior Darkvision', 'Drow Magic (Dancing Lights, Darkness, Faerie Fire)', 'Sunlight Sensitivity'],
        'preferred_classes': ['Rogue', 'Sorcerer', 'Cleric of Lolth', 'Warlock'],
        'culture': 'Matriarchal, deeply religious, and hierarchical. Drow society is built around the worship of Lolth, the Spider Queen, which influences their love for darkness, spiders, and betrayal.',
        "lore": "Drow, also known as dark elves, are a subrace of elves that have been exiled from the surface world and have made their home in the subterranean depths of the Underdark. Their society is matriarchal, worshiping the goddess Lolth, the Spider Queen, who encourages the ruthless suppression of weakness, leading to a culture rife with treachery and intrigue. Known for their cruelty and disdain for other races, Drow are feared and shunned by those on the surface. Despite this, they are a highly intelligent, charismatic, and agile race, with an innate affinity for powerful magic and a deep connection to arachnids.",
        'alignment': ["Chaotic Evil",  
            "Chaotic Neutral", 
            "Neutral Evil",  
            "True Neutral", 
            "Lawful Evil"
            ],
        "physical_characteristics": {
            'Male': {'height': (160, 190), 'weight': (60, 80)},
            'Female': {'height': (155, 185), 'weight': (55, 75)}
        },
        "male_names": [
            "Adinir", "Belaern", "Caelkoth", "Dhaunae", "Elaith", "Ghaunil", "Ilivar", "Jaelryn", "Kyrnol", "Lualyrr",
            "Malaggar", "Nadal", "Omareth", "Pharaun", "Quave", "Rizzen", "Solaufein", "Taldinyon", "Ulvir", "Vorn",
            "Waelvor", "Xundus", "Yazston", "Zaknafein", "Ardul", "Brorn", "Drisinil", "Felyndiira", "Halisstra", "Iymril"
        ],
        "female_names": [
            "Akordia", "Briza", "Charinida", "Drada", "Eclavdra", "Faeryl", "G'eldriia", "Haelra", "Ilharess", "Jezzara",
            "Khalazza", "Laele", "Maya", "Nizana", "Olorae", "Pellanistra", "Quenthel", "Rilrae", "SiNafay", "Talabrina",
            "Ulitree", "Viconia", "Waerva", "Xullrae", "Yvonnel", "Z'ress", "Alaunira", "Belarbreena", "Chalithra", "Dalninil",
            "Elendar", "Fel'rekt", "Ghaundan"
        ]
    },
    "Elf (Wood)": {
        "last_names": ["Amakiir (Gemflower)", "Amastacia (Starflower)", "Galanodel (Moonwhisper)", "Holimion (Diamonddew)", "Ilphelkiir (Gemblossom)", "Siannodel (Moonbrook)", "Xiloscient (Goldpetal)", "Liadon (Silverfrond)", "Meliamne (Oakenheel)", "Naïlo (Nightbreeze)"],
        "archetypes": ["Ranger", "Druid", "Scout", "Hunter", "Beastmaster", "Protector"],
        "backgrounds": ["Outlander", "Hermit", "Forester", "Guide", "Exile", "Folk Hero"],
        "innate_abilities": ["Mask of the Wild", "Fey Ancestry", "Trance", "Keen Senses", "Elf Weapon Training"],
        "preferred_classes": ["Ranger", "Druid", "Rogue", "Fighter"],
        "culture": "Wood Elves live in close-knit communities deeply integrated into forests and wild areas. They have a profound respect for nature, leading lives that seek to preserve the balance and beauty of their natural surroundings.",
        "lore": "Wood Elves, known for their affinity with nature, stealth, and keen senses, are well-suited to life in the wilderness. They tend to be more reclusive than their High Elf kin, living in harmony with the natural world. This connection with nature makes them exceptional Rangers and Druids, roles that capitalize on their skills in tracking, survival, and nature magic.",
        "alignment": [
            "Neutral Good",
            "True Neutral",
            "Chaotic Good"
        ],
        "physical_characteristics": {
            "Male": {'height':  (170, 200), 'weight': (60, 80)},
            "Female": {'height': (160,190), 'weight': (50,70)}
        },
        "male_names": [
            "Adran", "Aelar", "Aramil", "Arannis", "Aust", "Beiro", "Berrian", "Carric", "Enialis", "Erdan",
            "Galinndan", "Hadarai", "Heian", "Himo", "Immeral", "Ivellios", "Laucian", "Mindartis", "Paelias", "Peren",
            "Quarion", "Riardon", "Rolen", "Soveliss", "Thamior", "Tharivol", "Theren", "Varis"
        ],
        "female_names": [
            "Adrie", "Althaea", "Anastrianna", "Andraste", "Antinua", "Bethrynna", "Birel", "Caelynn", "Drusilia", "Enna",
            "Felosial", "Ielenia", "Jelenneth", "Keyleth", "Leshanna", "Lia", "Meriele", "Mialee", "Naivara", "Quelenna",
            "Quillathe", "Sariel", "Shanairra", "Shava", "Silaqui", "Theirastra", "Thia", "Vadania", "Valanthe", "Xanaphia"
        ]
    },
    "High Elf": {
        "last_names": [
            "Moonshadow", "Starweaver", "Sunstrider", "Dawndancer", "Lightshaper", "Nightsinger",
            "Silverbough", "Glimmeringleaf", "Skygazer", "Feywinds", "Everbloom", "Duskwalker",
            "Gleamingstar", "Dawnwhisper", "Auroraseeker", "Twilightborne", "Starfallen", "Moonlit",
            "Sunspark", "Glowingquill", "Eldertree", "Brightblade", "Spellbound", "Gleamglade",
            "Mysticstream", "Shimmerleaf"
        ],
        "archetypes": ["Wizard", "Sorcerer", "Arcanist", "Scholar", "Mage", "Spellblade"],
        "backgrounds": ["Sage", "Noble", "Scholar", "Artisan", "Magistrate", "Advisor"],
        "innate_abilities": ["Cantrip", "Fey Ancestry", "Trance", "Keen Senses", "Elf Weapon Training", "High Elf Magic"],
        "culture": "High Elf society is one of ancient traditions, valuing art, music, and the pursuit of arcane knowledge. Living in magnificent cities and secluded enclaves, they are closely tied to nature and the magical energies that flow through the world. High Elves have a deep appreciation for beauty and the finer things in life, often seen as aloof or distant by other races due to their long lifespans and inherent grace.",
        "alignment": [
            "Lawful Good",
            "Lawful Neutral",
            "Neutral Good"
        ],
        "preferred_classes": ["Wizard", "Sorcerer", "Fighter (Eldritch Knight)", "Rogue (Arcane Trickster)"],
        "lore": "High Elves, or Eladrin in some realms, hail from the enchanted forests and the oldest cities, where magic weaves through every aspect of their lives. With lifespans stretching over centuries, they have been pivotal in shaping history, defending their homelands against threats both mundane and arcane. Their societies are led by wise and powerful mages, with councils that govern with a blend of ancient wisdom and a deep understanding of magic's nuances.",
        "physical_characteristics": {
            "Male": {'height': (170, 200), "weight": (60, 80)},
            "Female": {'height': (160, 190), "weight": (50, 70)}
        },
        "male_names": [
            "Alaric", "Alathar", "Bellas", "Calaudron", "Durothil", "Elaith", "Faelar", "Gaerlan", "Haladar", "Ithilnar",
            "Laeroth", "Mirthal", "Naertho", "Othorion", "Paeral", "Quarrel", "Rathal", "Sovel", "Talath", "Uldar",
            "Vaalyun", "Valmaxian", "Xilfir", "Yarma", "Zaltarish", "Aelar", "Aramil", "Aust", "Beiro", "Berrian",
            "Carric", "Enialis", "Erdan", "Galinndan", "Hadarai", "Heian", "Himo", "Immeral", "Ivellios", "Laucian",

        ],
        "female_names": [
            "Alauniira", "Amastacia", "Anaral", "Ariawyn", "Bethrynna", "Caerthynna", "Dilara", "Elasha", "Faelyn", "Ilsevel",
            "Keerthana", "Larien", "Maelyrra", "Naevys", "Olera", "Phaerl", "Renna", "Sarielle", "Tiaathque", "Usara",
            "Venessa", "Yathlanae", "Zephyr", "Aelar", "Aramil", "Aust", "Beiro", "Berrian", "Carric", "Enialis", "Erdan",
            "Galinndan", "Hadarai", "Heian", "Himo", "Immeral", "Ivellios", "Laucian", "Mindartis", "Paelias", "Peren",
        ]
    },
    "Half-Orc": {
        "last_names": ["Ironfist", "Thunderjaw", "Steelskin", "Bloodaxe", "Gorebringer", "Skullsmasher", "Nightstalker", "Bonebreaker", "Ragefist", "Darkstorm", "Stormblade", "Wildheart", "Doomhammer", "Grimgor", "Wolfslayer", "Dragonsbane", "Earthshaker", "Frostborn", "Shadowbane", "Mudfoot", "Raveneye", "Boulderchest", "Thunderstrike", "Ironhide", "Battleborn", "Deathwhisper", "Stormfury", "Rageblood", "Blackblade", "Grimfang"],
        "archetypes": ["Berserker", "Champion", "Guardian", "Reaver", "War Chief", "Mystic Warrior"],
        "backgrounds": ["Soldier", "Mercenary", "Gladiator", "Outcast", "Hunter", "Tribal Nomad", "Bounty Hunter"],
        "innate_abilities": ["Relentless Endurance", "Savage Attacks", "Darkvision", "Menacing", "Powerful Build"],
        "preferred_classes": ["Barbarian", "Fighter", "Paladin", "Ranger", "Warlock"],
        "culture": "Half-Orcs often live on the fringes of both human and orcish societies, carving out a place for themselves through strength and determination. They value strength and honor, often proving themselves as worthy warriors and loyal allies. Their communities are places where strength is respected, but loyalty and honor can forge bonds as strong as any family tie.",
        "lore": "Born of two worlds, half-orcs carry the blood of humans and orcs, a heritage that grants them formidable physical prowess and resilience. Their existence is a testament to both conflict and union between orc and human cultures. Many half-orcs struggle with their identity, facing prejudice from both sides, but they are capable of incredible feats of courage and tenacity.",
        "alignment": [
            "Chaotic Good",
            "Chaotic Neutral",
            "Chaotic Evil",
            "Neutral Good",
            "True Neutral",
            "Neutral Evil",
            "Lawful Good",
            "Lawful Neutral",
            "Lawful Evil"
        ],
        "physical_characteristics": {
            "Male": {'height': (185, 215), 'weight': (80, 110)},
            "Female": {'height': (175, 205), 'weight': (75, 105)}
        },
        "male_names": [
            "Durth", "Brak", "Mok", "Grom", "Thrum", "Hogar", "Drog", "Varg", "Karg", "Gharn", "Rurk", "Thog", "Brogg", "Narg", "Ugarth", "Zogar", "Skar", "Grumbar", "Dorn", "Hurn", "Snorri", "Bolgar", "Fargrim", "Gorlag", "Krothu", "Murg", "Zorth", "Thark", "Ghurz", "Rend"
        ],
        "female_names": [
            "Baggi", "Emen", "Engong", "Kansif", "Myev", "Neega", "Ovak", "Ownka", "Shautha", "Sutha", "Vola", "Volen", "Yevelda", "Zagga", "Arha", "Briga", "Dreh", "Ghuna", "Kiga", "Lagazi", "Morna", "Noga", "Ootah", "Rash", "Tawar", "Ugga", "Vanchu", "Wolgah", "Yurag", "Zelga"
        ]
    },
    "Human": {
        "last_names": [
            "Brightwood", "Stormwind", "Highhill", "Darkwater", "Ironforge", "Lightfoot", "Swiftwind",
            "Greenfield", "Blackstone", "Goldheart", "Trueblade", "Silversmith", "Oakenshield", "Wolfbane",
            "Nightsong", "Dawnbringer", "Riversong", "Starfall", "Moonshadow", "Sunstrider", "Frostbeard",
            "Firehand", "Whitewall", "Redwood", "Bluewater", "Winterbourne", "Summerglen", "Springvale",
            "Autumnridge", "Evermead", "Hawkflight", "Lionheart", "Dragonseeker", "Bearclaw", "Raveneye",
            "Crowfeather", "Eaglewing", "Doveheart", "Sparrowhawk", "Foxglove", "Wolftrack", "Elkrunner",
            "Deerleap", "Falconcrest", "Owltree", "Tigerwillow", "Pantherpaw", "Leopardstride", "Serpentcoil",
            "Ashwood", "Briarheart", "Cinderfell", "Dewmist", "Ebonflow", "Frostvale", "Glimmerstone", "Hollowridge",
            "Ironbound", "Jadeleaf", "Kestrelmoon", "Lighthaven", "Meadowbrook", "Netherwood", "Oathkeeper",
            "Pinehollow", "Quicksilver", "Ravenhold", "Stormcaller", "Thornfield", "Underhill", "Valewatch",
            "Windwhisper", "Yewshade", "Zephyrwind", "Ambergrain", "Boulderback", "Crestwater", "Dawnriver",
            "Emberheart", "Fairwind", "Grainfall", "Harborlight", "Icetide", "Junipergrove", "Kingshaven",
            "Lakeshore", "Marshland", "Nightbloom", "Oakenspire", "Pearlshore", "Quarryfist", "Rumblefoot",
            "Stonebridge", "Timberline", "Umbershade", "Verdantfield", "Whitethorn", "Xenonblade", "Yellowbank",
            "Zenithpeak", "Avalon", "Brackenwood", "Crosswind", "Deeproot", "Eaglecrest", "Firesong", "Galeforce",
            "Havenford", "Ironwill", "Jasperrock", "Kilncreek", "Longshadow", "Moonveil", "Northstar",
            "Orchardbloom", "Prairiegold", "Quillhaven", "Riverstone", "Sunbeam", "Tranquilmount", "Upland",
            "Violetvale", "Westbrook", "Expanse", "Yarrowfield", "Zincarrow", "Marbleglen", "Nimbusreach",
            "Obsidianfall", "Pilgrimway", "Questhaven", "Riftward", "Starwatch", "Tidemarsh", "Unity",
            "Vanguard", "Wraithwood", "Xystarch", "Yielding", "Zealot", "Abyssal", "Blightwood", "Crimson",
        ],
        "archetypes": [
            'Ranger', 'Druid', 'Scout', 'Hunter', 'Beastmaster', 'Protector', 
            'Wizard', 'Sorcerer', 'Arcanist', 'Scholar', 'Mage', 'Spellblade',
            'Guardian', 'Champion', 'Pride Leader', 'Sunwalker', 'Ancestral Speaker', 'Warrior',
            'Alchemist', 'Inventor', 'Philosopher', 'Mediator', 'Artificer', 'Tinkerer',
            'Paladin', 'Cleric', 'Priest', 'Acolyte', 'Zealot', 'Crusader',
            'Rogue', 'Thief', 'Assassin', 'Swashbuckler', 'Trickster', 'Shadow',
            'Barbarian', 'Berserker', 'Shaman', 'Warlord', 'Reaver', 'Skald',
            'Bard', 'Minstrel', 'Lorekeeper', 'Troubadour', 'Skald', 'Enchanter',
            'Monk', 'Mystic', 'Ascetic', 'Sensei', 'Shadow', 'Elementalist',
            'Fighter', 'Soldier', 'Gladiator', 'Knight', 'Mercenary', 'Tactician',
            'Warlock', 'Hexblade', 'Conjurer', 'Necromancer', 'Enchanter', 'Pact-maker',
            'Cleric', 'Healer', 'Oracle', 'Exorcist', 'Preacher', 'Missionary',
            'Sorcerer', 'Wild Mage', 'Dragon Disciple', 'Storm Sorcerer', 'Doombringer', 'Arcane Savant',
            'Necromancer', 'Bone Collector', 'Spiritualist', 'Death Mage', 'Lichdom Aspirant', 'Grave Warden',
            'Invoker', 'Theurge', 'Diviner', 'Seer', 'Augur', 'Prophet',
            'Assassin', 'Venomist', 'Silent Death', 'Shadow Stalker', 'Poison Master', 'Infiltrator',
            'Duelist', 'Fencer', 'Swordmaster', 'Blademaster', 'Martial Artist', 'Weapon Master',
            'Pirate', 'Buccaneer', 'Privateer', 'Corsair', 'Sea Dog', 'Raider',
            'Viking', 'Marauder', 'Sea King/Queen', 'Shieldmaiden', 'Explorer', 'Navigator',
            'Samurai', 'Ronin', 'Shogun', 'Daimyo', 'Kensei', 'Bushido Practitioner',
            'Ninja', 'Kunoichi', 'Spy', 'Saboteur', 'Scout', 'Shadow Warrior',
            'Cavalier', 'Chevalier', 'Lancer', 'Horseman', 'Destrier Rider', 'Knight Errant',
            'Summoner', 'Binder', 'Spirit Caller', 'Beastlord', 'Animist', 'Familiar Keeper',
            'Illusionist', 'Phantasmist', 'Mirage Weaver', 'Trickster', 'Visionary', 'Reality Bender',
            'Psion', 'Telepath', 'Mindbender', 'Psychic Warrior', 'Soulknife', 'Thoughtstealer',
            'Witch', 'Warlock', 'Occultist', 'Hexer', 'Curseweaver', 'Spellwitch',
            'Shapeshifter', 'Werebeast', 'Metamorph', 'Morphling', 'Changeling', 'Beastwalker',
            'Elementalist', 'Pyromancer', 'Hydromancer', 'Geomancer', 'Aeromancer', 'Thaumaturge',
            'Alchemist', 'Brewmaster', 'Apothecary', 'Chemist', 'Plague Doctor', 'Potioneer',
            'Bounty Hunter', 'Tracker', 'Sniper', 'Survivalist', 'Trapper', 'Reconnaissance',
            'Engineer', 'Mechanic', 'Machinist', 'Inventor', 'Sapper', 'Technologist',
            'Diplomat', 'Emissary', 'Ambassador', 'Chancellor', 'Consul', 'Envoy',
            'Merchant', 'Trader', 'Salesman', 'Broker', 'Dealer', 'Negotiator',
            'Scholar', 'Academic', 'Historian', 'Researcher', 'Librarian', 'Lecturer',
            'Farmer', 'Gardener', 'Agriculturist', 'Horticulturist', 'Rancher', 'Homesteader',
            'Artisan', 'Craftsman', 'Artificer', 'Artiste', 'Creator', 'Designer',
        ],
        "backgrounds": [
            'Acolyte', 'Anthropologist', 'Archaeologist', 'Charlatan', 'City Watch', 'Clan Crafter',
            'Cloistered Scholar', 'Courtier', 'Criminal', 'Entertainer', 'Faction Agent', 'Far Traveler',
            'Folk Hero', 'Gladiator', 'Guild Artisan', 'Guild Merchant', 'Haunted One', 'Hermit',
            'Inheritor', 'Investigator', 'Knight', 'Knight of the Order', 'Marine', 'Mercenary Veteran',
            'Noble', 'Outlander', 'Pirate', 'Sage', 'Sailor', 'Scholar', 'Shipwright', 'Smuggler',
            'Soldier', 'Spy', 'Urban Bounty Hunter', 'Urchin', 'Vizier', 'Waterdhavian Noble',
            'Grinner', 'Plaintiff', 'Rival Intern', 'Historian', 'Black Fist Double Agent',
            'Dragon Casualty', 'Iron Route Bandit', 'Phlan Refugee', 'Stojanow Prisoner', 'Ticklebelly Nomad',
            'Caravan Specialist', 'Earthspur Miner', 'Harborfolk', 'Mulmaster Aristocrat', 'Phlan Insurgent',
            'Trade Sheriff', 'Underdark Scout', 'Uthgardt Tribe Member', 'Waterdhavian Noble', 'Azorius Functionary',
            'Boros Legionnaire', 'Dimir Operative', 'Golgari Agent', 'Gruul Anarch', 'Izzet Engineer',
            'Orzhov Representative', 'Rakdos Cultist', 'Selesnya Initiate', 'Simic Scientist',
            'Candlekeep Scholar', 'Ravenloft Trinket Seller', 'Cormanthor Refugee', 'Gate Urchin',
            'Hillsfar Merchant', 'Hillsfar Smuggler', 'Secret Identity', 'Shade Fanatic', 'Trade Consortium Member',
            'Failed Merchant', 'Luskan Corsair', 'Neverwinter Urban Noble', 'Waterdeep Noble'
        ],
        "innate_abilities": ["Adaptability", "Versatility", "Skill Versatility", "Cultural Chameleon"],
        "preferred_classes": [
            'Artificer', 'Alchemist', 'Artillerist', 'Battle Smith',
            'Barbarian', 'Berserker', 'Totem Warrior', 'Ancestral Guardian', 'Storm Herald', 'Zealot',
            'Bard', 'Lore', 'Valor', 'Glamour', 'Whispers', 'Swords', 'Creation', 'Eloquence',
            'Cleric', 'Knowledge', 'Life', 'Light', 'Nature', 'Tempest', 'Trickery', 'War', 'Forge', 'Grave',
            'Druid', 'Land', 'Moon', 'Dreams', 'Shepherd', 'Spores', 'Stars', 'Wildfire',
            'Fighter', 'Champion', 'Battle Master', 'Eldritch Knight', 'Arcane Archer', 'Cavalier', 'Samurai', 'Psi Warrior', 'Rune Knight',
            'Monk', 'Open Hand', 'Shadow', 'Four Elements', 'Kensei', 'Sun Soul', 'Drunken Master', 'Mercy', 'Astral Self',
            'Paladin', 'Devotion', 'Ancients', 'Vengeance', 'Conquest', 'Redemption', 'Oathbreaker', 'Crown', 'Glory', 'Watchers',
            'Ranger', 'Hunter', 'Beast Master', 'Gloom Stalker', 'Horizon Walker', 'Monster Slayer', 'Fey Wanderer', 'Swarmkeeper',
            'Rogue', 'Thief', 'Assassin', 'Arcane Trickster', 'Swashbuckler', 'Mastermind', 'Inquisitive', 'Scout', 'Phantom', 'Soulknife',
            'Sorcerer', 'Draconic', 'Wild Magic', 'Divine Soul', 'Shadow', 'Storm', 'Aberrant Mind', 'Clockwork Soul',
            'Warlock', 'Archfey', 'Fiend', 'Great Old One', 'Celestial', 'Hexblade', 'Fathomless', 'Genie', 'Undead',
            'Wizard', 'Abjuration', 'Conjuration', 'Divination', 'Enchantment', 'Evocation', 'Illusion', 'Necromancy', 'Transmutation', 'Bladesinging', 'War Magic', 'Chronurgy', 'Graviturgy'
        ],
        "culture": "Humans are found in all corners of the world, from the mightiest empires to the smallest rural communities. They build vast cities and monumental architectures, explore distant lands, and shape the world with their innovations and conflicts. Human societies are incredibly varied, with cultures that celebrate a spectrum of traditions, beliefs, and values.",
        "lore": "Humans are the most adaptable and ambitious people among the common races. They have varied tastes, morals, and customs in the many different lands where they have settled. When they settle, though, they stay: they build cities to last for the ages, and great kingdoms that can persist for long centuries. An individual human might have a relatively short life span, but a human nation or culture preserves traditions with origins far beyond the reach of any single human's memory. They are innovators and pioneers who push the boundaries of what is possible, driven by a restless urge to explore and achieve mastery in various disciplines.",
        "alignment": [
            "Lawful Good", "Neutral Good", "Chaotic Good",
            "Lawful Neutral", "True Neutral", "Chaotic Neutral",
            "Lawful Evil", "Neutral Evil", "Chaotic Evil"
        ],
        "physical_characteristics": {
            "Male": {"height": (160, 200), "weight": (70, 100)},
            "Female": {"height": (150, 190), "weight": (50, 80)}
        },
        "male_names": [
            "Alaric", "Borin", "Cedric", "Derek", "Eldon", "Falken", "Garrett", "Halden", "Ivar", "Jorin",
            "Kendrick", "Lorin", "Merek", "Nevin", "Orrin", "Perrin", "Quintus", "Roric", "Soren", "Tyrus",
            "Ulric", "Varin", "Walden", "Xander", "Yorin", "Zane", "Aedan", "Bryce", "Cael", "Davin",
            "Egan", "Flynn", "Galen", "Hadrian", "Ian", "Jasper", "Keiran", "Leon", "Miles", "Nolan",
            "Owen", "Paxton", "Quinn", "Rowan", "Seth", "Tristan", "Uri", "Vincent", "Wyatt", "Xavier", "Yale", "Zachary",
            "Aaron", "Benedict", "Charles", "David", "Edward", "Franklin", "George", "Henry", "Isaac", "James",
            "Kevin", "Liam", "Michael", "Nathan", "Oliver", "Patrick", "Quentin", "Robert", "Steven", "Thomas",
            "Ulysses", "Victor", "William", "Yosef", "Zachary", "Arthur", "Brian", "Caleb", "Daniel",
            "Elijah", "Felix", "Gabriel", "Harold", "Ian", "John", "Kyle", "Louis", "Mason", "Noah", "Oscar",
            "Paul", "Quincy", "Ryan", "Sean", "Tyler", "Uriah", "Wesley", "Xander", "Yuri", "Zane"
        ],
        "female_names": [
            "Alyssa", "Brielle", "Cara", "Dara", "Elena", "Fiona", "Giselle", "Hanna", "Isla", "Jenna",
            "Kara", "Lena", "Mira", "Nora", "Ophelia", "Pia", "Quinn", "Rosa", "Sara", "Tia", "Una",
            "Vera", "Willa", "Xenia", "Ysabel", "Zara", "Ada", "Bella", "Celia", "Diana", "Eva", "Flora",
            "Grace", "Helena", "Ida", "Julia", "Kyla", "Lora", "Maya", "Nina", "Olivia", "Petra", "Ruby",
            "Selena", "Tanya", "Uma", "Vivian", "Wendy", "Xyla", "Yvette", "Zoey","Abigail", "Bethany", 
            "Catherine", "Diana", "Eleanor", "Fiona", "Grace", "Hannah", "Isabel", "Jessica",
            "Katherine", "Laura", "Megan", "Natalie", "Olivia", "Penelope", "Quinn", "Rachel", "Sarah", "Tiffany",
            "Ursula", "Vanessa", "Wendy", "Xena", "Yasmine", "Zoe", "Alice", "Brianna", "Claire", "Danielle",
            "Emily", "Faith", "Gabrielle", "Heather", "Ivy", "Jennifer", "Kristen", "Lily", "Madison", "Nicole",
            "Octavia", "Paige", "Riley", "Sophie", "Tracy", "Uma", "Violet", "Whitney", "Xiomara", "Yolanda", "Zelda"
        ]
    },
    "Air Genasi": {
        "last_names": [
            "Cloudleaper", "Winddancer", "Skysong", "Breezefellow", "Stormvoyager", "Zephyrsong",
            "Gustborne", "Airstream", "Skywhisper", "Draftslider", "Windsworn", "Tempestsail",
            "Etherwalker", "Mistwanderer", "Galeforce", "Airheart", "Skyshaper", "Cloudsurfer",
            "Aetherdrift", "Windswept", "Stormwielder", "Heavensent", "Breezeshaper", "Skydrifter"
        ],
        "archetypes": ["Windwalker", "Skywatcher", "Stormcaller", "Elemental Envoy", "Aerialist", "Cloudspeaker"],
        "backgrounds": ["Explorer", "Hermit", "Pilgrim", "Outlander", "Sailor", "Messenger", "Elemental Adept"],
        "innate_abilities": ["Unending Breath", "Mingle with the Wind (Levitate)", "Air Affinity","Unending Breath", "Levitate", "Mingle with the Wind", "Air Mastery", "Gust of Wind"],
        "preferred_classes": ["Sorcerer", "Wizard", "Rogue", "Monk", "Druid", "Sorcerer", ],
        "culture": "Air Genasi culture is often characterized by a love for freedom and discovery. They tend to be wanderers and adventurers at heart, drawn to the exploration of new lands and the uncovering of ancient secrets.",
        "lore": "Air Genasi are born of the air element, often displaying traits like a sense of freedom, a love for exploration, and a natural affinity for magic that manipulates air and wind.",
        "alignment": [
            "True Neutral", 
            "Chaotic Neutral",
            "Neutral Good", "Neutral Evil", 
            "Lawful Neutral", "Chaotic Good", "Chaotic Evil" 
        ],
        "physical_characteristics": {
            "Male": {"height": (170, 195), "weight": (60, 85)},
            "Female": {"height": (165, 190), "weight": (55, 80)}
        }, 
        "male_names": [
                "Zephyr", "Gale", "Cielo", "Aero", "Breeze", "Cyclone", "Skye", "Strato", "Vento", "Whirl",
                "Blast", "Gust", "Jet", "Mistral", "Squall", "Tempest", "Vapor", "Windar", "Zephyros", "Aither",
                "Altus", "Boreas", "Corus", "Dew", "Eurus", "Fohn", "Gustav", "Horus", "Ion", "Jetstream",
                "Kaze", "Levante", "Monsoon", "Notus", "Oris", "Pavan", "Quilo", "Ramus", "Simoom", "Thermal",
                "Umbriel", "Volant", "Wester", "Xephyr", "Yonder", "Zalor", "Aeolus", "Brontes", "Cirrus", "Dors",
                "Eolo", "Flurry", "Ghibli", "Haboob", "Ith", "Jubal", "Kean", "Largo", "Mist", "Nimbus", "Oriel",
                "Puff", "Quintus", "Ridge", "Storm", "Turbine", "Uranus", "Vayun", "Wisp", "Xenon", "Yawl", "Zonda"
            ],
        "female_names": [
                "Aria", "Aurora", "Azure", "Brisa", "Ciel", "Era", "Fay", "Luna", "Nimbus", "Sirocco",
                "Sky", "Solara", "Tornado", "Twila", "Vayu", "Winda", "Zéphyr", "Halo", "Nebula", "Seraphine",
                "Aella", "Breezy", "Cirra", "Dawn", "Echo", "Frost", "Glimmer", "Haze", "Iris", "Jewel",
                "Kelda", "Lumin", "Mistral", "Nova", "Opal", "Pearl", "Quila", "Raine", "Sylph", "Talia",
                "Umbra", "Vesper", "Whisper", "Xanthe", "Yara", "Zephyra", "Alize", "Blaze", "Cloud", "Droplet",
                "Emberly", "Foehn", "Gale", "Halo", "Isla", "Jade", "Kiara", "Lael", "Maelstrom", "Nephele",
                "Oceana", "Polaris", "Quorra", "Raina", "Stella", "Tempest", "Unity", "Violet", "Willow",
                "Xylia", "Yasmin", "Zora"
            ]
    },
    "Dragonborn": {
        "last_names": [
            "Flameborn", "Stormbreath", "Ironscale", "Skyrider", "Frostfang", "Goldcrest", "Emberfall",
            "Windstrike", "Shadowflame", "Brightspear", "Thunderhorn", "Crimsonwing", "Azurehide",
            "Sunscaler", "Nightbellow", "Stoneclaw", "Fireheart", "Galewing", "Earthshaker", "Seabringer",
            "Rimecast", "Darktalon", "Lightbringer", "Stormcaller", "Deeproar"
        ],
        "archetypes": ["Champion", "Guardian", "Emissary", "Warrior", "Spellcaster", "Mercenary", "Paladin", "Sorcerer"],
        "backgrounds": ["Soldier", "Noble", "Explorer", "Mercenary", "Scholar", "Knight", "Sage", "Acolyte"],
        "innate_abilities": ["Draconic Ancestry", "Breath Weapon", "Damage Resistance", "Draconic Majesty"],
        "preferred_classes": ["Paladin", "Fighter", "Sorcerer", "Barbarian", "Cleric"],
        "culture": "Dragonborn culture is centered around clan and family. They have a profound sense of honor and duty, often aspiring to live up to the ideals of their draconic ancestors. Dragonborn societies are structured, with a strong emphasis on martial prowess and magical ability.",
        "lore": "Dragonborn are proud and noble, with a strong sense of honor and duty. They are often seen as aloof and intimidating, but those who earn their trust and respect will find them to be loyal and steadfast allies. Dragonborn, with their draconic heritage, are a proud and honorable race, often embodying the fearsome traits of dragons. Their culture highly values honor, clan loyalty, and excellence in battle. Dragonborn are naturally inclined towards classes that allow them to harness their innate draconic power, such as Paladins and Sorcerers, and they often find themselves in roles where they can lead or protect others. ",
        "alignment": [
            "Lawful Good",
            "Neutral Good",
            "Lawful Neutral"
        ],
        "physical_characteristics": {
            "Male": {"height": (180, 220), "weight": (90, 120)},
            "Female": {"height": (175, 215), "weight": (80, 110)}
        }, 
        "male_names": [
                "Arjhan", "Balasar", "Bharash", "Donaar", "Ghesh", "Heskan", "Kriv", "Medrash", "Mehen", "Nadarr",
                "Pandjed", "Patrin", "Rhogar", "Shamash", "Tarhun", "Torinn", "Zarkhil", "Sulvar", "Vrakthos", "Zovem",
                "Axtur", "Creth", "Draxan", "Ember", "Falkrin", "Grex", "Irxan", "Jax", "Korth", "Larn",
                "Morx", "Norix", "Othrel", "Pyxrin", "Queth", "Rax", "Saxton", "Thurkear", "Ulvir", "Vex",
                "Wyrx", "Xarx", "Yarx", "Zeth", "Axar", "Berth", "Fyrn", "Garn", "Hex", "Jurn", "Kyrox",
                "Lorx", "Marth", "Nyr", "Orin", "Prax", "Qyxn", "Ryst", "Syth", "Tyrox", "Urth", "Vyr",
                "Wrax", "Xyrn", "Yurx", "Zorx"
            ],
        "female_names": [
                "Akra", "Biri", "Daar", "Farideh", "Harann", "Flavilar", "Jheri", "Kava", "Korinn", "Mishann",
                "Nala", "Perra", "Raiann", "Sora", "Surina", "Thava", "Uadjit", "Vezera", "Yrjix", "Zofia",
                "Alyth", "Bryx", "Cynth", "Draxa", "Elyx", "Fyra", "Gyra", "Hyra", "Ixen", "Jyx",
                "Kyra", "Lyssa", "Myx", "Nyssa", "Oxara", "Pyra", "Qyra", "Ryssa", "Syra", "Tyra",
                "Uxia", "Vyra", "Wyn", "Xyra", "Yxara", "Zyra", "Arix", "Brissa", "Cyra", "Dyra",
                "Exa", "Frix", "Graxa", "Hyrax", "Iyra", "Jyra", "Kyrx", "Lyra", "Myra", "Nix",
                "Oryx", "Prissa", "Qyx", "Rixa", "Syrx", "Tyx", "Uxara", "Vix", "Wyrx", "Xixa",
                "Yurix", "Zyx"
            ]
    },
    "Gnome": {
        "last_names": [
            "Quickwhistle", "Fizzlebang", "Lightspark", "Wondergleam", "Bizzibod", "Glimmerflick",
            "Puddlestamp", "Rindlebock", "Dabblebox", "Glittergauge", "Fidgetbeam", "Whizzlestick",
            "Banglebuck", "Gizmoblink", "Twizzlefizz", "Bubblebouncer", "Clocktwist", "Beamhitch",
            "Gadgetglim", "Sparklethorn"
        ],
        "archetypes": ["Inventor", "Alchemist", "Tinker", "Wizard", "Illusionist", "Artisan", "Scholar"],
        "backgrounds": ["Artisan", "Hermit", "Guild Artisan", "Tinker", "Merchant", "Sage", "Explorer"],
        "innate_abilities": ["Darkvision", "Gnome Cunning", "Artificer's Lore", "Tinker"],
        "preferred_classes": ["Wizard", "Rogue", "Artificer", "Bard"],
        "culture": "Gnomes thrive in communities where innovation and curiosity are celebrated. They have an insatiable appetite for learning, often dedicating their lives to the mastery of their crafts or the unraveling of the world's mysteries.",
        "lore": "Gnomes are renowned for their inventiveness, curiosity, and affinity for magic, particularly within the realms of illusion and artifice. Their society is often characterized by a deep love for creating, learning, and exploring the mechanisms of the world around them. Gnomes make excellent Wizards and Rogues, with a special penchant for trickery, craftsmanship, and intellectual pursuits.",
        "alignment": [
            "Neutral Good",
            "Lawful Good",
            "True Neutral",
            "Chaotic Good",
            "Lawful Neutral"
        ],
        "physical_characteristics": {
            "Male": {"height": (90, 120), "weight": (40, 45)},
            "Female": {"height": (85, 115), "weight": (35, 40)}
        },
        "male_names": [
            "Alston", "Boddynock", "Brocc", "Burgell", "Dimble", "Eldon", "Fonkin", "Gimble", "Glim", "Jebeddo",
            "Kellen", "Namfoodle", "Orryn", "Roondar", "Seebo", "Sindri", "Warryn", "Wrenn", "Zook", "Fibblestib",
            "Bilbin", "Fenthwick", "Lorim", "Quill", "Rilkin", "Tilver", "Nim", "Orin", "Pip", "Rondo",
            "Ardoc", "Balabar", "Clewin", "Daergel", "Eberdeb", "Fablen", "Glaric", "Herble", "Ivron", "Jasper",
            "Kib", "Lorbac", "Morwen", "Nackle", "Ozif", "Pervin", "Quobin", "Rondic", "Swerf", "Toblen",
            "Ulmar", "Varnic", "Welber", "Xoblo", "Yeben", "Zeffon", "Ailmar", "Bink", "Corvin", "Dapifer"
        ],
        "female_names": [
            "Bimpnottin", "Breena", "Caramip", "Carlin", "Donella", "Duvamil", "Ella", "Ellyjobell", "Ellywick", "Lilli",
            "Loopmottin", "Mardnab", "Nissa", "Nyx", "Oda", "Orla", "Roywyn", "Shamil", "Tana", "Waywocket",
            "Alyda", "Bitty", "Curla", "Drusila", "Euphemia", "Frix", "Gwenna", "Hesper", "Isel", "Jinx",
            "Kizzy", "Lobelia", "Mimsy", "Nixi", "Oli", "Piper", "Quilla", "Rixi", "Sipsi", "Topsy",
            "Ulla", "Vexi", "Wixie", "Xeni", "Yola", "Zolli", "Amble", "Bex", "Cixi", "Dexi", "Froxi",
        ]
    },
    "Forest Gnome": {
        "last_names": [
            "Leafwhisper", "Berrypicker", "Dewdrop", "Mosscover", "Branchtwist", "Thicketfound",
            "Bloomhollow", "Fernshroud", "Petalwind", "Greenmeadow", "Brightbark", "Woodhew",
            "Streamdance", "Grasshopper", "Sunbeam", "Wildbloom", "Treehug", "Vineleaper",
            "Brambleheart", "Dappleleaf"
        ],
        "archetypes": ["Trickster", "Ranger", "Scout", "Druid", "Illusionist", "Beast Friend"],
        "backgrounds": ["Hermit", "Outlander", "Guide", "Folk Hero", "Artisan", "Explorer"],
        "innate_abilities": ["Natural Illusionist", "Speak with Small Beasts", "Darkvision", "Gnome Cunning"],
        "preferred_classes": ["Ranger", "Druid", "Wizard (Illusionist)", "Rogue"],
        "culture": "Forest Gnomes live in seclusion, hidden among the foliage of dense forests where they form tight-knit communities. They have a deep connection with nature, living in harmony with the forest and its creatures. Forest Gnomes are known for their playfulness, curiosity, and knack for illusion and stealth, helping them evade detection.",
        "alignment": [
            "Neutral Good",
            "Chaotic Good",
            "True Neutral",
            "Lawful Good"
        ],
        "lore": "Despite their reclusive nature, Forest Gnomes possess a deep-seated curiosity that drives them to explore the world beyond their woodland homes. Their innate magic allows them to cast illusions and communicate with animals, reflecting their strong bond with nature.",
        "physical_characteristics": {
            "Male": {"height": (90, 105), "weight": (35, 40)},
            "Female": {"height": (85, 100), "weight": (30, 35)}
        },
        "male_names": [
            "Bilbin", "Fenthwick", "Lorim", "Quill", "Rilkin", "Tilver", "Zook", "Nim", "Orin", "Pip",
            "Rondo", "Sindri", "Warryn", "Eldon", "Fibblestib", "Kellen", "Namfoodle", "Orryn", "Roondar", "Seebo",
            "Alston", "Boddynock", "Brocc", "Burgell", "Dimble", "Eldon", "Fonkin", "Gimble", "Glim", "Jebeddo",
            "Diblen", "Folwin", "Harbin", "Jinlop", "Kerbin", "Melnis", "Norbo", "Pog", "Quilfen", "Rigdo",
            "Silnan", "Thamli", "Uldwin", "Venbo", "Wilben", "Xalwin", "Yebin", "Zilnor", "Adbin", "Bilnor"
        ],
        "female_names": [
            "Bimpnottin", "Caramip", "Duvamil", "Ellywick", "Lilli", "Loopmottin", "Mardnab", "Nissa", "Nyxbis", "Oda",
            "Orla", "Roywyn", "Shamil", "Tana", "Waywocket", "Zanna", "Breena", "Carlin", "Donella", "Doralia",
            "Alys", "Bryn", "Cessily", "Drusa", "Euphemia", "Fenna", "Gilly", "Hesper", "Isolde", "Jovie",
            "Almira", "Bilsi", "Celwinn", "Delphi", "Eryn", "Faelie", "Gilsi", "Hinfi", "Illiwick", "Jilsi",
            "Kelni", "Lorfi", "Melri", "Nilsi", "Pilni", "Quilri", "Rinfi", "Silmi", "Tilsi", "Vilni"
        ]
    },
    "Rock Gnome": {
        "last_names": [
            "Tinkerfoot", "Cogspinner", "Boltwhistle", "Gearloose", "Pebblecraft", "Sprocketshank",
            "Clankforged", "Brassblast", "Stonegear", "Ironclamp", "Widgetwrench", "Gadgetfizzle",
            "Sparkshifter", "Coilbender", "Springgrind", "Flintspark", "Steelwidget", "Bronzecog",
            "Coppercoil", "Silvergear"
        ],
        "archetypes": ["Engineer", "Inventor", "Tinker", "Alchemist", "Artisan", "Scholar"],
        "backgrounds": ["Guild Artisan", "Tinker", "Merchant", "Sage", "Artisan", "Explorer"],
        "innate_abilities": ["Artificer's Lore", "Tinker", "Darkvision", "Gnome Cunning"],
        "preferred_classes": ["Artificer", "Wizard", "Rogue", "Fighter"],
        "culture": "Rock Gnomes are ingenious inventors and craftsmen, residing in bustling communities where innovation and creativity are highly valued. Their society is driven by the pursuit of knowledge, with each gnome dedicating their life to mastering a particular craft or area of study. Rock Gnomes are recognized for their contributions to the fields of engineering, alchemy, and arcane research.",
        "alignment": [
            "Lawful Good", 
            "Neutral Good",
            "Lawful Neutral"
        ],
        "lore": "Rock Gnomes have a natural propensity for invention and discovery, often leading them to become renowned inventors, engineers, and scholars. Their creations range from practical tools to wondrous mechanical gadgets that defy imagination.",
        "physical_characteristics": {
            "Male": {"height": (95, 110), "weight": (40, 45)},
            "Female": {"height": (90, 105), "weight": (35, 40)}
        },
        "male_names": [
            "Bilbin", "Fenthwick", "Lorim", "Quill", "Rilkin", "Tilver", "Zook", "Nim", "Orin", "Pip",
            "Rondo", "Sindri", "Warryn", "Eldon", "Fibblestib", "Kellen", "Namfoodle", "Orryn", "Roondar", "Seebo",
            "Alston", "Boddynock", "Brocc", "Burgell", "Dimble", "Eldon", "Fonkin", "Gimble", "Glim", "Jebeddo",
            "Alston", "Boddynock", "Brocc", "Drusus", "Erdan", "Falken", "Garret", "Hewitt", "Ivron", "Jax",
            "Kelvin", "Ludwig", "Milo", "Nebin", "Osborn", "Peff", "Quildor", "Rupert", "Sago", "Toblen",
            "Ulmo", "Vincent", "Wilbur", "Xalvador", "Yorrick", "Zephyr"
        ],
        "female_names": [
            "Bimpnottin", "Caramip", "Duvamil", "Ellywick", "Lilli", "Loopmottin", "Mardnab", "Nissa", "Nyxbis", "Oda",
            "Orla", "Roywyn", "Shamil", "Tana", "Waywocket", "Zanna", "Breena", "Carlin", "Donella", "Doralia",
            "Alys", "Bryn", "Cessily", "Drusa", "Euphemia", "Fenna", "Gilly", "Hesper", "Isolde", "Jovie",
            "Kelda", "Lorna", "Miri", "Nyx", "Olwin", "Paela", "Quilla", "Rosalind", "Sapphira", "Thimble",
            "Ula", "Vesper", "Wendelyn", "Xanthe", "Yelena", "Zol"
        ]
    },
    "Deep Gnome (Svirfneblin)": {
        "last_names": [
            "Understone", "Darkweave", "Gritshard", "Tunneler", "Lowvault", "Dimfinder",
            "Shadepool", "Silentfoot", "Nightrunner", "Earthblend", "Rockvein", "Deepdelver",
            "Shadowgem", "Gloomwalker", "Stoneknack", "Cavegloom", "Mudgrasp", "Ironhew",
            "Nightgranite", "Sootbeard"
        ],
        "archetypes": ["Illusionist", "Rogue", "Alchemist", "Tinker"],
        "backgrounds": ["Miner", "Artisan", "Outcast", "Spy", "Underdark Guide"],
        "innate_abilities": ["Superior Darkvision", "Gnome Cunning", "Stone Camouflage", "Svirfneblin Magic"],
        "preferred_classes": ["Rogue", "Wizard (Illusionist)", "Artificer"],
        "culture": "Deep Gnomes, or Svirfneblin, live in the Underdark, a place of danger and mystery. Their societies are well-hidden and heavily fortified, reflecting their constant vigilance against threats. Svirfneblin are known for their stoicism, hardiness, and exceptional ability to survive in the hostile environment of the Underdark.",
        "alignment": [
            "True Neutral",
            "Lawful Neutral",
            "Neutral Evil"
        ],
        "lore": "Unlike their surface-dwelling kin, Deep Gnomes have adapted to life in the Underdark, developing unique abilities that help them avoid detection and defend against the dangers that lurk in the dark.",
        "physical_characteristics": {
            "Male": {"height": (90, 105), "weight": (35, 45)},
            "Female": {"height": (85, 100), "weight": (30, 40)}
        },
        "male_names": [
            "Belwar", "Brickers", "Dankil", "Flint", "Krieger", "Kroop", "Quarrel", "Rathek", "Schnick", "Thrack",
            "Whurbin", "Bilnur", "Dalk", "Firble", "Glynn", "Kasek", "Nackle", "Murnig", "Pingun", "Renn", 
            "Alaric", "Bram", "Corin", "Drake", "Egon", "Falk", "Grom", "Haldor", "Ivar", "Jorn", "Loki",
            "Gimlen", "Narnor", "Skorf", "Veldin", "Zanik", "Gurnik", "Harbek", "Jasper", "Lemmy", "Norbo",
            "Orber", "Parns", "Quintik", "Rond", "Salmorn", "Tibor", "Umbod", "Voric", "Wrenn", "Xank"
        ],
        "female_names": [
            "Bilra", "Dagma", "Elizzib", "Fricknarti", "Helja", "Kriista", "Lurna", "Murneth", "Nalvyna", "Orla",
            "Schnella", "Triggvy", "Ulla", "Velra", "Welvy", "Zilka", "Breen", "Dini", "Gren", "Lini",
            "Astrid", "Brenna", "Cindra", "Dagmar", "Eir", "Freja", "Gilda", "Hedda", "Inga", "Jora",
            "Anni", "Berenn", "Curna", "Delpi", "Ermin", "Fili", "Glyndi", "Henni", "Ivina", "Jenniver",
            "Kilma", "Lempi", "Mindi", "Nys", "Ophi", "Pryn", "Quilla", "Renni", "Silli", "Tynni", "Uvi", "Venni", "Winni", "Xyli", "Yanni", "Zenni"
        ]
    },
    "Hill Dwarf": {
        "last_names": [
            "Barleybrew", "Earthwander", "Meadmaker", "Amberstone", "Caskbelly", "Wheatbeard",
            "Gentlehollow", "Softforge", "Mossfoot", "Greenfield", "Aleheart", "Brewbeard",
            "Mudfoot", "Grasscloak", "Leafbeard", "Sunshadow", "Hillheart", "Valewarden",
            "Streamwatcher", "Ferngully"
        ],
        "archetypes": ["Cleric", "Brewmaster", "Warrior", "Merchant"],
        "backgrounds": ["Guild Artisan", "Soldier", "Hermit", "Brewer", "Healer"],
        "innate_abilities": ["Darkvision", "Dwarven Resilience", "Dwarven Toughness", "Tool Proficiency", "Stonecunning"],
        "preferred_classes": ["Cleric", "Fighter", "Paladin"],
        "culture": "Hill Dwarves are known for their craftsmanship and connection to the land. Living in hillside strongholds and mining communities, they are skilled artisans, particularly in brewing and metalwork. Their societies are clan-based, with a strong emphasis on family, tradition, and the defense of their homes against any threats.",
        "alignment":  [
            "Lawful Good",
            "Neutral Good",
            "Lawful Neutral"
        ],
        "lore": "Hill Dwarves have a long history of coexistence with the surface lands, often trading with neighboring races and offering their crafted goods. Their resilience and hardiness allow them to thrive in environments others might find inhospitable.",
        "physical_characteristics": {
            "Male": {"height": (115, 135), "weight": (50, 75)},
            "Female": {"height": (110, 130), "weight": (40, 65)}
        },
        "male_names": [
            "Adrik", "Balin", "Dain", "Darrak", "Delg", "Eberk", "Flint", "Gardain", "Harbek", "Kildrak",
            "Morgran", "Orsik", "Oskar", "Rangrim", "Rurik", "Taklinn", "Thoradin", "Thorin", "Vondal", "Whurbin",
            "Bilnur", "Dalk", "Firble", "Glynn", "Kasek", "Nackle", "Murnig", "Pingun", "Renn","Alaric", "Bram", "Corin", "Drake", "Egon", "Falk", "Grom", "Haldor", "Ivar", "Jorn",
            "Loki", "Magnar", "Njal", "Ove", "Pjotr", "Quarrel", "Roar", "Sigurd", "Trygve", "Ulf",
            "Vidar", "Wilf", "Xarles", "Yngvar", "Zak"

        ],
        "female_names": [
            "Amber", "Artin", "Audhild", "Bardryn", "Dagnal", "Diesa", "Eldeth", "Falkrunn", "Finellen", "Gunnloda",
            "Gurdis", "Helja", "Hlin", "Kathra", "Kristryd", "Ilde", "Liftrasa", "Mardred", "Riswynn", "Sannl",
            "Torbera", "Torgga", "Vistra", "Breen", "Dini", "Gren", "Lini","Astrid", "Brenna", "Cindra", "Dagmar", "Eir", "Freja", "Gilda", "Hedda", "Inga", "Jora",
            "Kelda", "Lena", "Morna", "Nessa", "Oda", "Pia", "Runa", "Sif", "Tove", "Ursa",
            "Viveka", "Wenche", "Ylva", "Zelda"
        ]
    },
    "Mountain Dwarf": {
        "last_names": [
            "Ironfist", "Steelhammer", "Hardforge", "Anvilbrow", "Rockhearth", "Deepdelve",
            "Goldvein", "Silveraxe", "Stoneshield", "Thunderforge", "Orebeard", "Forgefire",
            "Boulderback", "Mountainpeak", "Granitegrip", "Ironheart", "Mithrilarm", "Coalbraid",
            "Rubyeye", "Sapphirefist"
        ],
        "archetypes": ["Blacksmith", "Warrior", "Guard", "Explorer"],
        "backgrounds": ["Soldier", "Smith", "Mercenary", "Mountain Guide", "Craftsman"],
        "innate_abilities": ["Darkvision", "Dwarven Resilience", "Dwarven Armor Training", "Tool Proficiency", "Stonecunning"],
        "preferred_classes": ["Fighter", "Paladin", "Barbarian"],
        "culture": "Mountain Dwarves reside in vast underground fortresses carved from the heart of mountains. They are unmatched smiths and warriors, priding themselves on their martial traditions and the crafting of legendary weapons and armor. Their societies are built on the principles of honor, craftsmanship, and the defense of their ancient halls from any intruders.",
        "alignment": [
            "Lawful Good",
            "Lawful Neutral",
            "Neutral Good"
        ],
        "lore": "Mountain Dwarves have storied histories of battles fought to protect their homelands from dragons, giants, and other threats. Their enduring legacy is one of resilience, valor, and the mastery of the forge.",
        "physical_characteristics": {
            "Male": {"height": (120, 140), "weight": (55, 80)},
            "Female": {"height": (115, 135), "weight": (45, 70)}
        },
         "male_names": [
            "Adrik", "Baern", "Barendd", "Brottor", "Bruenor", "Dain", "Darrak", "Delg", "Eberk", "Einkil",
            "Fargrim", "Flint", "Gardain", "Harbek", "Kildrak", "Morgran", "Orsik", "Oskar", "Rangrim", "Rurik",
            "Taklinn", "Thoradin", "Thorin", "Tordek", "Traubon", "Ulfgar", "Veit", "Vondal", "Whurbin", "Bilnur",
            "Dalk", "Firble", "Glynn", "Kasek", "Nackle", "Murnig", "Pingun","Gorunn", "Hakar", "Igmund", "Jorunn", "Krorin", "Lunnar", "Magnar", "Narvi", "Oinar", "Parn",
            "Quarar", "Rondar", "Sindri", "Thrain", "Ulfar", "Vidar", "Wolvar", "Yngvi", "Zorn", "Arngrim"
        ],
        "female_names": [
            "Amber", "Artin", "Audhild", "Bardryn", "Dagnal", "Diesa", "Eldeth", "Falkrunn", "Finellen", "Gunnloda",
            "Gurdis", "Helja", "Hlin", "Kathra", "Kristryd", "Ilde", "Liftrasa", "Mardred", "Riswynn", "Sannl",
            "Torbera", "Torgga", "Vistra", "Breen", "Dini", "Gren", "Lini","Brynja", "Dahlia", "Erika", "Frida", "Gerta", "Heidrun", "Ingrid", "Jordis", "Kara", "Lisbet",
            "Norna", "Ormhild", "Petrina", "Runa", "Sigrid", "Thora", "Unn", "Valka", "Wilma", "Yrsa"
        ]
    },
    "Halfling": {
        "last_names": [
            "Longsocks", "Pottershine", "Meadowbrook", "Goldfound", "Trueword", "Bramblethorn",
            "Elderberry", "Heartykettle", "Goodbarrel", "Bushgather", "Proudfoot", "Quickstep",
            "Softsong", "Brightcheek", "Farwalker", "Leafshade", "Dawnriver", "Brookstone",
            "Merryweather", "Peppergrain"
        ],
        "archetypes": ["Thief", "Farmer", "Bard", "Adventurer"],
        "backgrounds": ["Folk Hero", "Acrobat", "Burglar", "Innkeeper", "Merchant"],
        "innate_abilities": ["Lucky", "Brave", "Halfling Nimbleness", "Naturally Stealthy"],
        "preferred_classes": ["Rogue", "Bard", "Ranger", "Fighter"],
        "culture": "Halflings are known for their resourceful, resilient nature, and a strong sense of community. They prefer peaceful, bucolic lives in rural areas or small towns, where everyone knows each other. Halfling society is built on principles of mutual aid, hospitality, and the sharing of comforts.",
        "alignment": [
            "Lawful Good",
            "Neutral Good",
            "Lawful Neutral"
        ],
        "lore": "Halflings are small, often no taller than 3 feet, but what they lack in size, they make up for in courage and determination. They are adept at living under the radar of the larger races, often seen as mere folk of legend.",
        "physical_characteristics": {
            "Male": {"height": (90, 110), "weight": (30, 40)},
            "Female": {"height": (85, 105), "weight": (25, 35)}
        },
        "male_names": [
            "Alton", "Ander", "Cade", "Corrin", "Eldon", "Errich", "Finnan", "Garret", "Lindal", "Lyle",
            "Merric", "Milo", "Osborn", "Perrin", "Reed", "Roscoe", "Wellby", "Wendel", "Wenner", "Wes",
            "Aiden", "Bryce", "Cael", "Davin", "Egan", "Flynn", "Galen", "Hadrian", "Ian", "Jasper",
            "Bramwell", "Cotman", "Dodd", "Elian", "Ferdinand", "Geoff", "Henrick", "Ivor", "Jarrett", "Kelvin",
            "Lem", "Matthias", "Norris", "Otto", "Palmer", "Quincy", "Rupert", "Silas", "Tobias", "Vincent",
            "Wilbur", "Xander", "Yardley", "Zed"
        ],
        "female_names": [
            "Ama", "Bree", "Callie", "Cora", "Euphemia", "Jillian", "Kithri", "Lavinia", "Lidda", "Maegan",
            "Marigold", "Merla", "Myria", "Nedda", "Paela", "Portia", "Seraphina", "Shaena", "Trym", "Vani",
            "Verna", "Breen", "Dini", "Gren", "Lini","Althea", "Bonny", "Celeste", "Daisy", "Emeline", "Faye", "Greta", "Hazel", "Iris", "Jasmine",
            "Keeley", "Leona", "Mina", "Nellie", "Olive", "Piper", "Quinn", "Ruby", "Sophie", "Tansy",
            "Una", "Violet", "Willow", "Xeni", "Yolanda", "Zoe"
        ]
    },
    "Lightfoot Halfling": {
        "last_names": [
            "Quickfoot", "Silverbuckle", "Greenbottle", "Thistletop", "Barrelrider", "Underhill",
            "Tosscobble", "Brushgather", "Nimblefingers", "Leafrunner", "Smoothhands", "Brightpath",
            "Slyboot", "Swiftwhistle", "Tealeaf", "Appleblossom", "Fairgarden", "Honeyfoot",
            "Puddlejump", "Riverskip"
        ],
        "archetypes": ["Thief", "Bard", "Trickster", "Adventurer", "Scout", "Wanderer"],
        "backgrounds": ["Charlatan", "Entertainer", "Rogue", "Merchant", "Traveler", "Burglar"],
        "innate_abilities": ["Naturally Stealthy", "Lucky", "Brave", "Halfling Nimbleness"],
        "preferred_classes": ["Rogue", "Bard", "Cleric", "Sorcerer"],
        "culture": "Lightfoot Halflings are the most prone to wanderlust of their kind, often found exploring the world beyond their homes. They cherish freedom, diversity, and the thrill of discovery, easily blending into other societies.",
        "alignment": [
            "Chaotic Good",
            "Neutral Good",
            "Chaotic Neutral"
        ],
        "lore": "Thanks to their innate stealth and agility, Lightfoot Halflings excel in avoiding danger and finding their way out of trouble. Their curious and sociable nature often leads them into unexpected adventures.",
        "physical_characteristics": {
            "Male": {"height": (88, 108), "weight": (28, 38)},
            "Female": {"height": (83, 103), "weight": (23, 33)}
        },
        "male_names": [
            "Anton", "Basil", "Cliff", "Dom", "Evan", "Finn", "Giles", "Jasper", "Kip", "Lorin",
            "Miles", "Nico", "Ollie", "Pip", "Quinn", "Rollo", "Sly", "Toby", "Vern", "Waldo",
            "Xander", "Yann", "Zane", "Ander", "Boddy", "Cory", "Dane", "Evan", "Finn", "Giles",
            "Barrett", "Cyril", "Dexter", "Ellis", "Fletcher", "Graham", "Hugo", "Isaiah", "Jared", "Kyle",
            "Liam", "Mason", "Nolan", "Oscar", "Perry", "Quincy", "Reed", "Sean", "Tyler", "Ulysses",
            "Vincent", "Wesley", "Xavier", "Yale", "Zach"
        ],
        "female_names": [
            "Alia", "Bella", "Cassy", "Daisy", "Ella", "Fay", "Gilly", "Holly", "Ivy", "Jenna",
            "Kitty", "Lola", "Mina", "Nora", "Opal", "Polly", "Quilla", "Ruby", "Sally", "Tina",
            "Una", "Velma", "Wendy", "Xena", "Yana", "Zoe", "Aria", "Briar", "Cassia", "Della",
            "Ava", "Bree", "Clara", "Dina", "Elsa", "Faith", "Gina", "Hope", "Iris", "Joy",
            "Kay", "Lea", "Mae", "Nina", "Olive", "Paige", "Quinn", "Rose", "Sky", "Tess",
            "Ula", "Viv", "Willow", "Xena", "Yvonne", "Zara"
        ]
    },
    "Stout Halfling": {
        "last_names": [
            "Thickfoot", "Stoutbelly", "Heartyhedge", "Brewpot", "Aleheart", "Strongbranch",
            "Barleyloaf", "Toughbend", "Deepburrow", "Hardcheek", "Merrymeal", "Puddlejump",
            "Sturdyhill", "Broadleaf", "Teapot", "Heavypouch", "Briskbaker", "Boldfoot", 
            "Keeneye", "Firmgrip"
        ],
        "archetypes": ["Warrior", "Guard", "Brewmaster", "Farmer", "Stalwart Defender", "Mercenary"],
        "backgrounds": ["Soldier", "Artisan", "Farmer", "Guard", "Brewer", "Merchant"],
        "innate_abilities": ["Stout Resilience", "Lucky", "Brave", "Halfling Nimbleness"],
        "preferred_classes": ["Fighter", "Paladin", "Ranger", "Monk"],
        "culture": "Stout Halflings are heartier and more robust than their kin, often living in the heart of bustling communities. They are known for their exceptional craftsmanship, valuing hard work, dedication, and the protection of their homes.",
        "alignment": [
            "Lawful Good",
            "Lawful Neutral",
            "Neutral Good"
        ],
        "lore": "Stout Halflings have a natural resilience to toxins and a sturdy constitution, traits that serve them well in their industrious pursuits and when defending their homes from threats.",
        "physical_characteristics": {
            "Male": {"height": (92, 112), "weight": (32, 42)},
            "Female": {"height": (87, 107), "weight": (27, 37)}
        },
        "male_names": [
            "Alton", "Bram", "Cade", "Dale", "Eldon", "Finn", "Garrett", "Harol", "Ivor", "Jasper",
            "Lyle", "Milo", "Ned", "Osborn", "Perrin", "Quincy", "Roscoe", "Sam", "Tobias", "Ulric",
            "Vance", "Wilfred", "Xander", "Yorik", "Zed", "Ander", "Boddy", "Cory", "Dane", "Evan",
            "Corrin", "Derrik", "Edmon", "Fergus", "Galen", "Heron", "Isaac", "Jerrod", "Kelvin", "Leon",
            "Marlon", "Norbert", "Orton", "Preston", "Quinton", "Rupert", "Stefan", "Terron", "Upton", "Victor",
            "Warren", "Xylon", "York", "Zane", "Alden", "Baxter", "Cedric", "Dexter", "Eldric", "Fenton",
        ],
        "female_names": [
            "Amara", "Bella", "Cora", "Daisy", "Ella", "Fay", "Grace", "Hazel", "Ivy", "Jenna",
            "Kira", "Lana", "Mina", "Nora", "Opal", "Pippa", "Quilla", "Ruby", "Sara", "Tansy",
            "Una", "Violet", "Wendy", "Xeni", "Yara", "Zoe", "Aria", "Briar", "Cassia", "Della",
            "Althea", "Beatrix", "Celina", "Dora", "Eudora", "Felicia", "Greta", "Heidi", "Idalia", "Jolie",
            "Keira", "Leona", "Malia", "Nadia", "Oriana", "Petra", "Quinn", "Rosalind", "Selena", "Thalia",
            "Ursula", "Verna", "Wilma", "Xylia", "Yvette", "Zelda", "Adele", "Bianca", "Celia", "Dinah",
        ]
    },
    "Dwarf": {
        "last_names": [
            "Ironforge", "Steelhammer", "Bronzebeard", "Silveraxe", "Goldvein", "Stonefist",
            "Anvilbrow", "Forgefire", "Mountainson", "Deepdelver", "Oreheart", "Rockseeker",
            "Gemcutter", "Mithrilbraid", "Coalback", "Boulderchest", "Earthguard", "Flintknuckle",
            "Marblejaw", "Tunneltracker"
        ],
        "archetypes": ["Warrior", "Cleric", "Smith", "Brewmaster", "Merchant", "Miner", "Stonecarver", "Guard"],
        "backgrounds": ["Guild Artisan", "Soldier", "Noble", "Smith", "Miner", "Craftsman", "Mercenary"],
        "innate_abilities": ["Darkvision", "Dwarven Resilience", "Dwarven Combat Training", "Stonecunning", "Tool Proficiency"],
        "preferred_classes": ["Fighter", "Cleric", "Paladin", "Barbarian"],
        "culture": "Dwarven society is built on ancient traditions of craftsmanship, honor, and clan loyalty. Living in fortified mountain strongholds or deep underground cities, Dwarves are renowned for their skill in metallurgy, stonecraft, and engineering. Their communities are tight-knit, with a strong emphasis on family and clan ties.",
        "alignment": [
            "Lawful Good",
            "Neutral Good",
            "Lawful Neutral"
        ],
        "lore": "Dwarves are a stout and hardy folk, known for their longevity and resistance to the hardships. They are born into a world of stone and metal, finding beauty and strength in the heart of mountains. Their history is filled with tales of legendary warriors, ingenious artisans, and deep-seated feuds with goblins and orcs.",
        "physical_characteristics": {
            "Male": {"height": (130, 150), "weight": (70, 90)},
            "Female": {"height": (120, 140), "weight": (50, 70)}
        },
        "male_names": [
            "Adrik", "Balin", "Dain", "Durin", "Eberk", "Flint", "Gardain", "Harbek", "Kildrak", "Morgran",
            "Orsik", "Rangrim", "Thoradin", "Ulfgar", "Vondal", "Brottor", "Dolgrin", "Grunnar", "Holt", "Lodar",
            "Nurk", "Oskar", "Rurik", "Traubon", "Veit", "Barendd", "Brottor", "Bruenor", "Darrak", "Delg", "Einkil",
            "Fargrim", "Gardain", "Harbek", "Kildrak", "Morgran", "Orsik", "Oskar", "Rangrim", "Rurik", "Taklinn",
            "Gorren", "Thurim", "Barundar", "Fargrim", "Gloin", "Thrain", "Thror", "Bifur", "Bofur", "Bombur",
            "Dorin", "Groin", "Nain", "Narvi", "Oin", "Fundin", "Farin", "Gror", "Nori", "Dori"
            ],
        "female_names": [
            "Amber", "Artin", "Audhild", "Bardryn", "Dagnal", "Diesa", "Eldeth", "Falkrunn", "Gunnloda", "Helja",
            "Kathra", "Kristryd", "Mardred", "Riswynn", "Sannl", "Torbera", "Vistra", "Wilhel", "Yurda", "Zerda",
            "Bree", "Callie", "Cora", "Euphemia", "Jillian", "Kithri", "Lavinia", "Lidda", "Maegan", "Marigold",
            "Berylla", "Kotri", "Drumora", "Nali", "Dori", "Thili", "Frida", "Greda", "Hilda", "Ilde",
            "Kari", "Liftrasa", "Marni", "Nedis", "Sigrun", "Therlin", "Urda", "Vekka", "Fridil", "Gloa"
        ]
    },
    "Scourge Aasimar": {
        "last_names": [
            "Radiantwrath", "Lightbringer", "Suncaller", "Flareheart", "Dayguard", "Blazeborn",
            "Solarfury", "Heavenrage", "Divinespark", "Puritylash", "Halofire", "Glowreaper",
            "Dawnscourge", "Sunshard", "Luminaflame", "Brightstorm", "Celestialfire", "Aurorawing",
            "Coronablast", "Etherealblaze"
        ],
        "archetypes": ["Avenger", "Divine Agent", "Martyr", "Zealot", "Lightbringer", "Protector"],
        "backgrounds": ["Acolyte", "Hermit", "Missionary", "Solitary", "Guardian", "Divine Herald"],
        "innate_abilities": ["Radiant Consumption", "Light Bearer", "Healing Hands", "Celestial Resistance"],
        "preferred_classes": ["Paladin", "Cleric", "Sorcerer", "Warlock"],
        "culture": "Scourge Aasimar carry within them a burning divine light that they can unleash to smite their foes. However, this power comes at great personal risk, as the radiance consumes them as well. They are driven by a purpose to fight evil and darkness, often taking on crusades against malevolence.",
        "alignment": [
            "Lawful Good",
            "Neutral Good",
            "Lawful Neutral"
        ],
        "lore": "Born from a celestial bloodline, Scourge Aasimar are marked by their ability to channel intense radiant energy. This power is both a blessing and a curse, as it demands they confront evil directly, risking themselves to protect the innocent.",
        "physical_characteristics": {
            "Male": {"height": (165, 185), "weight": (70, 100)},
            "Female": {"height": (160, 180), "weight": (55, 85)}
        },
        "male_names": [
            "Azrael", "Cassiel", "Ezra", "Gideon", "Ishmael", "Jophiel", "Lucian", "Mikhael", "Nathaniel", "Raziel",
            "Sariel", "Uriel", "Zachariah", "Gabriel", "Seraph", "Raphael", "Daniel", "Samuel", "Michael", "Jerahmeel",
            "Ananiel", "Barachiel", "Cathetel", "Dumah", "Erelim", "Hadriel", "Imamiah", "Jehoel", "Kushiel", "Lemuel",
            "Manakel", "Nuriel", "Ophiel", "Penemue", "Quabriel", "Remliel", "Sealtiel", "Tzadkiel", "Usiel", "Vehuel",
            "Yofiel", "Zuriel", "Aphiel", "Bariel", "Cerviel", "Dabriel", "Ezekiel", "Faniel", "Gadriel", "Haniel",
        ],
        "female_names": [
            "Ariel", "Bethany", "Cassia", "Dina", "Eliana", "Gabrielle", "Hanael", "Isra", "Jael", "Katriel",
            "Lailah", "Muriel", "Naomi", "Ruth", "Seraphina", "Tamar", "Uriela", "Yael", "Zophiel", "Selaphiel",
            "Seraphiel", "Raphaela", "Sariel", "Uriel", "Zachariah","Anael", "Bethor", "Calah", "Dara", "Ela", "Faith", "Galia", "Hemera", "Irenea", "Jophia",
            "Kemuel", "Levana", "Maia", "Neha", "Oriel", "Phoebe", "Qastiel", "Rhea", "Sephora", "Thalassa",
            "Urania", "Vesta", "Yofie", "Zahara", "Alethea", "Brielle", "Cassiel", "Dinah", "Eliora", "Gavriela",
        ]
    },
    "Fallen Aasimar": {
        "last_names": [
            "Shadowborne", "Duskwither", "Gloomveil", "Fallenstar", "Nightsorrow", "Eclipsedheart",
            "Darkfeather", "Moonscorn", "Sunforsaken", "Twilightcurse", "Celestialfall", "Voidwhisper",
            "Starless", "Nightblessed", "Dawnbreaker", "Lightbane", "Eclipseward", "Grimshade",
            "Duskwalker", "Shadowflight"
        ],
        "archetypes": ["Avenger", "Shadow Knight", "Dark Paladin", "Revenant"],
        "backgrounds": ["Exile", "Haunted One", "Soldier", "Acolyte", "Outcast"],
        "innate_abilities": ["Necrotic Shroud", "Healing Hands", "Light Bearer", "Celestial Resistance"],
        "preferred_classes": ["Paladin", "Warlock", "Fighter", "Rogue"],
        "culture": "Fallen Aasimar have turned away from their celestial guidance, often due to tragedy or corruption. They embody darker aspects, with powers that can instill fear and manipulate the shadows. Despite their fall, some seek redemption, while others revel in their newfound darkness.",
        "alignment": [
            "Lawful Evil",
            "Neutral Evil",
            "Chaotic Good",
            "Chaotic Neutral",
            "True Neutral"
        ],
        "lore": "Once blessed with divine purpose, Fallen Aasimar have seen their celestial light dimmed or extinguished. Their fall from grace is a personal journey that can lead to villainy or a quest for redemption, making them complex figures caught between worlds.",
        "physical_characteristics": {
            "Male": {"height": (165, 185), "weight": (70, 100)},
            "Female": {"height": (160, 180), "weight": (55, 85)}
        },
        "male_names": [
            "Abaddon", "Balthazar", "Caim", "Draven", "Eblis", "Hadeon", "Ishkur", "Malik", "Nisroc", "Orpheus",
            "Paimon", "Ramiel", "Sammael", "Tartarus", "Valefar", "Zephon", "Azazel", "Dagon", "Gorgon", "Mammon",
            "Naberius", "Orias", "Phenex", "Rahab", "Semyaza", "Vassago", "Zagan", "Amon", "Belial", "Decarabia",
            "Belial", "Cerberus", "Dismas", "Erebus", "Fenriz", "Gehenna", "Hemah", "Incubus", "Kronos", "Leviathan",
            "Moloch", "Naberius", "Orias", "Phenex", "Quorin", "Ronove", "Sargatanas", "Thamuz", "Ukobach", "Vassago",
            "Xaphan", "Yeqon", "Zagan", "Amon", "Belial", "Decarabia", "Eurynomos", "Furfur", "Gusion", "Halphas",
        ],
        "female_names": [
            "Agrat", "Bathory", "Circe", "Dracul", "Eisheth", "Hecate", "Jezebel", "Kali", "Lilith", "Morrigan",
            "Nyx", "Olympia", "Pandora", "Ravenna", "Sekhmet", "Tiamat", "Ursula", "Vesper", "Xanthe", "Zephyra",
            "Astarte", "Baba", "Carmilla", "Diana", "Ereshkigal", "Freya", "Grendel", "Hela", "Ishtar", "Juno",
            "Alecto", "Bellona", "Dahlia", "Empusa", "Furiae", "Griselda", "Hesper", "Invidia", "Jinx", "Keres",
            "Lamia", "Mara", "Nemesis", "Onoskelis", "Persephone", "Qetesh", "Rusalka", "Sytry", "Thalia", "Ursel",
            "Vantha", "Witch", "Xesta", "Yuki", "Zilla", "Alecto", "Bellona", "Dahlia", "Empusa", "Furiae", "Griselda",
        ]
    },
    "Earth Genasi": {
        "last_names": [
            "Stonefist", "Ironroot", "Earthweaver", "Mudfoot", "Bouldershoulder", "Dirtwhisper",
            "Cliffwalker", "Rockbinder", "Gravelgrind", "Terraformer", "Oreheart", "Dustcloak",
            "Cragborn", "Gemsight", "Peakwarden", "Soilworn", "Groundshaker", "Mantledepth",
            "Quartzvein", "Graniteshield"
        ],
        "archetypes": ["Stoneguard", "Earthshaker", "Geomancer", "Boulderfist"],
        "backgrounds": ["Outlander", "Artisan", "Soldier", "Hermit", "Miner"],
        "innate_abilities": ["Earth Walk", "Merge with Stone", "Strength of the Earth", "Pass without Trace"],
        "preferred_classes": ["Fighter", "Druid", "Barbarian", "Monk"],
        "culture": "Earth Genasi are grounded and stoic, with societies that value strength, endurance, and the ability to work with stone and metal. Their communities are often found in mountainous or rocky areas, built to last through the ages. They have a deep connection to the land and are seen as unmovable in their resolve.",
        "alignment": [
            "True Neutral",
            "Neutral Good",
            "Neutral Evil"
        ],
        "lore": "Earth Genasi inherit their traits from earth elementals, often manifesting in their sturdy build and stoic nature. They have an innate connection with the earth, able to manipulate soil, rock, and metal, and draw strength from the ground beneath them.",
        "physical_characteristics": {
            "Male": {"height": (180, 200), "weight": (80, 120)},
            "Female": {"height": (175, 195), "weight": (70, 110)}
        },
        "male_names": [
        "Crag", "Granite", "Boulder", "Dolmen", "Flint", "Geo", "Mudar", "Ore", "Pebble", "Rock",
        "Stone", "Terra", "Cliff", "Dustan", "Gravel", "Mason", "Quartz", "Shale", "Terran", "Garnet",
        "Grit", "Moss", "Petrus", "Rubble", "Slate", "Talus", "Tomb", "Gneiss", "Lode", "Magma",
        "Bedrock", "Bor", "Craton", "Diorite", "Erdan", "Grit", "Halden", "Iron", "Ledger", "Marble",
        "Obsidian", "Plateau", "Ridge", "Slate", "Talus", "Umber", "Venture", "Yardang", "Zircon", "Gypsum",
        "Lode", "Mantle", "Nacre", "Olivine", "Pumice", "Quarry", "Rhyolite", "Sard", "Tuff", "Vermiculite"
        ],
        "female_names": [
            "Amber", "Citrine", "Gemma", "Jade", "Opal", "Ruby", "Sapphire", "Terra", "Diamond", "Emerald",
            "Jaspe", "Mica", "Pearl", "Rosalin", "Silica", "Topaz", "Agate", "Coral", "Onyx", "Ivy",
            "Lily", "Rose", "Violet", "Daisy", "Fern", "Hazel", "Iris", "Luna", "Olive", "Petal"
            "Alabaster", "Beryl", "Clay", "Dahlia", "Fern", "Garnetta", "Hazel", "Iolite", "Jaspera", "Lithia",
            "Marla", "Nephrite", "Peridot", "Quartzina", "Selenite", "Turquoise", "Una", "Vesta", "Wisteria", "Zinnia",
            "Argilla", "Brissa", "Calcite", "Drusa", "Esmeralda", "Felstone", "Galena", "Heliodor", "Igneous", "Kyanite"
        ]
    },
    "Fire Genasi": {
        "last_names": [
            "Flameheart", "Cinderforge", "Blazewarden", "Emberspark", "Pyrewalker", "Ashenfury",
            "Coalsmolder", "Infernofist", "Sootcloak", "Brightblaze", "Firebrand", "Lavaborn",
            "Heatwave", "Scorchscribe", "Flickerflame", "Wildfire", "Volcaneye", "Charbloom",
            "Flarewatcher", "Moltenvein"
        ],
        "archetypes": ["Flamecaller", "Pyromancer", "Inferno Blade", "Fireheart"],
        "backgrounds": ["Smith", "Soldier", "Survivor", "Artisan", "Rebel"],
        "innate_abilities": ["Darkvision", "Fire Resistance", "Reach to the Blaze", "Produce Flame"],
        "preferred_classes": ["Sorcerer", "Wizard", "Fighter", "Barbarian"],
        "culture": "Fire Genasi have a passion that matches the flickering flames they are connected to. Their communities are vibrant and dynamic, often found in warmer climates or volcanic regions. They are known for their exceptional metalwork and craftsmanship, as well as their fierce independence.",
        "alignment": [
            "Chaotic Neutral",
            "Chaotic Good",
            "Chaotic Evil"
        ],
        "lore": "Fire Genasi are born from the union of mortals and beings of elemental fire, carrying the flame's might in their veins. They are temperamental and charismatic, with a natural affinity for fire magic and an inherent resistance to heat and flames.",
        "physical_characteristics": {
            "Male": {"height": (170, 190), "weight": (60, 80)},
            "Female": {"height": (165, 185), "weight": (55, 75)}
        },
        "male_names": [
        "Blaze", "Brand", "Coal", "Ember", "Flint", "Ignis", "Pyro", "Scorch", "Tinder", "Vulcan",
        "Ash", "Cinder", "Flame", "Heat", "Inferno", "Sear", "Spark", "Flicker", "Torch", "Wildfire",
        "Char", "Fire", "Flare", "Glow", "Pyra", "Singe", "Smolder", "Soot", "Blaze", "Burn",
        "Ardor", "Brasier", "Crispin", "Drake", "Eldur", "Fiero", "Glow", "Hearth", "Incinero", "Jolt",
        "Kindle", "Lumen", "Magma", "Nero", "Orin", "Pyralis", "Ragnar", "Smolder", "Umbra", "Volcano",
        "Weld", "Xolotl", "Yanix", "Zephyr", "Blast", "Combust", "Dynamo", "Eflare", "Forge", "Gleed"
        ],
        "female_names": [
            "Amber", "Blaze", "Cinder", "Emberly", "Flicker", "Glenda", "Hestia", "Ignia", "Pyra", "Seara",
            "Tinder", "Vesta", "Wildfire", "Flare", "Scorchia", "Blazella", "Char", "Heatia", "Inferna", "Sol",
            "Singe", "Soot", "Flame", "Glow", "Pyra", "Singe", "Smolder", "Soot", "Blaze", "Burn",
            "Alev", "Branda", "Cressida", "Dinah", "Eldora", "Fiara", "Glory", "Hela", "Iris", "Jorja",
            "Keahi", "Lavia", "Melina", "Nova", "Oriana", "Phoenix", "Ravina", "Seraphina", "Thalassa", "Vulcana",
            "Whira", "Xyris", "Yalena", "Zel", "Adara", "Brielle", "Calida", "Desara", "Enya", "Fiamma"
        ]
    },
    "Water Genasi": {
        "last_names": [
            "Waveflow", "Stormsurge", "Deepcurrent", "Ripplewake", "Tidemourn", "Rainwhisper",
            "Brooksong", "Frostfathom", "Mistveil", "Rivergleam", "Seaborn", "Icebound",
            "Crestcaller", "Dewmirror", "Foambringer", "Gulfstride", "Springseeker", "Torrentscribe",
            "Whirlpool", "Bubblespark"
        ],
        "archetypes": ["Sorcerer", "Druid"],
        "backgrounds": ["Sailor", "Fisher", "Explorer"],
        "innate_abilities": ["Shape Water", "Amphibious", "Swim"],
        "culture": "Water Genasi often find themselves at the intersection of land and sea, harboring a deep connection with aquatic environments. Their communities are usually fluid, with members frequently traveling and exploring. Individuality and freedom are highly valued among Water Genasi, leading to a society where each member's path is as unique as the waters they cherish. Many serve as mediators between aquatic beings and land dwellers, using their innate abilities to bridge worlds.",
        "preferred_classes": ["Druid", "Sorcerer", "Wizard", "Rogue"],
        "alignment": [
            "True Neutral",
            "Chaotic Neutral",
            "Neutral Good"
        ],
        "lore": "Born of the union between the mortal realm and the elemental water, Water Genasi carry the essence of the seas, rivers, and rain within them. This heritage grants them a natural mastery over water and its forms, from the calmest pond to the most tempestuous ocean. While they are drawn to bodies of water, Water Genasi adapt to a variety of environments, their spirits as free as the waters they command.",
        "physical_characteristics": {
            "Male": {"height": (160, 190), "weight": (65, 100)},
            "Female": {"height": (155, 185), "weight": (60, 95)}
        },
        "male_names": [
        "Brook", "Caspian", "Dover", "Fjord", "Huron", "Lir", "Marin", "Nile", "Oceanus", "Reef",
        "River", "Thames", "Tide", "Triton", "Wade", "Zale", "Mist", "Rain", "Storm", "Marsh",
        "Cobalt", "Drift", "Eddy", "Ford", "Glacier", "Jet", "Moor", "Pike", "Rill", "Shoal",
        "Surge", "Thal", "Undine", "Vortex", "Whirl", "Bay", "Creek", "Gale", "Loch", "Murk",
        "Ripple", "Surf", "Torrent", "Brine", "Current", "Dew", "Flow", "Gulf", "Harbor", "Neptune",
        "Puddle", "Rivulet", "Sleet", "Tarn", "Wave", "Zephyr"
        ],
        "female_names": [
            "Aqua", "Cascade", "Delta", "Eyre", "Harbor", "Isle", "Kai", "Lagoon", "Marina", "Nerida",
            "Oceana", "Pearl", "Raina", "Serena", "Talia", "Undine", "Vivian", "Waverly", "Coral", "Misty",
            "River", "Shore", "Tide", "Wade", "Zale", "Mist", "Rain", "Storm", "Marsh", "Cobalt",
            "Brooke", "Crystal", "Diana", "Firth", "Gwen", "Harmony", "Isla", "Jewel", "Kelda", "Lake",
            "Mira", "Naida", "Opal", "Pacifica", "Ria", "Selkie", "Tarn", "Ula", "Velma", "Willow",
            "Azure", "Beryl", "Clarity", "Droplet", "Estuary", "Fountain", "Glimmer", "Haven", "Inlet", "Jade"
        ]
    },
    "Goblin": {
        "last_names": [
            "Sneaksnag", "Quickfingers", "Cragleap", "Nightrunner", "Mudscuttle", "Ratbait",
            "Firesnapper", "Puddlejumper", "Rustgear", "Scraptooth", "Bogwhisker", "Shinyfinder",
            "Dankfoot", "Grimnose", "Sootcloak", "Pestgrin", "Fizzlebang", "Trashmuncher",
            "Slinkboot", "Gadgetgrin"
        ],
        "archetypes": ["Trickster", "Scout", "Thief", "Warrior", "Alchemist"],
        "backgrounds": ["Urchin", "Criminal", "Survivor", "Mercenary", "Scavenger", "Rebel"],
        "innate_abilities": ["Darkvision", "Nimble Escape", "Fury of the Small"],
        "preferred_classes": ["Rogue", "Ranger", "Wizard", "Fighter"],
        "culture": "Goblin societies are often chaotic, organized in loose clans led by the strongest or most cunning among them. They are known for their survival instincts, living in the margins of the world, in dark forests, caves, and underground lairs. Goblins are resourceful, making the most of their environment to survive.",
        "alignment": [
            "Neutral Evil",
            "Chaotic Evil",
            "True Neutral"
        ],
        "lore": "Goblins are small, green-skinned creatures known for their cunning and resourcefulness. Their societies are built on the principles of strength and cunning, with power often changing hands through deceit or force.",
        "physical_characteristics": {
            "Male": {"height": (100, 120), "weight": (40, 55)},
            "Female": {"height": (95, 115), "weight": (35, 50)}
        },
        "male_names": [
            "Grib", "Snark", "Zig", "Wix", "Rax", "Nix", "Pix", "Kreel", "Grax", "Vex",
            "Znix", "Blip", "Warp", "Quip", "Zag", "Splug", "Tik", "Tok", "Gnak", "Nerk",
            "Brag", "Creak", "Dreg", "Flink", "Gnash", "Hob", "Irk", "Jank", "Klept", "Lurk",
            "Mung", "Nobble", "Ork", "Prang", "Quirk", "Runt", "Skulk", "Trimp", "Urk", "Vile",
            "Wretch", "Xank", "Yap", "Zorp", "Grift", "Plunk", "Qwix", "Rivel", "Sneer", "Twist",
            "Vex", "Warp", "Xip", "Yap", "Zig", "Blix", "Clink", "Drip", "Flix", "Grip",
        ],
        "female_names": [
            "Bree", "Grit", "Nella", "Zilch", "Pox", "Wizzle", "Tizzy", "Lix", "Pixie", "Sizzle",
            "Dree", "Vil", "Lilo", "Mink", "Zara", "Kiki", "Fizzle", "Glim", "Blix", "Razzle",
            "Zazz", "Frit", "Glim", "Hiss", "Jinx", "Kiki", "Lulu", "Mimi", "Nixie", "Pip",
            "Blink", "Cackle", "Drizzle", "Eek", "Fizzle", "Gabble", "Hiss", "Itch", "Jinx", "Klutz",
            "Muddle", "Nudge", "Ogle", "Piddle", "Quash", "Riddle", "Squib", "Tangle", "Uzzle", "Vex",
            "Wisp", "Xen", "Yowl", "Zap", "Creep", "Dabble", "Echo", "Flick", "Glimmer", "Hobble"
        ]
    },
    "Loxodon": {
        "last_names": [
            "Ivorytusk", "Templetrunk", "Serenestep", "Calmwater", "Gentlegiant", "Thundersnout",
            "Eldertrunk", "Quietriver", "Steadyhand", "Peacekeeper", "Soulherder", "Wisdomseeker",
            "Gravefoot", "Mossback", "Longmemory", "Stillwater", "Silentmarch", "Thunderfoot",
            "Ancientpath", "Sagebrush"
        ],
        "archetypes": ["Guardian", "Hierophant", "Stonemason", "Peacekeeper", "Shaman"],
        "backgrounds": ["Acolyte", "Hermit", "Soldier", "Artisan", "Monk", "Guild Artisan"],
        "innate_abilities": ["Powerful Build", "Natural Armor", "Keen Smell", "Serene", "Loxodon Serenity"],
        "preferred_classes": ["Cleric", "Monk", "Paladin", "Fighter"],
        "culture": "Loxodon societies are calm and structured, deeply spiritual, and follow a matriarchal hierarchy. They value wisdom, memory, and community, living in harmonious settlements. Their ceremonies and traditions are ancient, reflecting their deep connection to the earth and its cycles.",
        "alignment": [
            "Lawful Good",
            "Neutral Good",
            "Lawful Neutral"
        ],
        "lore": "Loxodons are elephantine humanoids known for their wisdom, strength, and peaceful nature. They are revered for their deep spiritual connection to the world and their formidable memory.",
        "physical_characteristics": {
            "Male": {"height": (210, 250), "weight": (300, 400)},
            "Female": {"height": (205, 245), "weight": (250, 350)}
        },
        "male_names": [
            "Throm", "Lorant", "Mamut", "Behemoth", "Ganesh", "Herdar", "Ivory", "Kurn", "Mastodon", "Nimar",
            "Ortusk", "Pran", "Quor", "Rantus", "Seran", "Tuskor", "Umar", "Vend", "Wooly", "Yantor",
            "Zantus", "Asterion", "Brom", "Carn", "Durn", "Euron", "Gorth", "Harkon", "Ith", "Jarn",
            "Karn", "Lorthos", "Mogis", "Naros", "Orgh", "Pythor", "Quorn", "Rath", "Sorn", "Thrax",
            "Zamur", "Baran", "Tolun", "Harun", "Jorim", "Velun", "Korin", "Sarvus", "Marun", "Telgor",
            "Durnam", "Volun", "Ceran", "Jerom", "Borun", "Atrus", "Pelor", "Gromun", "Horun", "Larvus",
            "Meran", "Norix", "Olum", "Perom", "Rumon", "Silun", "Turam", "Varun", "Worom", "Xerun", "Yarum", "Zuron"
        ],
        "female_names": [
            "Amaranth", "Berdine", "Calista", "Dhoruba", "Elandra", "Flor", "Ganesa", "Hathor", "Irie", "Jovita",
            "Kala", "Lunet", "Matrika", "Nadi", "Orla", "Panya", "Quanda", "Rada", "Sunita", "Tama", "Usha", "Vesta", "Zula",
            "Acantha", "Briza", "Circe", "Diona", "Eurydice", "Faela", "Ghita", "Hecuba", "Ianthe", "Jordis",
            "Kallista", "Lysa", "Merope", "Nyx", "Olympia", "Phaedra", "Rhea", "Stheno", "Thalia", "Ursa", "Vesta", "Xena", "Ylva", "Zephyra",
            "Belura", "Corinna", "Dulara", "Erona", "Firna", "Gerda", "Hulna", "Ivana", "Jorna", "Kerani",
            "Lorna", "Marula", "Nirali", "Olenna", "Perina", "Quirina", "Rosalin", "Selora", "Terani", "Ulani",
            "Verena", "Wilora", "Xylena", "Ysora", "Zarani", "Alera", "Brona", "Celara", "Drusa", "Elorna"
        ]
    },
    "Minotaur": {
        "last_names": [
            "Hornblade", "Mazewalker", "Bullheart", "Ragehorn", "Ironhoof", "Thunderroar",
            "Beastbreaker", "Stormcharge", "Warbellow", "Gorecaller", "Labyrinthborn", "Skullcrusher",
            "Earthstomp", "Bloodfur", "Runebrand", "Darkmaze", "Thunderhorn", "Battlebrawn",
            "Stonehoof", "Ragebound"
        ],
        "archetypes": ["Gladiator", "Marauder", "Berserker", "Navigator", "Guard"],
        "backgrounds": ["Soldier", "Sailor", "Outcast", "Laborer", "Gladiator", "Mercenary"],
        "innate_abilities": ["Horns", "Goring Rush", "Hammering Horns", "Labyrinthine Recall", "Imposing Presence"],
        "preferred_classes": ["Fighter", "Barbarian", "Paladin", "Ranger"],
        "culture": "Minotaur societies are built around strength and combat prowess, often residing in mazes or strongholds. They have a deep sense of honor and pride in their physical abilities, and their social structure is based on martial achievement.",
        "alignment": [
            "Chaotic Neutral",
            "Chaotic Good",
            "Neutral Good"
        ],
        "lore": "Minotaurs are bullish humanoids, known for their fearsome appearance and combat skills. Originating from ancient labyrinths, they carry the legacy of their maze-dwelling ancestors, combining brute strength with a keen strategic mind.",
        "physical_characteristics": {
            "Male": {"height": (200, 230), "weight": (100, 150)},
            "Female": {"height": (190, 220), "weight": (95, 145)}
        },
        "male_names": [
            "Asterion", "Brom", "Carn", "Durn", "Euron", "Gorth", "Harkon", "Ith", "Jarn", "Karn",
            "Lorthos", "Mogis", "Naros", "Orgh", "Pythor", "Quorn", "Rath", "Sorn", "Thrax", "Urgos", "Vorn", "Wulfgar", "Xanth", "Yagos", "Zethos",
            "Barus", "Craton", "Drakos", "Erebus", "Folgar", "Grast", "Huron", "Iskar", "Juron", "Krusos",
            "Lorak", "Moros", "Norok", "Oltos", "Prax", "Quron", "Rokar", "Stron", "Tork", "Ulkus", "Vrax", "Wrox", "Xerx", "Yurk", "Zorak",
            "Axom", "Bragos", "Cron", "Dak", "Erak", "Farg", "Gron", "Halm", "Ivgor", "Jax"
        ],
        "female_names": [
            "Acantha", "Briza", "Circe", "Diona", "Eurydice", "Faela", "Ghita", "Hecuba", "Ianthe", "Jordis",
            "Kallista", "Lysa", "Merope", "Nyx", "Olympia", "Phaedra", "Rhea", "Stheno", "Thalia", "Ursa", "Vesta", "Xena", "Ylva", "Zephyra",
            "Amaranth", "Berdine", "Calista", "Dhoruba", "Elandra", "Flor", "Ganesa", "Hathor", "Irie", "Jovita",
            "Aleria", "Brenna", "Coris", "Delia", "Enya", "Fiora", "Greta", "Helia", "Iris", "Jora",
            "Kyra", "Lora", "Myra", "Nora", "Oriana", "Pria", "Qyra", "Riona", "Sora", "Tyrna", "Ulyra", "Vyra", "Wynna", "Xylia", "Yara", "Zora",
            "Ariadne", "Bryseis", "Cyllene", "Daphne", "Elara", "Faythe", "Glykeria", "Hestia", "Ismene", "Jocasta",
        ]
    },
    "Simic Hybrid": {
        "last_names": [
            "Finclade", "Gillstream", "Tentashade", "Scalesight", "Krakenborn", "Wavefused",
            "Mantawave", "Biomeld", "Coralvein", "Aquasplice", "Hydraheart", "Eelwhisper",
            "Shellmind", "Barnaclebond", "Fathomjoin", "Seaforged", "Tidalmeld", "Zygomind",
            "Kelpmerge", "Surgecraft"
        ],
        "archetypes": ["Adapted Warrior", "Aquatic Envoy", "Experimental Escapee", "Geneticist", "Bioengineer"],
        "backgrounds": ["Researcher", "Guild Artisan", "Survivor", "Urban Explorer", "Scientist"],
        "innate_abilities": ["Animal Enhancement", "Carapace", "Grappling Appendages", "Nimble Climber", "Aquatic Adaptation", "Enhanced Senses"],
        "preferred_classes": ["Fighter", "Rogue", "Wizard", "Druid"],
        "culture": "Simic Hybrids often struggle with their identity, caught between the worlds of their original races and the new capabilities they possess. Many find a sense of belonging within the Simic Combine, where their talents can be honed for the betterment of all.",
        "alignment": [
            "Lawful Good", "Neutral Good", "Chaotic Good",
            "Lawful Neutral", "True Neutral", "Chaotic Neutral",
            "Lawful Evil", "Neutral Evil", "Chaotic Evil"
        ],
        "lore": "Created through magical experimentation, Simic Hybrids seek to perfect life by combining the best aspects of different beings. Their existence is a testament to both the potential and dangers of unbridled biological research. Simic Hybrids result from arcane experiments combining various humanoid and aquatic creature features, primarily conducted by the Simic Combine in settings like Ravnica. They are known for their adaptability and the unique modifications that grant them a variety of enhancements tailored to their environment or tasks.",
        "physical_characteristics": {
            "Male": {"height": (155, 195), "weight": (60, 100)},
            "Female": {"height": (150, 190), "weight": (55, 95)}
        },
        "male_names": [
            "Adrix", "Biomut", "Cytoplast", "Drex", "Evolv", "Fint", "Gel", "Hydropon", "Ixidor", "Jelenn",
            "Kraj", "Ludvic", "Mimeoplasm", "Nucleon", "Ooze", "Plax", "Quor", "Rafiq", "Simic", "Telcor", "Uro", "Vig", "Zegana",
            "Aether", "Biomass", "Cytos", "Drax", "Evolvus", "Fintus", "Gelos", "Hydrus", "Ixidus", "Jelennus",
            "Brinelin", "Craej", "Duovex", "Ecton", "Fluxum", "Glacian", "Hex", "Intrax", "Jovix", "Krex",
            "Lumagraft", "Morophon", "Nexil", "Ovrix", "Phyto", "Rax", "Stemix", "Trovax", "Umbrix", "Volax", "Wrax", "Xenograft", "Yolvix", "Zonot"
        ],
        "female_names": [
            "Alira", "Biogene", "Cyanea", "Daphnia", "Elodea", "Fucus", "Gyre", "Hydra", "Ionia", "Jessa",
            "Kelpie", "Laminaria", "Merfolk", "Naiad", "Ondine", "Pelagia", "Quilla", "Riven", "Syl", "Thalassa", "Umbra", "Vortex", "Wave", "Zoosporea",
            "Aqua", "Bios", "Cytos", "Drae", "Evo", "Fint", "Gel", "Hydro", "Ix", "Jel",
            "Amarin", "Bryozoa", "Cnidaria", "Diatom", "Ephyra", "Florina", "Genlisea", "Helia", "Isogen", "Jellica",
            "Koral", "Lysigen", "Mycon", "Nymphae", "Oleander", "Phyrexia", "Quintara", "Rhizome", "Selagin", "Tisane", "Ulva", "Vallis", "Xylem", "Yarrow", "Zephyranth"
        ]
    },
    "Kalashtar": {
        "last_names": [
            "Mindwhisper", "Dreamsailor", "Thoughtwave", "Soulbinder", "Spiritdance", "Lightweaver",
            "Etherwalker", "Starvoyager", "Astralguide", "Celestialseeker", "Psychicwind", "Visionquester",
            "Tranquilstream", "Serenitywoven", "Peacebringer", "Harmonyflame", "Insightgazer", "Oraclepath",
            "Mysticwander", "Reveriekeeper"
        ],
        "archetypes": ["Mindful Protector", "Spiritual Emissary", "Dreamspeaker", "Psychic Warrior"],
        "backgrounds": ["Haunted One", "Hermit", "Sage", "Acolyte", "Outsider"],
        "innate_abilities": ["Telepathy", "Psychic Resistance", "Dual Mind", "Dreamer"],
        "preferred_classes": ["Monk", "Paladin", "Psion", "Sorcerer"],
        "culture": "Kalashtar communities are serene and introspective, focusing on meditation, the exploration of dreams, and the pursuit of inner peace. They are empathetic and driven by a collective desire to fend off the darkness that threatens their spirit counterparts.",
        "alignment": [
            "Lawful Good",
            "Neutral Good",
            "Lawful Neutral"
        ],
        "lore": "Kalashtar are mystical beings, born from the union between humanity and renegade spirits from the plane of dreams, known as Quori. They possess psychic abilities and a deep, spiritual connection to the world of dreams. The Kalashtar were formed through a rebellion within the realm of dreams, merging human hosts with escaping Quori spirits. This bond grants them their psychic abilities and a dual consciousness, experiencing both human and Quori thoughts.",
        "physical_characteristics": {
            "Male": {"height": (165, 185), "weight": (65, 85)},
            "Female": {"height": (160, 180), "weight": (60, 80)}
        },
        "male_names": [
            "Aran", "Borak", "Davan", "Hakan", "Idrin", "Jorrel", "Kean", "Lan", "Miran", "Nolan",
            "Orin", "Pavan", "Quori", "Rolan", "Sarim", "Talan", "Urin", "Var", "Wilom", "Xanaphia",
            "Baran", "Cyril", "Dythan", "Erandi", "Firan", "Garan", "Harun", "Ishar", "Javan", "Kyran",
            "Loran", "Mykal", "Niraj", "Olan", "Pyran", "Qadir", "Roshan", "Sajan", "Taran", "Uthal", "Veer", "Wynash", "Xyrus", "Yoren", "Zorander"
        ],
        "female_names": [
            "Ari", "Bala", "Chana", "Dava", "Ehani", "Farah", "Ghani", "Hala", "Irina", "Jhani",
            "Kala", "Liri", "Mhani", "Nari", "Oli", "Pala", "Quista", "Rani", "Sari", "Thava", "Uhani", "Vala", "Wynri", "Xyli", "Yala", "Zhani",
            "Alani", "Bryn", "Caeli", "Dyani", "Erini", "Faera", "Gyli", "Hani", "Isari", "Jael",
            "Kyri", "Lysa", "Maeli", "Nyssa", "Ori", "Priya", "Qyra", "Raeli", "Sani", "Tyra", "Ulyra", "Vyli", "Wysa", "Xyra", "Yani", "Zyli"
        ]
    },
    "Beasthide": {
        "last_names": [
            "Thickhide", "Stonefur", "Ironpelt", "Wildmane", "Densebristle", "Hardback",
            "Bouldercoat", "Toughwool", "Sturdygrowl", "Shieldskin", "Oakenfur", "Gritscale",
            "Steelwool", "Ruggedtrail", "Brawnhide", "Mossback", "Granitehair", "Forgeleather",
            "Cragbeard", "Brickshell"
        ],
        "archetypes": ["Resilient Guardian", "Feral Defender", "Wilderness Survivor", "Stalwart Protector"],
        "backgrounds": ["Outlander", "Soldier", "Guard", "Athlete", "Farmer"],
        "innate_abilities": ["Shifting Feature (Tough Hide)", "Enhanced Durability", "Stalwart Shift"],
        "preferred_classes": ["Barbarian", "Fighter", "Ranger", "Druid"],
        "culture": "Beasthide Shifters value strength, endurance, and the ability to withstand adversity. Their communities are often close-knit, with a strong emphasis on protecting one another and surviving the challenges of the wild.",
        "alignment": [
            "True Neutral",
            "Chaotic Neutral",
            "Neutral Good"
        ],
        "lore": "Beasthide Shifters, one of the many shifter subraces, possess animalistic features and can transform to enhance their physical resilience. Known for their toughness, they are descendants of humans and lycanthropes. Arising from the union of humans and lycanthropes, Beasthide Shifters have inherited the ability to tap into their bestial nature, gaining enhanced physical capabilities. They live on the edge of civilization, where they can be free to embrace their dual nature.",
        "physical_characteristics": {
            "Male": {"height": (165, 195), "weight": (75, 115)},
            "Female": {"height": (160, 190), "weight": (70, 110)}
        },
        "male_names": [
            "Arbor", "Brunt", "Crag", "Durn", "Elgor", "Fangar", "Grunt", "Harken", "Iron", "Jurg",
            "Kurn", "Lurtz", "Mog", "Narg", "Orsik", "Prunt", "Quark", "Rusk", "Strom", "Turg", "Ulgar", "Vond", "Warg", "Xang", "Yurk", "Zorn",
            "Axe", "Bane", "Claw", "Dusk", "Fang", "Gore", "Hawk", "Jaw", "Krag", "Lash", "Maul", "Nail", "Ogre", "Pike", "Quake", "Rage", "Stag", "Tusk", "Vex", "Warg", "Xorn", "Yarn", "Zorn"
            "Brogan", "Drake", "Garrick", "Harben", "Krag", "Mardon", "Norix", "Parn", "Rendal", "Skarn", 
            "Thar", "Vrox", "Zoltan", "Baron", "Drex", "Felk", "Jarv", "Morak", "Rav", "Sorn", "Torbin", 
            "Varl", "Wilg", "Xor", "Yarn", "Zarv"
        ],
        "female_names": [
            "Arna", "Brena", "Curna", "Dorna", "Elna", "Fiera", "Gruna", "Harna", "Irna", "Jorna",
            "Korna", "Lurna", "Morna", "Norna", "Orna", "Purna", "Qurna", "Runa", "Surna", "Tarna", "Urna", "Vorna", "Wurna", "Xerna", "Yerna", "Zurna",
            "Brytta", "Della", "Fayra", "Hestra", "Kella", "Lara", "Myra", "Nyssa", "Orella", "Pyra", 
            "Ryla", "Sella", "Thyra", "Ursa", "Vella", "Wynna", "Xylla", "Ysma", "Zella", "Arya", "Brynn", 
            "Cyra", "Drusa", "Evyra", "Glynna", "Hyla", "Ilyra", "Jyra", "Kyna", "Lyna", "Myra", "Nyla",
        ]
    },
    "Longtooth": {
        "last_names": [
            "Ironfang", "Wolfbinder", "Bearmantle", "Tigertooth", "Lionheart", "Ravenclaw",
            "Elkbane", "Hawkridge", "Bullforce", "Serpentgrin", "Dragonsnarl", "Eagleplume",
            "Boarbristle", "Pantherprowl", "Stagroar", "Viperlash", "Falconwing", "Rhinocharge",
            "Cobraclasp", "Pumafist"
        ],
        "archetypes": ["Fierce Warrior", "Pack Hunter", "Wild Adventurer", "Savage Fighter"],
        "backgrounds": ["Outlander", "Hunter", "Mercenary", "Gladiator", "Scout"],
        "innate_abilities": ["Shifting Feature (Fierce Bite)", "Enhanced Strength", "Feral Tenacity"],
        "preferred_classes": ["Barbarian", "Ranger", "Fighter", "Rogue"],
        "culture": "Longtooth Shifters are known for their ferocity and loyalty to their pack. They often live in close-knit communities, valuing strength, courage, and the bonds of kinship.",
        "alignment": ["Neutral Good", "Chaotic Good", "True Neutral","Chaotic Neutral"],
        "lore": "Descendants of ancient lycanthropes, Longtooths have mastered the balance between their human and bestial natures. They are revered and feared for their ferocity in battle and their unyielding loyalty to their pack.",
        "physical_characteristics": {
            "Male": {"height": (170, 190), "weight": (80, 110)},
            "Female": {"height": (160, 180), "weight": (70, 100)}
        },
        "male_names": [
            "Bark", "Claw", "Drift", "Echo", "Frost", "Grove", "Hawk", "Icicle", "Jolt", "Kite",
            "Leaf", "Moss", "Noble", "Oak", "Peak", "Quartz", "Ridge", "Slate", "Tide", "Umbra", "Vale", "Wind", "Xylem", "Yew", "Zephyr",
            "Blaze", "Canyon", "Dune", "Ember", "Flint", "Glacier", "Horizon", "Inferno", "Jasper", "Kraken", 
            "Lynx", "Magma", "Nimbus", "Obsidian", "Pine", "Quake", "Raptor", "Stone", "Torrent", "Vulcan", 
            "Wildfire", "Yosemite", "Zircon", "Axel", "Boulder", "Crest", "Dusk", "Everest", "Falcon", "Gale",
        ],
        "female_names": [
            "Aura", "Breeze", "Cedar", "Dew", "Ember", "Fawn", "Glade", "Heather", "Ivy", "Jasmine",
            "Kestrel", "Luna", "Meadow", "Nectar", "Olive", "Petal", "Quill", "Raven", "Star", "Terra", "Unity", "Violet", "Willow", "Xena", "Yarrow", "Zenith",
            "Briar", "Crystal", "Dahlia", "Echo", "Flora", "Garnet", "Hazel", "Indigo", "Juniper", "Kimber", 
            "Lilac", "Marigold", "Nova", "Opal", "Pearl", "Ruby", "Sapphire", "Topaz", "Ursula", "Verdant", 
            "Wisteria", "Xanthe", "Yucca", "Zinnia", "Amber", "Beryl", "Coral", "Daisy", "Emerald", "Fern",
        ]
    },
    "Swiftstride": {
        "last_names": [
            "Quickwind", "Fleetfoot", "Shadowleap", "Silentstep", "Rapidstream", "Moonchaser",
            "Sunrunner", "Windswift", "Brightsprint", "Starvault", "Galebound", "Lightningtread",
            "Thunderskip", "Cloudrace", "Skydash", "Riverdance", "Dewstride", "Stormsprint",
            "Echoglide", "Nimbleshift"
        ],
        "archetypes": ["Rogue", "Ranger", "Duelist", "Scout", "Assassin", "Swashbuckler"],
        "backgrounds": ["Urchin", "Outlander", "Charlatan", "Entertainer", "Spy", "Rebel"],
        "innate_abilities": ["Shifting", "Dextrous", "Swift Stride", "Evasive", "Natural Stealth"],
        "preferred_classes": ["Rogue", "Ranger", "Monk", "Bard"],
        "culture": "Swiftstride Shifters are elusive and independent, often seen as loners. They excel in stealth and speed, using their abilities to outmaneuver foes and perform recon missions.",
        "alignment": [
            "Chaotic Neutral",
            "Chaotic Good",
            "Neutral Good"
        ],
        "lore": "Swiftstride, often hailed from the whispering forests and vast plains, are beings of grace and velocity. Known for their unparalleled agility, they move with the wind, leaving barely a trace behind. Descendants of a mystical lineage that blends with the natural world, Swiftstrides have an innate connection to the land that allows them to navigate through the most treacherous terrains with ease. Their societies value freedom, movement, and harmony with nature, often living in nomadic tribes or secluded communities. Despite their elusive nature, Swiftstrides are fiercely loyal to their kin and allies, using their swift movements to protect their lands from any who dare to disrupt the balance.",
        "physical_characteristics": {
            "Male": {"height": (165, 185), "weight": (65, 85)},
            "Female": {"height": (160, 180), "weight": (60, 80)}
        },
        "male_names": [
            "Blaze", "Crest", "Dash", "Eagle", "Flint", "Gale", "Haze", "Inferno", "Jet", "Kestrel",
            "Lightning", "Meteor", "Nimbus", "Onyx", "Peregrine", "Quest", "Racer", "Surge", "Torrent", "Vortex", "Whirl", "Zephyr",
            "Arrow", "Bolt", "Canyon", "Drake", "Expanse", "Falcon", "Graphite", "Horizon", "Impact",
            "Jolt", "Kite", "Lynx", "Mach", "Nitro", "Obsidian", "Prism", "Quartz", "Rift", "Sprint",
            "Talon", "Uplift", "Velocity", "Wind", "Xenon", "Yacht", "Zinc"
        ],
        "female_names": [
            "Astra", "Bolt", "Celeste", "Dawn", "Echo", "Flicker", "Glimmer", "Halo", "Iris", "Joy",
            "Kite", "Lark", "Mist", "Nova", "Orbit", "Pulse", "Quiver", "Ripple", "Spark", "Twilight", "Vivid", "Whisper", "Zest",
            "Aurora", "Breeze", "Cirrus", "Dazzle", "Ember", "Flash", "Glow", "Harmony", "Indigo",
            "Jubilee", "Karma", "Lotus", "Mirage", "Nebula", "Oasis", "Phoenix", "Quest", "Radiance",
            "Stellar", "Turbulence", "Umbra", "Vapor", "Wave", "Xylo", "Yield", "Zen"
        ]
    },
    "Wildhunt": {
        "last_names": [
            "Stormhowler", "Moontracker", "Frostfang", "Shadowpelt", "Thunderrunner", "Riversnarl",
            "Windstalker", "Nightlurker", "Misthowl", "Rainchaser", "Snowstalker", "Dawnprowler",
            "Grovebound", "Starhunter", "Sunsprint", "Earthgrowler", "Flamepaw", "Icetreader",
            "Thundervein", "Skymane"
        ],
        "archetypes": ["Druid", "Ranger", "Beastmaster", "Guardian", "Survivalist", "Tracker"],
        "backgrounds": ["Hermit", "Outlander", "Sage", "Folk Hero", "Guide", "Hunter"],
        "innate_abilities": ["Shifting", "Enhanced Senses", "Mark of the Wild", "Natural Camouflage", "Beast's Intuition"],
        "preferred_classes": ["Druid", "Ranger", "Cleric", "Barbarian"],
        "culture": "Wildhunt Shifters have a deep connection to the natural world, often serving as its stewards. They are unparalleled trackers who use their keen senses to protect their lands and allies from threats.",
        "alignment": [
            "Lawful Good",
            "Neutral Good",
            "Lawful Neutral"
        ],
        "lore": "Descendants of the union between the primeval forces of nature and mortals, Wildhunt members are imbued with an innate connection to the wild. Known for their unparalleled tracking abilities and a deep bond with beasts, they often serve as guardians of sacred groves and protectors of the balance between civilization and the untamed world.",
        "physical_characteristics": {
            "Male": {"height": (170, 195), "weight": (75, 95)},
            "Female": {"height": (165, 190), "weight": (70, 90)}
        },
        "male_names": [
            "Thorn", "Bramble", "Leaf", "Gust", "Ridge", "Stone", "River", "Storm", "Clay", "Dale",
            "Fern", "Hawk", "Jasper", "Moss", "Orion", "Pike", "Rune", "Slate", "Vale", "Wolf",
            "Ash", "Boulder", "Cedar", "Drift", "Elm", "Flare", "Glenn", "Heath", "Iron", "Kite",
            "Larch", "Moor", "Nestor", "Oak", "Peak", "Quartz", "Reed", "Shale", "Thicket", "Umber",
            "Vent", "Wold", "Yarrow", "Zenith"
        ],
        "female_names": [
            "Breeze", "Brook", "Dawn", "Echo", "Fawn", "Gale", "Heather", "Ivy", "Luna", "Meadow",
            "Nectar", "Opal", "Petal", "Rain", "Sky", "Star", "Terra", "Violet", "Willow", "Zephyr",
            "Aurora", "Briar", "Crystal", "Dew", "Ember", "Flora", "Glade", "Holly", "Jade", "Kiwi",
            "Laurel", "Marigold", "Nyssa", "Olive", "Pearl", "Quill", "Rose", "Sage", "Thyme", "Unity",
            "Verdant", "Wren", "Yucca", "Zinnia"
        ]
    },
    "Owlin": {
        "last_names": [
            "Nightheart", "Silentwing", "Moonfeather", "Stormbeak", "Windswoop", "Gloomclaw",
            "Duskplume", "Twilighteye", "Shadowflight", "Frostfeather", "Skytalons", "Starhunter",
            "Hollowhooter", "Mistfeather", "Dawnwatcher", "Galeclaw", "Tidefeather", "Nightwhisper",
            "Snowwing", "Forestwatch"
        ],
        "archetypes": ["Wizard", "Sorcerer", "Scholar", "Mystic", "Watcher", "Sentry"],
        "backgrounds": ["Acolyte", "Sage", "Hermit", "Watcher", "Librarian", "Navigator"],
        "innate_abilities": ["Flight", "Keen Sight", "Silent Feathers", "Night Vision", "Wind Wisdom"],
        "preferred_classes": ["Wizard", "Sorcerer", "Rogue", "Monk"],
        "culture": "Owlin communities are often found in secluded, forested regions, preferring the calm of the night. They are known for their wisdom, close-knit families, and a deep connection to the moon and stars. Owlin society values knowledge and stealth, using their abilities to protect their homes and gather information.",
        "alignment":  [
            "True Neutral",
            "Neutral Good",
            "Neutral Evil"
        ],
        "lore": "Originally from a realm of twilight and endless forests, the Owlin carry the mystique of the night in their very beings. They are seen as omens of change or guardians of ancient secrets, moving silently through the night sky.",
        "physical_characteristics": {
            "Male": {"height": (150, 170), "weight": (45, 60)},
            "Female": {"height": (145, 165), "weight": (40, 55)}
        },
        "male_names": [
            "Alden", "Barn", "Cedric", "Darian", "Elton", "Falcon", "Glyn", "Hoot", "Icarus", "Jareth",
            "Kestrel", "Lark", "Merlin", "Nestor", "Orville", "Peregrine", "Quill", "Raven", "Soren", "Talon",
            "Alaric", "Branton", "Colm", "Davin", "Eldwyn", "Farrell", "Garrick", "Haldor", "Inigo", "Jovin",
            "Kelvin", "Lorin", "Merrick", "Norvin", "Oswin", "Paden", "Quinby", "Roland", "Stellan", "Thorin",
            "Ulric", "Vernon", "Wilbur", "Xenon", "Yorick", "Zane", "Axel", "Barrett", "Corvin", "Drake",
            "Egon", "Finn", "Gideon", "Halston", "Idris", "Joel", "Kai"
        ],
        "female_names": [
            "Aria", "Briar", "Celeste", "Diana", "Eowyn", "Flora", "Glenda", "Hazel", "Iris", "Jade",
            "Kira", "Lyla", "Mina", "Nova", "Olive", "Phoebe", "Quilla", "Rhea", "Serena", "Tawny",
            "Alia", "Bryn", "Cassia", "Delia", "Elowen", "Fawn", "Giselle", "Harlow", "Ilaria", "Janelle",
            "Kestrel", "Lisette", "Maris", "Nyla", "Opal", "Pearl", "Quincy", "Rowena", "Selene", "Tindra",
            "Ursa", "Vesper", "Willow", "Xena", "Yvette", "Zinnia", "Amara", "Beatrix", "Calista", "Dawn",
            "Echo", "Fable", "Gwen", "Haven", "Isa", "Jolie", "Kyra", "Luna", "Mira", "Nyx", "Oona",
        ]
    },
    "Fairy": {
        "last_names": [
            "Moondancer", "Sunsparkle", "Starwhisper", "Glimmerwing", "Twilightgleam", "Breezewhisper",
            "Dewtwinkle", "Glowblossom", "Shadowflutter", "Lightshimmer", "Mistymeadow", "Raindropripple",
            "Frostspark", "Thornwhisper", "Petaldrift", "Wispwander", "Nightshine", "Daydreamer",
            "Eclipseflutter", "Rainbowgleam","Dewpetal", "Moonwhisper", "Sunsparkle", "Starlight", "Glimmerwing", "Thornheart", "Rosevine",
            "Breezebloom", "Nightshade", "Lightfoot", "Shimmerleaf", "Brightdawn", "Mistwisp", "Cloudskipper",
            "Raindrop", "Snowflake", "Eclipse", "Windsong", "Meadowbrook", "Wildflower"
        ],
        "archetypes": [
        "Trickster", "Guardian of Nature", "Mystic Dancer", "Elemental Adept"
    ],
        "backgrounds": [
        "Wandering Minstrel", "Herbalist", "Forest Protector", "Artisan", "Explorer"
    ],
        "innate_abilities":  [
        "Flight", "Invisibility", "Nature Magic", "Fey Ancestry"
    ],
        "culture": "Fairies live in vibrant, hidden enclaves within enchanted forests or mystical glades. Their society is playful and mischievous, yet they hold a deep respect for nature and the balance of the natural world. Fairies are fiercely protective of their homes, using their magic to thwart those who would do harm to their realms. Fairies are deeply connected to nature and the magical world. They thrive in enchanted forests and mystical groves, living in harmony with the land. Their societies are often seen as whimsical and lighthearted, but they fiercely protect their homes from any harm.",
        "alignment": [
            "Chaotic Neutral",
            "Chaotic Good",
            "Chaotic Evil"
        ],
        "preferred_classes": [
        "Druid", "Ranger", "Sorcerer", "Bard"
        ],
        "lore": "Fairies are embodiments of the wild and wondrous aspects of the world. They are born from laughter, joy, and the unbridled energy of life itself, making them natural wielders of magic and guardians of nature’s mysteries.",
        "physical_characteristics": {
            "Male": {"height": (10, 20), "weight": (1, 3)},
            "Female": { "height": (10, 20), "weight": (1, 3)}
        },
        "male_names": [
            "Anlon", "Birch", "Caelum", "Dell", "Eirnin", "Fionn", "Galen", "Hale", "Ianthe", "Jorin",
            "Kyler", "Lorcan", "Milo", "Niall", "Oberon", "Pyrus", "Quilo", "Roric", "Silvan", "Tyto",
            "Larkin", "Merrow", "Nevin", "Orin", "Puck", "Quinn", "Rowan", "Seamus", "Taran", "Uilliam",
            "Varden", "Wynn", "Xylon", "Yarrow", "Zephyr", "Alastar", "Bracken", "Corin", "Devlin", "Eamon",
            "Finbar", "Gareth", "Hayden", "Iollan", "Jarlan", "Keenan", "Leif", "Morcan", "Neale", "Oisin",
            "Padraig", "Quinlan", "Ronan", "Sorley", "Turlough", "Urien", "Vaughn", "Wilf", "Xander", "Yestin",

        ],
        "female_names": [
            "Aine", "Bella", "Cerise", "Daphne", "Elara", "Fay", "Gemma", "Halia", "Ivy", "Jasmine",
            "Kyla", "Liora", "Maeve", "Nixie", "Ondine", "Piper", "Quilla", "Rosalind", "Sylvie", "Thalia",
            "Luna", "Meadow", "Nectar", "Opal", "Petal", "Rain", "Sky", "Star", "Terra", "Violet",
            "Willow", "Zephyr", "Astra", "Breeze", "Cedar", "Dew", "Ember", "Fawn", "Glade", "Heather",
            "Aisling", "Breena", "Clodagh", "Deirdre", "Etain", "Fianna", "Grainne", "Honora", "Isolde", "Juno",
            "Keira", "Lunette", "Meara", "Niamh", "Orla", "Petra", "Riona", "Saoirse", "Tressa", "Una",
            "Vevina", "Wynne", "Xylia", "Yseult", "Zelda", "Alannah", "Brielle", "Callista", "Dara", "Eirlys",
            "Ffion", "Glynis", "Heulwen", "Iona", "Julitta", "Katell", "Lys", "Morgana", "Nolwenn", "Ophira"
        ]
    },
    "Rabbitfolk (Harengon)": {
        "last_names": [
            "Quickfoot", "Thistlehop", "Briarbound", "Meadowleap", "Greenfield", "Cottonwhisker",
            "Burrowskip", "Hedgejumper", "Cloverfinder", "Dewsniffer", "Grasswhistle", "Leapshadow",
            "Fernsprint", "Hazelbuck", "Puddlejumper", "Sprintgrass", "Vinehopper", "Willowbound",
            "Brookskip", "Dandelionwisp"
        ],
        "archetypes": ["Ranger", "Rogue", "Alchemist", "Jester", "Scout", "Trickster"],
        "backgrounds": ["Farmer", "Merchant", "Artisan", "Entertainer", "Explorer", "Fugitive"],
        "innate_abilities": ["Leporine Senses", "Rabbit Hop", "Lucky Footwork", "Burrow", "Hare's Agility"],
        "preferred_classes": ["Rogue", "Ranger", "Bard", "Druid"],
        "culture": "Rabbitfolk communities are often found in meadows, forests, or fertile lands where they can live in harmony with the environment. They are known for their quick wits, agility, and a strong sense of community. Harengon society emphasizes the joy of exploration and the value of curiosity, with many tales of adventure passed down through generations.",
        "alignment": [
            "Chaotic Neutral",
            "Chaotic Good",
            "Chaotic Evil"
        ],
        "lore": "The Harengon are blessed by the spirit of the hare, granting them remarkable agility and luck. They are natural explorers and survivors, adept at navigating both the wilds and the stories of their people.",
        "physical_characteristics": {
            "Male": {"height": (125, 145), "weight": (35, 45)},
            "Female": {"height": (120, 140), "weight": (30, 40)}
        },
        "male_names": [
            "Burrow", "Clover", "Dandelion", "Elm", "Fiver", "Gorse", "Hazel", "Inkwell", "Jumper", "Kip",
            "Leap", "Mallow", "Nibble", "Oats", "Pounce", "Quiver", "Rabbit", "Skip", "Thumper", "Vetch",
            "Barley", "Cotton", "Drift", "Echo", "Flint", "Grass", "Harvest", "Ivy", "Jolly", "Mirth",
            "Nestor", "Orchard", "Patch", "Rustle", "Sprint", "Tiller", "Wicket", "Yarrow", "Zephyr",
        ],
        "female_names": [
            "Bunny", "Cinnamon", "Daisy", "Ember", "Fern", "Ginger", "Honey", "Iris", "Juniper", "Lily",
            "Maple", "Nutmeg", "Olive", "Poppy", "Quincy", "Rose", "Sunny", "Tulip", "Violet", "Willow",
            "Aster", "Blossom", "Clove", "Dewdrop", "Elm", "Fawn", "Gale", "Heather", "Ivy", "Luna",
            "Blossom", "Clove", "Dewdrop", "Eclair", "Flora", "Glade", "Harmony", "Jade", "Kiwi", "Laurel",
            "Meadow", "Orchid", "Petunia", "Ruby", "Sprout", "Trill", "Unity", "Verdant", "Whisper", "Zinnia"
        ]
    },
    "Centaur": {
        "last_names": [
            "Swiftwind", "Thunderhoof", "Meadowmane", "Forestgallop", "Riverstride", "Stormchaser", 
            "Plainstalker", "Heathrunner", "Wildmane", "Greenmeadow", "Cloudleaper", "Nightgallop", 
            "Dawntracker", "Sunstampede", "Moonhoof", "Starherder", "Windsweeper", "Grasswhisper", 
            "Raindancer", "Snowrunner"
        ],
        "archetypes": ["Warrior", "Guardian", "Scout", "Emissary", "Druid", "Ranger"],
        "backgrounds": ["Outlander", "Hermit", "Soldier", "Gladiator", "Nomad", "Guide"],
        "innate_abilities": ["Equine Build", "Hooves", "Survivor", "Charge", "Nature's Ally"],
        "preferred_classes": ["Fighter", "Druid", "Ranger", "Barbarian"],
        "culture": "Centaur society blends the love of freedom with a deep connection to nature and the lands they inhabit. Living in nomadic tribes, centaurs roam vast plains and forests, living off the land and following the seasons. They are known for their exceptional speed, strength, and wisdom of the natural world, making them unparalleled scouts and formidable in combat.",
        "alignment": [
            "True Neutral",
            "Chaotic Neutral",
            "Neutral Good"
        ],
        "lore": "Centaurs are half-human, half-horse creatures embodying the untamed spirit of nature. They are often found guarding sacred glades, ancient paths, and natural wonders of the world. Despite their somewhat wild appearance, they possess a profound wisdom and a keen understanding of the balance of nature.",
        "physical_characteristics": {
            "Male": {"height": (190, 250), "weight": (400, 600)},
            "Female": {"height": (180, 240), "weight": (350, 550)}
        },
        "male_names": [
            "Aron", "Briar", "Cronus", "Darian", "Efron", "Galen", "Horus", "Icarus", "Jaran", "Kiron",
            "Lorian", "Miron", "Norian", "Orion", "Pyron", "Quiron", "Rion", "Saran", "Theron", "Urian",
            "Varian", "Warron", "Xenon", "Yaron", "Zephyr", "Achilles", "Bellerophon", "Castor", "Damon", "Eros",
            "Felix", "Gideon", "Hector", "Icarus", "Jason", "Kairos", "Lysander", "Mars", "Nestor", "Orpheus",
            "Alden", "Bracken", "Calder", "Dorin", "Eldar", "Faron", "Garrick", "Halen", "Isar", "Joren",
            "Kyron", "Landon", "Morven", "Nestor", "Oberon", "Pellan", "Quentin", "Rolan", "Stefan", "Tyron",
            "Varden", "Wyatt", "Xander", "Yestin", "Zorion"
        ],
        "female_names": [
            "Aella", "Brielle", "Cerelia", "Daphne", "Elara", "Fauna", "Galia", "Helia", "Ianthe", "Jolene",
            "Kyra", "Lorelle", "Mirela", "Nadia", "Orielle", "Phoebe", "Quilla", "Rhea", "Selene", "Talia",
            "Urania", "Vesta", "Wynda", "Xylia", "Yolanda", "Zanthe", "Ariadne", "Briseis", "Cassiopeia", "Danae", "Electra",
            "Fiona", "Gaia", "Hera", "Iris", "Jocasta", "Kalliope", "Leda", "Mnemosyne", "Nyx", "Olympia",
            "Althea", "Bryony", "Callista", "Diana", "Eirene", "Fayre", "Giselle", "Hestia", "Isolde", "Jessa",
            "Kestrel", "Leona", "Melania", "Nerys", "Olena", "Priya", "Quintessa", "Seraphina", "Thalia", "Unity",
            "Valora", "Wynne", "Xena", "Yasmine", "Zelda"
        ]
    },
    "Aasimar": {
        "last_names": [
            "Lightbringer", "Dawncaller", "Starborne", "Moonbeam", "Sunshard", "Heavensent", 
            "Celestine", "Divinesong", "Etherealwing", "Seraphine", "Glowheart", "Skyharbor", 
            "Haloquest", "Radiantbloom", "Aurorawatch", "Daydreamer", "Evershine", "Glimmerfell", 
            "Brightsoul", "Angelglow"
        ],
        "archetypes": ["Protector", "Scourge", "Fallen", "Redeemed", "Emissary", "Divine Agent"],
        "backgrounds": ["Acolyte", "Sage", "Hermit", "Missionary", "Guardian", "Healer"],
        "innate_abilities": ["Healing Hands", "Light Bearer", "Celestial Resistance", "Radiant Soul", "Necrotic Shroud"],
        "preferred_classes": ["Paladin", "Cleric", "Warlock", "Sorcerer"],
        "culture": "Aasimar are born to serve as champions of the gods, often feeling a divine calling to enact the will of their celestial patron. They are raised among humans, standing out as beacons of hope or avatars of divine wrath, depending on their lineage and the nature of their celestial guide. Aasimar work towards promoting good, often becoming leaders or revered figures in the communities they protect.",
        "alignment": [
            "Lawful Good",
            "Neutral Good",
            "Lawful Neutral"
        ],
        "lore": "Aasimars are humans with a significant amount of celestial or other good outsider blood in their heritage. They are descendants of sacred unions between mortals and angels or other celestial beings. Their existence is a testament to the world's inherent goodness, often manifesting when the need for hope and salvation is greatest.",
        "physical_characteristics": {
            "Male": {"height": (165, 200), "weight": (70, 90)},
            "Female": {"height": (160, 195), "weight": (60, 80)}
        },
        "male_names": [
            "Azor", "Cassiel", "Dariel", "Ezra", "Gabriel", "Haniel", "Ithuriel", "Jophiel", "Kemuel", "Loriel",
            "Muriel", "Nathaniel", "Ophiel", "Puriel", "Raziel", "Sariel", "Tamiel", "Uriel", "Vretil", "Zachariel",
            "Zophiel", "Ariel", "Barachiel", "Camael", "Dumah", "Erelim", "Forfax", "Gadreel", "Hadraniel", "Israfel",
            "Amariah", "Benaiah", "Caelum", "Devoriel", "Emmanuel", "Gavreel", "Hadriel", "Immanuel", "Jerahmeel", "Kafziel",
            "Lemuel", "Manoah", "Natanael", "Obadiah", "Peniel", "Quabriel", "Raphael", "Sachiel", "Tzadkiel", "Uziel",
            "Yael", "Zadkiel", "Zerachiel", "Zuriel", "Aziel", "Barchiel", "Cassiel", "Dardiel", "Ezriel", "Gadriel",
        ],
        "female_names": [
            "Ariel", "Bethany", "Cassia", "Dina", "Eliana", "Gabrielle", "Hestia", "Isra", "Jael", "Katriel",
            "Lael", "Mael", "Neria", "Oriel", "Phaedra", "Rael", "Seraphina", "Talia", "Uriela", "Verchiel", "Zephyra",
            "Zuriel", "Aria", "Brielle", "Cassiel", "Dariel", "Ezra", "Gabriel", "Haniel", "Ithuriel", "Jophiel",
            "Anael", "Bethel", "Celestiel", "Darael", "Eliora", "Faith", "Galatea", "Hosanna", "Iriel", "Jophiela",
            "Kezia", "Lysiel", "Maia", "Naomi", "Penina", "Qetesh", "Ruthael", "Shani", "Tzofiya", "Urania",
            "Vesta", "Yofiel", "Zahara", "Zuriela", "Amatiel"
        ]
    },
    "Orc": {
        "last_names": [
            "Doomhammer", "Bloodfist", "Ironjaw", "Skullcrusher", "Stormreaver", "Wolfbrother", 
            "Gorebash", "Ragehowl", "Thunderaxe", "Blacktusk", "Earthshaker", "Bonechewer", 
            "Warbringer", "Grimfang", "Frostwolf", "Nightscream", "Mudsnout", "Rendflesh", 
            "Spiritbinder", "Firetotem"
        ],
        "archetypes": ["Berserker", "War Chief", "Shaman", "Hunter", "Brute", "Marauder"],
        "backgrounds": ["Outlander", "Soldier", "Mercenary", "Tribal Nomad", "Survivor", "Gladiator"],
        "innate_abilities": ["Aggressive", "Powerful Build", "Menacing", "Endurance", "Savage Attacks"],
        "preferred_classes": ["Barbarian", "Fighter", "Ranger", "Druid"],
        "culture": "Orcs live in a world where the strong survive and the strongest lead. Their culture revolves around the strength of their tribes and their connection to the earth and its spirits. Honor and strength are the pillars of orcish identity, with each orc striving to bring glory to their name and their tribe.",
        "lore": "Orcs are often portrayed as fierce warriors and tribal nomads who value strength and honor above all. In many fantasy settings, they are depicted as living in harsh environments, from desolate wastelands to dense, untamed forests, which shapes their resilient and tenacious nature. Orc societies are typically structured around clans or tribes, with a strong emphasis on martial prowess as a key to leadership and respect within the group. Despite their reputation for brutality, orcs possess a rich culture with deep traditions, rituals, and a connection to the natural world, often worshipping gods of war, nature, or tribal ancestry. Orcs are known for their formidable physical strength, endurance, and fierce demeanor, making them exceptional warriors on the battlefield. Their life in challenging terrains contributes to their excellent skills as hunters and trackers, leading many to become Rangers. Some orcs, drawn by a need to prove their strength and valor, venture into the world as Mercenaries or Adventurers, seeking to forge their own legend. Their last names often reflect their attributes or achievements, with names like Ironfist, Wolfcaller, and Stormblade signifying feats of strength, affinity with nature, or prowess in battle.",
        "alignment": [
            "Chaotic Neutral",
            "Chaotic Good",
            "Chaotic Evil"
        ],
        "physical_characteristics": {
            "Male": {"height": (190, 220), "weight": (85, 120)},
            "Female": {"height": (180, 210), "weight": (80, 115)}
        },
        "male_names": [
            "Brug", "Dench", "Feng", "Gell", "Henk", "Keth", "Mhurren", "Ront", "Shump", "Thokk",
            "Varguk", "Yurk", "Zed", "Urok", "Skar", "Rogash", "Nargol", "Krosh", "Gorat", "Drog",
            "Blud", "Crush", "Drak", "Gharn", "Hruth", "Lug", "Murg", "Nob", "Orgh", "Prug",
            "Quark", "Rash", "Snarl", "Torg", "Ugak", "Vrak", "Wrug", "Xog", "Yargh", "Zulgh",
            "Agh", "Brok", "Durth", "Grish", "Holgh", "Krug", "Lok", "Mok", "Nuk", "Pog"
        ],
        "female_names": [
            "Baggi", "Emen", "Engong", "Kansif", "Myev", "Neega", "Ovak", "Shautha", "Vola", "Yevelda",
            "Gruna", "Drenna", "Ungol", "Rishka", "Mog", "Garnak", "Furga", "Bethak", "Aglak", "Zogga",
            "Brog", "Dura", "Ghara", "Grusha", "Holg", "Kraga", "Luta", "Mogga", "Nogga", "Pogga",
            "Argha", "Braga", "Clob", "Draka", "Egh", "Floba", "Grisha", "Hagga", "Irk", "Jez",
            "Klob", "Lurga", "Mokka", "Nagga", "Onga", "Prak", "Quash", "Ragga", "Slog", "Trug",
            "Urga", "Vasha", "Wogga", "Xyga", "Yaga", "Zurga", "Agna", "Bulga", "Dorga", "Golga"
        ]
    },
    "Tiefling": {
        "last_names": [
            "Shadowhorn", "Darkwhisper", "Fellgaze", "Nightwalker", "Sinstalker", "Voidheart", 
            "Crimsonwing", "Hellforge", "Brimstone", "Ashcloak", "Flameveil", "Dreadmire", 
            "Soulfire", "Ironshard", "Grimsmile", "Thornblood", "Ravenlock", "Stormscorn", 
            "Infernobane", "Wraithveil"
        ],
        "archetypes": ["Infernal", "Abyssal", "Rebel", "Outcast", "Sorcerer", "Dark Knight"],
        "backgrounds": ["Charlatan", "Criminal", "Entertainer", "Hermit", "Sage", "Warlock"],
        "innate_abilities": ["Infernal Legacy", "Darkvision", "Hellish Resistance", "Fiendish Charm", "Winged"],
        "preferred_classes": ["Warlock", "Sorcerer", "Rogue", "Bard"],
        "culture": "Tieflings often find themselves on the fringes of society, where their adaptability, resilience, and innate powers carve out niches of influence and survival. Their culture is one of resistance, adaptation, and the search for identity, forging bonds that transcend the typical constraints of race and heritage.",
        "lore": "Tieflings are one of the most fascinating races in fantasy settings, marked by their infernal heritage that grants them distinct features such as horns, tails, and often otherworldly skin colors. This heritage traces back to a pact made generations ago, imbuing them with the essence of the lower planes. Despite the prejudices they face, Tieflings are far from monolithic; they are as diverse in personality and alignment as any human, elf, or dwarf. Their infernal ancestry provides them with unique abilities, often making them naturally inclined towards arcane arts. Tieflings carry the weight of their lineage with a mix of pride and sorrow, navigating a world that views them with suspicion and fear. Yet, many use their innate abilities to challenge those prejudices, becoming powerful Warlocks, enchanting Bards, or even cunning Rogues. They often adopt names that reflect their complex nature, a blend of darkness and light, such as Shadowhorn, Darkwhisper, or Soulfire. Their backgrounds are as varied as their appearances; some embrace the chaos of their ancestry as Rebels or Charlatans, while others seek to rise above their demonic ties, striving for heroism or even sanctity. The life of a Tiefling is one of contradiction, caught between two worlds, and it is this struggle that defines their most compelling stories.",
        "alignment": [
            "Lawful Evil",
            "Neutral Evil",
            "Chaotic Good",
            "Chaotic Neutral",
            "True Neutral"
        ],
        "physical_characteristics": {
            "Male": {"height": (170, 200), "weight": (70, 90)},
            "Female": {"height": (160, 190), "weight": (60, 80)}
        }, 
        "male_names": [
            "Akmenos", "Amnon", "Barakas", "Damakos", "Ekemon", "Iados", "Kairon", "Leucis", "Melech", "Mordai",
            "Pelaios", "Skamos", "Therai", "Zepar", "Caim", "Rahab", "Abaddon", "Baaz", "Cimer",
            "Deimos", "Exodus", "Focalor", "Haures", "Iados", "Kasdeya", "Leraje", "Mammon", "Naberius", "Oriax",
            "Paimon", "Raum", "Sabnock", "Tenebrous", "Uvall", "Vassago", "Xaphan", "Zepar",
            "Draeth", "Fenriz", "Gorion", "Havoc", "Jarlaxle", "Korvus", "Lazarus", "Malik", "Nero", "Osric",
            "Pyre", "Quintus", "Raziel", "Samael", "Talon", "Umbra", "Vexx", "Wyrm", "Xanxus", "Yorick",
            "Zephyros", "Astaroth", "Baal", "Carn", "Draven", "Erebus", "Furion", "Grim", "Hex", "Israfel",
            "Jago", "Kazan", "Lucien", "Malthus", "Noctis", "Orpheus", "Prosper", "Rune", "Strife", "Torment"
        ],
        "female_names": [
            "Akta", "Anakis", "Bryseis", "Criella", "Damaia", "Ea", "Kallista", "Lerissa", "Makaria", "Nemeia",
            "Orianna", "Phelaia", "Rieta", "Synoria", "Thela", "Uzza", "Verrona", "Zarya", "Arioch", "Ravyn",
            "Amon", "Baal", "Caim", "Dagon", "Eligos", "Furcas", "Geryon", "Halphas", "Ipos", "Kasdeya",
            "Leraje", "Mammon", "Naberius", "Oriax", "Paimon", "Raum", "Sabnock", "Tenebrous", "Uvall", "Vassago",
            "Azura", "Bast", "Circe", "Desdemona", "Elysia", "Faustina", "Griselda", "Hecate", "Isolde", "Jinx",
            "Karma", "Lilith", "Morrigan", "Nyx", "Ophelia", "Persephone", "Qadira", "Ravana", "Sorsha", "Tamsin",
            "Undine", "Vesper", "Wysteria", "Xanthe", "Ysolde", "Zephyra", "Acantha", "Belladonna", "Calypso",
            "Drusilla", "Echo", "Fae", "Galatea", "Havannah", "Ianthe", "Jubilee", "Kestrel", "Lucinda", "Miranda",
            "Narcissa", "Octavia", "Pandora", "Quintessa", "Rosalind", "Selene", "Thalassa", "Urania", "Venetia",
            "Winona", "Xylia", "Yasmine", "Zelda"
        ]
    },
    "Kenku": {
        "last_names": [
            "Silentwhisper", "Darkquill", "Shadowcloak", "Nightraven", "Mimicbeak", "Echofeather",
            "Thiefwing", "Crowshroud", "Rookshadow", "Whisperflight", "Blackplume", "Gloombeak",
            "Hoarsecaller", "Mockingbird", "Nightchatter", "Ravenwatch", "Sablefeather", "Trickstertalon",
            "Vagabondwing", "Windstealer"
        ],
        "archetypes": ["Rogue", "Bard", "Trickster", "Shadow", "Mimic"],
        "backgrounds": ["Urchin", "Charlatan", "Criminal", "Spy", "Entertainer"],
        "innate_abilities": ["Mimicry", "Expert Forgery", "Stealthy"],
        "preferred_classes": ["Rogue", "Bard", "Ranger"],
        "culture": "Kenku form secretive communities in urban environments. Their society is one of necessity and survival, often turning to organized crime or serving as mercenaries. They communicate through an intricate system of mimicked sounds and are known for their ability to replicate any noise, voice, or music they've heard.",
        "lore": "Kenku are a fascinating race found in many fantasy settings, particularly noted in Dungeons & Dragons for their unique characteristics and lore. These crow-like humanoids are cursed to lack creative vision and the ability to speak in their own voices. Instead, they can perfectly mimic any sound they hear, including voices and noises, which they use to communicate. Historically, Kenku were servants of a powerful, unnamed deity, from whom they stole and were thus cursed with their current form and limitations. They are often found in urban settings, working in the underbelly of society due to their innate skills in stealth and mimicry. Kenku are typically drawn to professions that make use of their dexterity and stealth, such as thieves and scouts, but their skill in mimicry also makes them excellent spies. Despite their curse, many Kenku aspire to flight, a freedom they were stripped of, and they often seek magical means to achieve this lost ability. Their society is built around tight-knit communities where they rely on each other's strengths to survive, often led by a Kenku with a particularly cunning mind or an exceptional talent for strategy.",
        "alignment": [
            "Neutral Evil",
            "Neutral Good",
            "Lawful Neutral",
            "Chaotic Neutral",
            "True Neutral"
        ],
        "physical_characteristics": {
            "Male": {"height": (150, 160), "weight": (45, 55)},
            "Female": {"height": (145, 155), "weight": (40, 50)}
        },
        "male_names": [
            "Clink", "Flicker", "Murmur", "Rattle", "Scribble", "Twitch", "Whisper", "Zik", "Bleak", "Drifter",
            "Echo", "Gloom", "Nimble", "Quill", "Shadow", "Vex", "Click", "Dash", "Jinx", "Rustle", "Smudge", "Tinker",
            "Wisp", "Clatter", "Flick", "Mumble", "Raven", "Scrawl", "Twitch", "Whistle", "Zephyr",
            "Gust", "Sneer", "Frost", "Mirth", "Preen", "Sable", "Cobble", "Nicker", "Prattle", "Skitter",
            "Wheeze", "Bramble", "Grift", "Plume", "Scrape", "Veil", "Chitter", "Fawn", "Glint", "Loam",
            "Ripple", "Squall", "Thicket", "Barb", "Crest", "Dew", "Gaze", "Haze", "Knack", "Lurch",
            "Maze", "Prowl", "Scorch", "Trickle", "Wisp", "Brink", "Crackle", "Fleet", "Glitch", "Loom",
        ],
        "female_names": [
            "Breeze", "Chirr", "Flutter", "Piper", "Raven", "Serene", "Twinkle", "Wisp", "Crest", "Dapple",
            "Glimmer", "Mottle", "Patch", "Speckle", "Tally", "Veer", "Whirl", "Blend", "Fleet", "Mingle", "Prism", "Sway", "Thread",
            "Blink", "Briar", "Coil", "Dusk", "Ember", "Flick", "Gale", "Hush", "Iris", "Jewel", "Kite", "Lace",
            "Meadow", "Nectar", "Orchid", "Plum", "Quest", "Rose", "Silk", "Tide", "Umber", "Violet",
            "Willow", "Xenon", "Yarrow", "Zenith", "Aria", "Beryl", "Clover", "Dawn", "Echo", "Fern",
            "Glimpse", "Harbor", "Ivory", "Jade", "Kismet", "Lotus", "Marble", "Nova", "Opal", "Pearl",
            "Quartz", "Reed", "Sapphire", "Tulip", "Unity", "Velvet", "Winter", "Xylo", "Yucca", "Zephyr"
        ]
    },
    "Goliath": {
        "last_names": [
            "Peakstrider", "Mountainheart", "Bouldercrush", "Thunderfist", "Stonebreaker", "Frostkeeper",
            "Cliffwalker", "Ridgehunter", "Summitborn", "Skybreaker", "Earthwielder", "Cragjumper",
            "Snowstrider", "Rockbinder", "Galeforce", "Tundrastrider", "Highpeak", "Cloudchaser",
            "Glaciermover", "Stormcaller"
        ],
        "archetypes": ["Warrior", "Guardian", "Berserker", "Stone's Endurance"],
        "backgrounds": ["Outlander", "Soldier", "Athlete", "Mountain Guide"],
        "innate_abilities": ["Powerful Build", "Mountain Born", "Stones Endurance", "Natural Athlete"],
        "preferred_classes": ["Barbarian", "Fighter", "Paladin"],
        "culture": "Goliath society is competitive, with a focus on individual achievement and tribal survival. They have a deep respect for nature and the elements, often invoking them in rituals and naming conventions. Goliaths live in small, nomadic tribes that roam the mountainous terrains, hunting and foraging for food.",
        "alignment": ["Lawful Neutral", "Lawful Good", "Neutral"],
        "lore": "Goliaths are seen as the embodiment of the raw power and majesty of the mountains they call home. They are born survivors, capable of enduring physical hardships that would fell lesser beings. Their society is structured around challenges and trials to prove one's worth and gain status within the tribe.",
        "physical_characteristics": {
            "Male": {"height": (210, 250), "weight": (140, 200)},
            "Female": {"height": (200, 240), "weight": (130, 190)}
        },
        "male_names": [
            "Gauthak", "Keothi", "Muthar", "Nalla", "Orilo", "Paavu", "Raavak", "Thalai", "Uthal", "Vaunea",
            "Waukeen", "Aukan", "Eglath", "Gae-Al", "Ilikan", "Kavaki", "Lo-Kag", "Manneo", "Noke", "Pethani", "Thotham",
            "Thuli", "Uthal", "Vatavi", "Voren", "Zethaya", "Aram", "Bael", "Borivik", "Fodel", "Glar", "Grigor", "Igan",
            "Ivor", "Kosef", "Mival", "Orel", "Pavel", "Sergor", "Darvin", "Dorn", "Evendur", "Gorstag", "Grim", "Helm",
            "Barakas", "Crag", "Durnn", "Harbek", "Kraval", "Mog", "Orsik", "Rurik", "Shamash", "Tagak",
            "Volibar", "Yorak", "Zed", "Arrok", "Brogg", "Drang", "Gurnn", "Korag", "Lunn", "Morak", "Narak", "Prug", "Rogath", "Skamak", "Truk"

        ],
        "female_names": [
            "Gaiath", "Katho-Olavi", "Manneo", "Ovak", "Sutha", "Thalai", "Uthal", "Vadoola", "Waimo", "Yuldra",
            "Auta", "Elan", "Faeda", "Galia", "Hilo", "Kana", "Lago", "Maru", "Nari", "Ooli", "Pani", "Rue",
            "Sutha", "Thola", "Vola", "Yevelda", "Zetha", "Bertha", "Dalka", "Eskar", "Frida", "Gretta", "Harika", "Inka", "Jeska", "Kala", "Letha",
            "Marni", "Nala", "Olga", "Peka", "Ragna", "Sigrid", "Torka", "Ursa", "Valka", "Wilka", "Xylia", "Yrsa", "Zara"
        ]
    },
    "Aarakocra": {
        "last_names": [
            "Windtalon", "Skysoar", "Featherfall", "Highnest", "Stormwing", "Cloudcircler", "Galeclaw",
            "Sunfeather", "Thunderswoop", "Skywatch", "Breezeglider", "Lightwing", "Airdiver", "Winddancer",
            "Stormchaser", "Nestbuilder", "Skyshriek", "Horizonwatcher", "Featherdance", "Cloudsinger"
        ],
        "archetypes": ["Skywarden", "Windwalker", "Sorcerer of the Sky", "Elemental Adept"],
        "backgrounds": ["Explorer", "Hermit", "Scout", "Messenger"],
        "innate_abilities": ["Flight", "Talon Strikes", "Wind Manipulation", "Keen Senses"],
        "preferred_classes": ["Ranger", "Monk", "Druid", "Sorcerer"],
        "culture": "Aarakocra society is highly communal and deeply connected to the sky and wind. They build their homes in high mountain nests or cliff-side structures, rarely touching the ground. Aarakocra are known for their close-knit family units and tribal communities, with a strong emphasis on aerial agility and freedom.",
        "alignment": ["Neutral Good", "Lawful Good", "True Neutral", "Chaotic Good"],
        "lore": "Originating from the Elemental Plane of Air, Aarakocra are avian humanoids who embody the freedom of the skies. They are messengers, scouts, and guardians of the upper reaches of the world. With their ability to fly, Aarakocra have a unique perspective on the world below and a natural inclination to explore the horizons.",
        "physical_characteristics": {
            "Male": {"height": (150, 180), "weight": (45, 60)},
            "Female": {"height": (145, 175), "weight": (40, 55)}
        },
        "male_names": [
            "Aera", "Cawth", "Eerek", "Gawain", "Kraw", "Perraw", "Quaf", "Rook", "Swoop", "Talon",
            "Vreek", "Wraw", "Zephyr", "Bront", "Darr", "Flink", "Jarak", "Lirr", "Mott", "Naw", "Perrit", "Rill",
            "Sark", "Tarr", "Varr", "Warr", "Zarr", "Breez", "Dawn", "Flit", "Jentil", "Lori", "Melli", "Norri",
            "Blaze", "Cyclon", "Drift", "Feather", "Glide", "Horizon", "Jet", "Kestrel", "Mistral", "Nester", 
            "Ornis", "Peregrine", "Quill", "Skyler", "Thermal", "Upwind", "Ventus", "Whirl", "Xanto", "Yarak", 
            "Zonda", "Avis", "Birrus", "Cirro", "Duul", "Eurus", "Frey", "Gale", "Hawk", "Icarus"
        ],
        "female_names": [
            "Auri", "Cirri", "Ellai", "Kirri", "Merla", "Prill", "Sarai", "Thri", "Valli", "Yara",
            "Zelli", "Breez", "Dawn", "Flit", "Jentil", "Lori", "Melli", "Norri", "Piri", "Renn", "Skai", "Tilli",
            "Venn", "Wrenn", "Zenn", "Birra", "Cirra", "Dara", "Eira", "Fira", "Gira", "Hira", "Iira", "Jira",
            "Kira", "Lira", "Mira", "Nira", "Oira", "Pira", "Rira", "Sira", "Tira", "Vira", "Wira", "Xira", "Yira", "Zira"
            "Aquila", "Breeze", "Cloudia", "Dew", "Eos", "Fayra", "Gliss", "Halo", "Iris", "Joy", 
            "Kestra", "Luna", "Mist", "Nimbus", "Orielle", "Penna", "Quila", "Raine", "Sora", "Tula", 
            "Ula", "Vesper", "Windia", "Xyra", "Yolanda", "Zephyrette", "Alize", "Brook", "Celeste", "Dara"
        ]
    },
    "Triton": {
        "last_names": [
            "Waveheart", "Seastorm", "Deepfin", "Marinerider", "Tideseeker", "Oceanblade",
            "Coralkeeper", "Foamwhisper", "Abysswalker", "Saltbreeze", "Tidebinder", "Waterveil",
            "Seaborn", "Aquawarden", "Galefin", "Stormsurge", "Depthstrider", "Squallchaser",
            "Reefguard", "Maelstromfury"
        ],
        "archetypes": ["Guardian of the Depths", "Wave Speaker", "Sea Knight", "Aquatic Adept"],
        "backgrounds": ["Guardian", "Explorer", "Mariner", "Noble"],
        "innate_abilities": ["Control Air and Water", "Amphibious", "Guardians of the Depths", "Aquatic Adaptation"],
        "preferred_classes": ["Paladin", "Sorcerer", "Warlock", "Fighter"],
        "culture": "Triton society is deeply intertwined with the ocean's mysteries and majesty. Living in underwater cities, they see themselves as the protectors of the sea and all its creatures. Tritons are noble and take their self-appointed roles as guardians against the threats from the depths seriously. They value honor, prowess in battle, and the ability to navigate and understand the vast and mysterious ocean.",
        "alignment": [
            "Lawful Good",
            "Neutral Good",
            "Lawful Neutral"
        ],
        "lore": "Hailing from the Elemental Plane of Water, Tritons ventured into the Material Plane to combat ancient evils lurking beneath the waves. Over the centuries, they adapted to life in the ocean's depths, often unseen by land-dwelling creatures. Their existence is a testament to their success in keeping malevolent undersea forces at bay, though they remain vigilant and ever-ready to face emerging threats.",
        "physical_characteristics": {
            "Male": {"height": (160, 190), "weight": (70, 90)},
            "Female": {"height": (155, 185), "weight": (65, 85)}
        },
        "male_names": [
            "Corus", "Delnis", "Jassan", "Keros", "Lorvis", "Molos", "Nalos", "Orius", "Pelias", "Rhorlis",
            "Thalor", "Vulmar", "Zephos", "Aldain", "Borak", "Cyrill", "Drakon", "Eldar", "Folmon", "Grius",
            "Halos", "Ildar", "Joros", "Kaldor", "Lorak", "Meldar", "Nalos", "Orius", "Peldar", "Rilos", "Thalos",
            "Glaucus", "Hali", "Idas", "Jelani", "Kai", "Lir", "Marlin", "Nereus", "Oceanus", "Poseidon", 
            "Qalir", "Rin", "Seaton", "Tritus", "Ulaan", "Varun", "Wavir", "Xebel", "Yul", "Zale", 
            "Aegir", "Brizo", "Ceto", "Dorado", "Euron", "Finley", "Galen", "Huracan", "Ianthe", "Jona"
        ],
        "female_names": [
            "Amatheia", "Beloril", "Cerissa", "Dione", "Eunalee", "Galene", "Ianira", "Kyma", "Lysianassa", "Melite",
            "Nerites", "Oceana", "Pelagia", "Rhanope", "Thetis", "Vellamo", "Zephyra", "Acantha", "Brisa", "Calissa",
            "Anahita", "Beryl", "Coralia", "Delmare", "Elysia", "Firtha", "Galia", "Hestia", "Ione", "Jinna", 
            "Kailani", "Leucothea", "Maera", "Naiad", "Ondina", "Pavati", "Qyra", "Rinna", "Seraphine", "Talia", 
            "Undine", "Venus", "Wynne", "Xylia", "Ysel", "Zisa", "Aqua", "Bay", "Cyma", "Doris"
        ]
    },
    "Firbolg": {
        "last_names": [
            "Treewalker", "Mossbeard", "Leafshade", "Grovekeeper", "Forestfriend", "Timberwatch",
            "Meadowroamer", "Branchwhisper", "Thicketborn", "Greenwarden", "Woodshaper", "Ferncomber",
            "Sylvanstream", "Rootsinger", "Pinebender", "Hillstrider", "Valleydreamer", "Brookwatcher",
            "Dewgatherer", "Stonecarver"
        ],
        "archetypes": ["Druid", "Cleric", "Ranger", "Peacekeeper", "Guardian", "Sage"],
        "backgrounds": ["Hermit", "Outlander", "Sage", "Acolyte", "Guardian of the Forest", "Keeper of Traditions"],
        "innate_abilities": ["Firbolg Magic", "Hidden Step", "Powerful Build", "Speech of Beast and Leaf", "Detect Magic", "Disguise Self"],
        "preferred_classes": ["Druid", "Cleric", "Ranger"],
        "culture": "Firbolg society is deeply connected to nature and the forests they call home. They live in small, tight-knit communities that are hidden away from the rest of the world, often acting as stewards and protectors of the woodland realms. Firbolgs are peaceful and reclusive, preferring to avoid conflict when possible. They have a profound respect for all living things, practicing a lifestyle that is in harmony with the natural order.",
        "alignment": ["Neutral Good", "Lawful Good", "True Neutral", "Chaotic Good"],
        "lore": "Firbolgs are gentle giants among the fey, embodying the spirit of the primeval forests. Their origins are shrouded in mystery, believed to be blessings from the gods of nature themselves. Firbolgs possess an innate connection to the magic of the land, allowing them to blend in with their surroundings and communicate with plants and animals. They are seldom seen by outsiders, as they use their abilities to remain hidden, only emerging when their homes are threatened or to help those in dire need.",
        "physical_characteristics": {
            "Male": {"height": (210, 250), "weight": (125, 150)},
            "Female": {"height": (205, 245), "weight": (120, 145)}
        },
        "male_names": [
            "Ardan", "Beothain", "Caelum", "Darragh", "Eoghan", "Faolan", "Gareth", "Haran", "Iarfhlaith", "Jaran",
            "Keenan", "Lorcan", "Muireadhach", "Nuadha", "Oisin", "Peadar", "Quinlan", "Ronan", "Seamus", "Turlough",
            "Uilliam", "Viggo", "Wynne", "Xander", "Yorath", "Zephyrus", "Ailill", "Bran", "Cormac", "Dermot", "Eoin",
            "Bran", "Conall", "Diarmuid", "Eunan", "Fergal", "Gallagher", "Hugh", "Ian", "Kieran", "Lugh",
            "Mannix", "Niall", "Ollie", "Phelan", "Ruarc", "Sullivan", "Torin", "Uisdean", "Vincent", "Wyatt",
            "Xander", "Yarin", "Zephyr", "Ailill", "Bran", "Cormac", "Dermot", "Eoin", "Finn", "Gallagher", "Hugh",
        ],
        "female_names": [
            "Aine", "Briona", "Caoimhe", "Dearbhla", "Eimhear", "Fionnuala", "Grainne", "Iseult", "Liadan", "Maebh",
            "Niamh", "Orlaith", "Pegeen", "Riona", "Saoirse", "Tuilelaith", "Una", "Velora", "Wynne", "Yseult",
            "Zephyra", "Aisling", "Brianna", "Caitriona", "Dervla", "Eithne", "Fidelma", "Grainne", "Iseult", "Jocelyn",
            "Kathleen", "Laoise", "Maeve", "Nuala", "Oonagh", "Peggy", "Roisin", "Saoirse", "Teagan", "Una", "Vevila",
            "Xanthe", "Yseult", "Zephyra", "Ailbhe", "Blathnaid", "Caoimhe", "Dervla", "Eibhlin", "Fionnghuala",
            "Gormlaith", "Honor", "Iseult", "Jocelyn", "Kathleen", "Laoise", "Maeve", "Nuala", "Oonagh", "Peggy",
            "Aisling", "Blathnaid", "Ciara", "Deirdre", "Enya", "Finola", "Gobnait", "Honora", "Iona", "Joan",
            "Keira", "Lilis", "Morna", "Neasa", "Onora", "Pronncha", "Roisin", "Sibeal", "Talulla", "Ula",
            "Viona", "Wren", "Xyla", "Yanna", "Zelda"
        ]
    },
    "Tabaxi": {
        "last_names": [
            "Nightwhisker", "Silentpaw", "Swifttail", "Moonshadow", "Jadegaze", "Suntreader",
            "Windclimber", "Startracker", "Rainfinder", "Cloudleaper", "Dawndancer", "Frostfur",
            "Thundersneak", "Riverstride", "Flamestalker", "Duskrunner", "Skygazer", "Sunspot",
            "Mistymane", "Wildchaser"
        ],
        "archetypes": ["Rogue", "Bard", "Ranger", "Explorer", "Scout", "Thief"],
        "backgrounds": ["Charlatan", "Entertainer", "Outlander", "Sailor", "Smuggler", "Wanderer"],
        "innate_abilities": ["Feline Agility", "Cat's Claws", "Cat's Talent", "Darkvision", "Keen Smell"],
        "preferred_classes": ["Rogue", "Bard", "Ranger"],
        "culture": "Tabaxi culture is one of curiosity and wanderlust, driving them to explore beyond their native tropical or subtropical homelands. They are storytellers and collectors, often gathering tales and trinkets from their travels. Tabaxi communities are loose-knit, with each individual pursuing their own path of discovery, though they share their stories and knowledge with kin upon returning. Their society places great value on personal growth and the pursuit of knowledge.",
        "alignment": ["Chaotic Good", "Neutral Good", "Chaotic Neutral"],
        "lore": "Tabaxi roam the vast world with insatiable curiosity, driven by their quest for stories, treasures, and experiences. Their agility and stealth, combined with keen senses, make them exceptional hunters and explorers. Originating from realms lush and vibrant, Tabaxi adapt quickly to various environments, making them versatile and unpredictable adventurers.",
        "physical_characteristics": {
            "Male": {"height": (165, 195), "weight": (70, 90)},
            "Female": {"height": (160, 190), "weight": (65, 85)}
        },
        "male_names": [
            "Cloud on the Mountaintop", "Five Thunder", "Jaguar in the Night", "Obsidian Claw", "Quick Strike",
            "River That Sings", "Silent Step", "Twilight Hunter", "Wind in the Leaves", "Zephyr of the Canyon",
            "Moonlit Jungle", "Rapid River", "Serpent's Shadow", "Starlight Wanderer", "Whispering Wind",
            "Frost on the Fern", "Lightning Before Thunder", "Painted Sky", "Hidden Prowler", "Laughing Brook",
            "Breeze Through Reed", "Dusk on the Horizon", "Ember in the Darkness", "Flicker of the Flame", "Gleam Under Moon",
            "Mist on the Mountain", "Pebble in the Pond", "Pine in the Forest", "Rain on the Roof", "Ripple in the Water",
        ],
        "female_names": [
            "Autumn Fire", "Dancing Leaf", "Echoing Whisper", "Golden Sunbeam", "Lunar Reflection",
            "Morning Dew", "Rain on the River", "Shimmering Water", "Snowy Mountain", "Sunset Horizon",
            "Crimson Leaf", "Fleeting Fox", "Harvest Moon", "Night's Embrace", "Opal of the Stream",
            "Pearl of the Depths", "Quiet Meadow", "Radiant Dawn", "Sapphire Glint", "Tranquil Garden",
            "Blossom in the Night", "Dewdrop Under Starlight", "Glimmering Shard", "Mist on the Mountain", "Whirlwind's Dance",
            "Whispering Willow", "Dancing Flame", "Gentle Breeze", "Luminous Echo", "Mystic River",
            
        ]
    },
    "Lizardfolk": {
        "last_names": [
            "Mudsnout", "Scaleback", "Sharptooth", "Brightcrest", "Swifttail", "Longclaw",
            "Darkwater", "Sundew", "Ridgehunter", "Marshstalker", "Cragbiter", "Fenstrider",
            "Gatorjaw", "Tidalsnapper", "Reedwhistler", "Stormscale", "Dunewalker", "Siltseeker",
            "Rivermaw", "Thornhide"
        ],
        "archetypes": ["Shaman", "Druid", "Fighter", "Hunter", "Survivalist", "Warrior"],
        "backgrounds": ["Outlander", "Hermit", "Swamp Dweller", "Tribal Nomad", "Hunter-Gatherer", "Shaman's Apprentice"],
        "innate_abilities": ["Bite", "Cunning Artisan", "Hold Breath", "Hunter's Lore", "Natural Armor", "Hungry Jaws"],
        "preferred_classes": ["Druid", "Fighter", "Ranger"],
        "culture": "Lizardfolk communities are deeply integrated with their swampy, riverine, or coastal environments. They possess a pragmatic mindset, viewing the world through a lens of survival and utility. Lizardfolk culture is less about tradition or history and more about the practical aspects of life: hunting, crafting, and the symbiotic relationship with their surroundings. Emotions are considered a curiosity, as Lizardfolk primarily operate on instinct and logic.",
        "alignment": ["True Neutral", "Neutral Good", "Neutral Evil"],
        "lore": "Lizardfolk are reptilian humanoids who live in close harmony with nature, often misunderstood by other races due to their emotional detachment and survival-driven lifestyle. They are skilled hunters and crafters, making use of everything their environment offers. While they might seem cold or indifferent, Lizardfolk have their own complex societies and beliefs, deeply respecting the balance of nature.",
        "physical_characteristics": {
            "Male": {"height": (170, 220), "weight": (80, 120)},
            "Female": {"height": (160, 210), "weight": (70, 110)}
        },
        "male_names": [
            "Ssath", "Krex", "Zissk", "Throden", "Sesk", "Hessk", "Geth", "Xiss", "Othokent", "Ssark",
            "Sseth", "Vess", "Zess", "Dess", "Hissk", "Issk", "Jesk", "Kess", "Liss", "Moss", "Ness",
            "Oss", "Pess", "Qess", "Ress", "Ssiss", "Tess", "Wess", "Xess", "Yess","Marrash", "Keth", "Yarss", "Vrak", "Tessk", "Jurk", "Grassk", "Drath", "Crask", "Brassk",
            "Athiss", "Drazz", "Jhank", "Lurr", "Mossk", "Narssk", "Orrik", "Pessk", "Rassk", "Surk", "Tessk", "Vrassk", "Wessk", "Xissk", "Yarssk", "Zessk"

        ],
        "female_names": [
            "Shirish", "Kessessek", "Tliss", "Ssila", "Chath", "Dasss", "Hisswa", "Sslith", "Thessik", "Vess",
            "Zess", "Dess", "Hissk", "Issk", "Jesk", "Kess", "Liss", "Moss", "Ness", "Oss", "Pess", "Qess",
            "Issra", "Jhess", "Kassa", "Lethiss", "Mishka", "Niss", "Othess", "Plesk", "Qiss", "Riss",
            "Sassa", "Thiss", "Ussk", "Vessisk", "Wasska", "Xess", "Yith", "Zess", "Assik", "Cress"
        ]
    },
    "Yuan-ti Pureblood": {
        "last_names": [
            "Scalesinger", "Venomtongue", "Coilbinder", "Fangcaller", "Slitherscale", "Darkwhisper",
            "Viletouch", "Serpentbrow", "Nightcoil", "Poisonveil", "Scaleweaver", "Deathhiss",
            "Gloomfang", "Shadowscale", "Dreadsworn", "Vipereye", "Silentstrike", "Bloodserpent",
            "Plaguewinder", "Swiftslither"
        ],
        "archetypes": ["Sorcerer", "Warlock", "Cleric", "Infiltrator", "Spy", "Assassin"],
        "backgrounds": ["Cultist", "Noble", "Spy", "Scholar of the Ancient", "Infiltrator", "Agent of Chaos"],
        "innate_abilities": ["Innate Spellcasting", "Magic Resistance", "Poison Immunity", "Suggestion", "Animal Friendship (snakes only)"],
        "preferred_classes": ["Sorcerer", "Warlock", "Cleric"],
        "culture": "Yuan-ti Purebloods are part of the Yuan-ti society, a secretive and manipulative group that seeks to gain power and influence. They blend easily into human societies to further their own ends. Yuan-ti value cunning, intelligence, and magical prowess, often engaging in complex plots to achieve their goals.",
        "alignment": ["Neutral Evil", "Lawful Evil", "Chaotic Evil"],
        "lore": "Yuan-ti Purebloods are the result of ancient humanoids merging with snakes, creating a race that retains much of their human appearance with subtle serpentine features. They are the most human-like of the Yuan-ti, used as agents in the world above their subterranean cities.",
        "physical_characteristics": {
            "Male": {"height": (170, 180), "weight": (70, 80)},
            "Female": {"height": (160, 170), "weight": (60, 70)}
        },
        "male_names": [
            "Ssessar", "Xalthis", "Zessith", "Hiss'ir", "Ssyrin", "Yths", "Merssos", "Sseth", "Vyr", "Zyss",
            "Niss'ir", "Thyss", "Zar'ith", "Rassas", "Hethiss", "Ssath", "Dythis", "Vessis", "Kyriss", "Issar",
            "Rhess", "Mythas", "Nythir", "Ssiv", "Vyth", "Zress", "Ossar", "Jyth", "Qyss", "Liss", "Ssyr",
            "Ssith",
        ],
        "female_names": [
            "Ssathala", "Yszalla", "Tsiyara", "Essreth", "Issrana", "Xalyth", "Zessire", "Ssyrith", "Ythssine", "Vessyth",
            "Ithress", "Nysyra", "Thissina", "Essyra", "Rysyra", "Vysara", "Systa", "Zyssara", "Athissa", "Lythi",
            "Dyssira", "Sythra", "Hyssana", "Wysara", "Qyssina", "Tysara", "Ulyssa", "Fyssara", "Jyssina", "Kyssara",
            "Lysara", "Ssithra", "Ssathara", "Ssyrana", "Ssithra", "Ssathara", "Ssyrana"
        ]
    },
    "Satyr": {
        "last_names": [
            "Leafstrider", "Vineheart", "Thicketplay", "Mirthbranch", "Grovefellow", "Bramblebeard",
            "Fernhoof", "Meadowprance", "Piperoot", "Songwood", "Dewdance", "Thornwhistle",
            "Riverskip", "Breezefoot", "Mossantler", "Wildrun", "Honeywhisk", "Foamleap",
            "Brookjump", "Caskthumper"
        ],
        "archetypes": ["Bard", "Rogue", "Trickster", "Fey Wanderer"],
        "backgrounds": ["Entertainer", "Outlander", "Charlatan", "Folk Hero"],
        "innate_abilities": ["Magic Resistance", "Ram", "Mirthful Leaps", "Reveler"],
        "preferred_classes": ["Bard", "Rogue", "Druid"],
        "culture": "Satyrs embody the spirit of freedom, revelry, and connection to nature. They live in the moment, making music, feasting, and wandering the forests. Satyr communities are loose associations of friends and family who gather for celebration and support.",
        "alignment": ["Chaotic Good", "Neutral Good", "Chaotic Neutral"],
        "lore": "Originating from the Feywild, Satyrs are fey creatures known for their goat-like lower bodies, love of music, and insatiable desire for pleasure. They are often found in the company of other fey, celebrating the wild beauty of nature.",
        "physical_characteristics": {
            "Male": {"height": (160, 180), "weight": (60, 80)},
            "Female": {"height": (155, 175), "weight": (55, 75)}
        },
        "male_names": [
            "Cyrion", "Dionysos", "Euneos", "Faunus", "Glaucus", "Hylas", "Iacchus", "Krotos", "Lysios", "Marsyas",
            "Nysios", "Orpheus", "Pholus", "Rhoikos", "Silvanus", "Tityrus", "Vilinos", "Xantheus", "Zephyrus",
            "Panos", "Aristaeus", "Euros", "Leandros", "Melanthios", "Theron", "Calix", "Dion", "Eryx", "Galenos",
            "Iphis", "Kydon", "Lykos", "Nikias", "Orestes", "Pyrrhos", "Seilenos", "Thyrsos", "Zenon", "Aeson",
            "Bacchus", "Eurys", "Glykon", "Iakchos", "Korax", "Lampros", "Makarios", "Narkissos", "Oinopion", "Pylades",
        ],
        "female_names": [
            "Acantha", "Bacchante", "Carya", "Daphne", "Eudora", "Ianthe", "Kalypso", "Melaina", "Naiad", "Oread",
            "Pheres", "Rhea", "Syrinx", "Thalia", "Xanthe", "Yalena", "Zephyra", "Aella", "Beroe", "Circe","Beroe", "Dione", "Elaini", "Galene", "Helike", "Ismene", "Kleio", "Melita", "Nessa", "Othreis",
            "Phoebe", "Rhode", "Selene", "Theia", "Xene", "Zelene", "Chloe", "Daphnis", "Erato", "Ianira", "Kallisto",
            "Lamia", "Melia", "Nephele", "Oinone", "Pallas", "Rheia", "Semele", "Thetis", "Xanthe", "Ylva", 
        ]
    },
    "Warforged": {
        "last_names": [
            "Shieldbearer", "Swordarm", "Geargrind", "Ironstride", "Steelshaper", "Cogspinner",
            "Anvilheart", "Forgefire", "Pistonpunch", "Battleguard", "Marchforge", "Rivetclasp",
            "Platemender", "Wirewoven", "Treadsprint", "Hammerfist", "Axleturn", "Steamheart",
            "Boltbracer", "Circuitmind"
        ],
        "archetypes": ["Guardian", "Soldier", "Scout", "Artificer"],
        "backgrounds": ["Soldier", "Mercenary Veteran", "Smith", "Sage"],
        "innate_abilities": ["Integrated Protection", "Constructed Resilience", "Sentry's Rest", "Specialized Design"],
        "preferred_classes": ["Fighter", "Paladin", "Artificer", "Wizard"],
        "culture": "Warforged were created as soldiers for a war that has since ended. Now free, they seek purpose and a place in the world. Warforged communities are rare, often forming around shared goals or created families rather than traditional societal structures.",
        "alignment": ["True Neutral", "Lawful Good", "Chaotic Good", "Neutral Evil", "Lawful Neutral", "Chaotic Neutral"],
        "lore": "Warforged are sentient constructs created through powerful magic and artifice. Originally built for battle, they are now autonomous beings with the freedom to shape their destinies and explore their newly found individuality.",
        "physical_characteristics": {
            "Male": {"height": (180, 220), "weight": (100, 300)},
            "Female": {"height": (180, 220), "weight": (100, 300)}
        },
        "male_names": [
            "Anchor", "Bastion", "Cutter", "Drift", "Echo", "Forge", "Grim", "Helix", "Iron", "Javelin",
            "Knave", "Lock", "Mace", "Noble", "Onyx", "Pike", "Quartz", "Rivet", "Slate", "Tower",
            "Unit", "Vice", "Ward", "Xenon", "Yield", "Zenith", "Aegis", "Blade", "Cipher", "Dawn",
            "Bolt", "Clank", "Dynamo", "Edge", "Frost", "Gauge", "Hex", "Impulse", "Jet", "Knox",
            "Link", "Magnet", "Node", "Orbit", "Pivot", "Quarry", "Reactor", "Spire", "Torch", "Vector",
            "Weld", "Zinc", "Alloy", "Beam", "Core", "Dash", "Eon", "Frame", "Gear", "Hull", "Ingot",
            "Jolt", "Keel", "Lever", "Matrix", "Node", "Optic", "Pylon", "Quartz", "Ratchet", "Surge",
            "Turbine", "Volt", "Winch", "Xylo", "Yoke", "Zap"
        ],
        "female_names": [
            "Aegis", "Blade", "Cipher", "Dawn", "Ember", "Frost", "Glory", "Haven", "Iris", "Jade",
            "Karma", "Lumen", "Mist", "Nova", "Orbit", "Pulse", "Quest", "Rune", "Spark", "Tempest",
            "Unity", "Vortex", "Willow", "Xylo", "Zen", "Aria", "Breeze", "Cinder", "Dusk", "Ember",
            "Array", "Breeze", "Circuit", "Dusk", "Echo", "Fable", "Gear", "Harmony", "Inertia", "Jubilee",
            "Kaleidoscope", "Lattice", "Mirage", "Nimbus", "Oasis", "Prism", "Quill", "Reflect", "Silhouette",
            "Tide", "Vivid", "Wisp", "Xenith", "Yield", "Zephyr", "Alba", "Beryl", "Crystal", "Delta", "Eclipse",
            "Facade", "Glyph", "Horizon", "Illumina", "Jade", "Kyanite", "Lunar", "Mosaic", "Nebula", "Opaline",
            "Pixel", "Quartz", "Ripple", "Spectrum", "Tesseract", "Umbra", "Vertex", "Whirl", "Xenon", "Yucca", "Zircon"
        ]
    },
    "Changeling": {
        "last_names": [
            "Manyfaces", "Twistmirror", "Evermask", "Shiftshade", "Glimmerveil", "Trueform",
            "Mirrorborn", "Doublesight", "Nightskin", "Wispshadow", "Echovoice", "Morphling",
            "Vaguefigure", "Flickerflesh", "Cloudpersona", "Blendwalker", "Gossamer", "Silkveil",
            "Dawndisguise", "Twilightmask"
        ],
        "archetypes": ["Spy", "Infiltrator", "Diplomat", "Actor"],
        "backgrounds": ["Charlatan", "Entertainer", "Urban Bounty Hunter", "Spy"],
        "innate_abilities": ["Shapechanger", "Changeling Versatility", "Unsettling Visage"],
        "preferred_classes": ["Rogue", "Bard", "Sorcerer", "Warlock"],
        "culture": "Changeling culture is fluid, mirroring their ability to adapt and change. They often find themselves in the role of mediators, spies, or entertainers, thriving on their capacity for transformation. Changelings lack a unified society, instead blending into those of other races, although they do form tight-knit communities where they can truly be themselves without fear.",
        "alignment": ["True Neutral", "Neutral Good", "Neutral Evil", "Lawful Neutral", "Chaotic Neutral"],
        "lore": "Changelings are beings with the supernatural ability to alter their appearance. Their origins are shrouded in mystery, with rumors of their lineage tied to doppelgangers. Changelings use their abilities not just for survival, but to explore the very nature of identity.",
        "physical_characteristics": {
            "Male": {"height": (160, 180), "weight": (50, 70)},
            "Female": {"height": (160, 180), "weight": (50, 70)}
        },
        "male_names": [
            "Blaise", "Caelum", "Dael", "Echo", "Fable", "Gale", "Harken", "Illum", "Jester", "Kael",
            "Lark", "Mimic", "Nemo", "Orion", "Pace", "Quill", "Riddle", "Sable", "Tale", "Umbra",
            "Veer", "Whim", "Xilo", "Yonder", "Zephyr","Arc", "Brisk", "Crest", "Drake", "Ebb", 
            "Flint", "Glitch", "Haze", "Ink", "Jolt", "Kite", "Loft", "Mirth", "Niche", "Ogle", 
            "Pulse", "Quest", "Rift", "Surge", "Thrift", "Undertow", "Vex", "Wink", "Xorn", "Yield", "Zest"
        ],
        "female_names": [
            "Aura", "Briar", "Clio", "Dream", "Elysia", "Fawn", "Glimmer", "Halo", "Ivy", "Joy",
            "Kismet", "Luna", "Mirage", "Nyx", "Opal", "Pixie", "Quest", "Raven", "Star", "Twyla",
            "Utopia", "Vail", "Wisp", "Xen", "Yara", "Zinnia", "Aria", "Bliss", "Chime", "Dove", "Essence", "Flare", "Gale", "Heart", "Isle", "Jewel",
            "Kindle", "Leaf", "Muse", "Nectar", "Ode", "Plume", "Quaint", "Rise", "Shine", "Thrive",
            "Vivid", "Wave", "Zephyr", "Aurora", "Bloom", "Celeste", "Dawn", "Eve", "Fauna", "Glow",
            "Harbor", "Indigo", "Jasmine", "Kiara", "Lyric", "Melody", "Nirvana", "Oasis", "Petal",
            "Quiver", "Rhythm", "Serene", "Trance", "Unity", "Venus", "Whisper", "Xanthe", "Yasmine", "Zelda"
        ]
    },
    "Kobold": {
        "last_names": [
            "Flamepaw", "Sneakwhisker", "Trapminder", "Goldsniffer", "Tunneldigger", "Rockchipper",
            "Gemscale", "Shadowtail", "Lodefinder", "Burrowclaw", "Cragshaper", "Riddlepebble",
            "Nestwatcher", "Moonminer", "Firesnout", "Sparkshin", "Ashwhisk", "Dustfoot", "Glinteye",
            "Darkburrow"
        ],
        "archetypes": ["Trapmaker", "Scout", "Inventor", "Sorcerer"],
        "backgrounds": ["Urchin", "Artisan", "Outcast", "Tinker"],
        "innate_abilities": ["Pack Tactics", "Sunlight Sensitivity", "Grovel, Cower, and Beg", "Dragon's Cunning"],
        "preferred_classes": ["Rogue", "Wizard", "Sorcerer", "Artificer"],
        "culture": "Kobold society is deeply hierarchical, centered around serving a powerful leader or dragon. They are ingenious trap makers, valuing cunning and resourcefulness. Their communities are often underground or in dense forests, places where they can leverage their affinity for traps and stealth.",
        "alignment": [
            "Lawful Evil",
            "Neutral Evil",
            "Lawful Neutral"
        ],
        "lore": "Kobolds are small, reptilian creatures who worship dragons as demigods and serve them with fanatic fervor. Their lives are dedicated to serving these powerful beings, emulating their strength and cunning in hopes of gaining favor or protection.",
        "physical_characteristics": {
            "Male": {"height": (90, 120), "weight": (25, 35)},
            "Female": {"height": (85, 115), "weight": (20, 30)}
        },
        "male_names": [
            "Meepo", "Kurtulmak", "Dak", "Jeek", "Rik", "Snick", "Taklak", "Urd", "Zak", "Grex",
            "Hark", "Irk", "Kob", "Lurk", "Merk", "Nerk", "Pik", "Quik", "Rat", "Skrat",
            "Tak", "Urd", "Vak", "Wak", "Xak", "Yak", "Zak", "Aak", "Bak", "Cak", "Dak",
            "Eak", "Fak", "Gak", "Hak", "Iak", "Jak", "Kak", "Lak", "Mak", "Nak", "Oak",
            "Vex", "Pox", "Glib", "Nix", "Ox", "Zip", "Tix", "Vik", "Wrex", "Zix",
            "Blix", "Crix", "Drex", "Flix", "Grix", "Jix", "Klix", "Lix", "Mix", "Nixx",
            "Pix", "Qix", "Rix", "Stix", "Trix", "Vox", "Wix", "Xix", "Yix", "Zax"
        ],
        "female_names": [
            "Eepa", "Kobara", "Daka", "Jeeka", "Rika", "Snika", "Takla", "Urda", "Zaka", "Grexa",
            "Harka", "Irka", "Koba", "Lurka", "Merka", "Nerka", "Pika", "Quika", "Rata", "Skrata",
            "Axa", "Bixa", "Cixa", "Daxa", "Fexa", "Gixa", "Hexa", "Ixa", "Jexa", "Kixa",
            "Lexa", "Mixa", "Nixa", "Oxa", "Pexa", "Qixa", "Rexa", "Sixa", "Texa", "Uxa",
            "Vixa", "Wexa", "Xixa", "Yexa", "Zexa", "Axia", "Bexa", "Cexa", "Dexa", "Exa"
        ]
    },
    "Bugbear": {
        "last_names": [
            "Nightclaw", "Moonstalker", "Shadowgrip", "Thornbrute", "Silentthorn", "Gloomhunter",
            "Beastsnarl", "Darkfur", "Bloodpaw", "Grimhide", "Savageheart", "Briarborn", "Stealthstride",
            "Ragefang", "Mistwalker", "Frostjaw", "Ironmaul", "Thunderhowl", "Boulderback", "Stormclaw"
        ],
        "archetypes": ["Brute", "Sneak", "Ambusher", "Warrior"],
        "backgrounds": ["Marauder", "Outcast", "Survivor", "Spy", "Scout"],
        "innate_abilities": ["Long-Limbed", "Powerful Build", "Sneaky", "Surprise Attack"],
        "preferred_classes": ["Rogue", "Barbarian", "Ranger", "Fighter"],
        "culture": "Bugbear society values strength and stealth, with individuals often serving as scouts or warriors within goblinoid armies. They prefer solitary or small group living, relying on their prowess in ambush and combat to survive and thrive.",
        "alignment": [
            "Chaotic Evil",
            "Neutral Evil",
            "Chaotic Neutral"
        ],
        "lore": "Bugbears are the larger cousins of goblins and hobgoblins, known for their brute strength and predatory nature. They are the boogeymen of the forest, using their stealth and power to terrorize weaker creatures.",
        "physical_characteristics": {
            "Male": {"height": (190, 220), "weight": (100, 150)},
            "Female": {"height": (180, 210), "weight": (90, 140)}
        },
        "male_names": [
            "Krugg", "Morg", "Brug", "Thokk", "Grank", "Vrok", "Drukk", "Hrung", "Korg", "Lug",
            "Narg", "Orsk", "Prug", "Ront", "Srug", "Trag", "Urg", "Vrak", "Wrang", "Zrug",
            "Blarg", "Murk", "Thrug", "Vorn", "Grash", "Krug", "Morn", "Drak", "Gurn", "Lorn",
            "Barn", "Dorn", "Frug", "Gharn", "Hurn", "Karn", "Lark", "Musk", "Nusk", "Parn",
            "Quark", "Rusk", "Sark", "Tharn", "Urk", "Varn", "Wark", "Xarn", "Yurk", "Zarn"
        ],
        "female_names": [
            "Brulla", "Kella", "Urga", "Grumsha", "Vrulla", "Mogga", "Drulla", "Lurga", "Snorga", "Rulla",
            "Torgga", "Wurga", "Zugga", "Nurka", "Krugga", "Hrug", "Gragga", "Frukka", "Dugga", "Cragga",
            "Aruga", "Bruga", "Cruga", "Druga", "Eruga", "Fruga", "Gruga", "Hruga", "Iruga", "Kruga",
            "Lruga", "Mruga", "Nruga", "Oruga", "Pruga", "Qruga", "Rruga", "Sruga", "Truga", "Uruga",
            "Vruga", "Wruga", "Xruga", "Yruga", "Zruga", "Aruk", "Bruk", "Cruk", "Druk", "Erk"
        ]
    },
    "Githyanki": {
        "last_names": [
            "Warslayer", "Astralreaver", "Voidrunner", "Starblade", "Galaxyborn", "Sunspear",
            "Netherstrike", "Cosmicfury", "Skyraider", "Voidscar", "Astrosmith", "Eclipsehunter",
            "Starvenger", "Galacticrage", "Cometstrike", "Planeswalker", "Nebuladream", "Voidborn",
            "Celestialwar", "Aetherwarrior"
        ],
        "archetypes": ["Warrior", "Knight", "Psion", "Wizard"],
        "backgrounds": ["Astral Raider", "Soldier", "Mercenary", "Spellblade"],
        "innate_abilities": ["Decadent Mastery", "Githyanki Psionics", "Martial Prodigy", "Astral Navigation", "Telepathy"],
        "preferred_classes": ["Fighter", "Wizard", "Warlock", "Paladin"],
        "culture": "Githyanki society is martial and hierarchical, organized under a strict caste system led by their lich-queen, Vlaakith. They dwell in the Astral Plane, in fortresses built from the carcasses of dead gods, and are known for their raids on other worlds aboard astral ships.",
        "alignment": [
            "Lawful Evil",
            "Neutral Evil",
            "Lawful Neutral"
        ],
        "lore": "Originating from a race enslaved by mind flayers, the Githyanki broke free and evolved into fierce warriors of the Astral Plane. They harbor a deep hatred for their former oppressors and are ever-prepared for conflict, viewing other races as either tools or threats.",
        "physical_characteristics": {
            "Male": {"height": (170, 190), "weight": (60, 75)},
            "Female": {"height": (160, 180), "weight": (55, 70)}
        },
        "male_names": [
            "Zerthimon", "Githrak", "Vlaakith", "Kithrak", "Zerth", "Dak'kon", "Quith", "Rakth", "Sarath", "Vith",
            "Munthrek", "Nareth", "Pyrth", "Reth", "Sekth", "Tyrth", "Vlak", "Yarth", "Zeth", "Frath", "Krath", "Larth",
            "Marth", "Nyth", "Orath", "Prath", "Qith", "Rorth", "Sarth", "Trith", "Urth", "Varth", "Wrath", "Xarth",
            "Yith", "Zurth", "Athrek", "Brak", "Certh", "Derth"
        ],
        "female_names": [
            "Zirthara", "Githara", "Vlaa", "Kithara", "Zertha", "Dak'kara", "Quitha", "Raktha", "Saratha", "Vitha",
            "Munthara", "Naretha", "Pyrtha", "Retha", "Sektha", "Tyrtha", "Vlaka", "Yartha", "Zetha", "Fratha", "Kratha",
            "Lartha", "Martha", "Nyrtha", "Oratha", "Pratha", "Qitha", "Rortha", "Sartha", "Tritha", "Urtha", "Vartha",
            "Wratha", "Xartha", "Yitha", "Zurtha", "Athreka", "Braka", "Certha", "Dertha"
        ]
    },
    "Githzerai": {
        "last_names": [
            "Mindbender", "Calmstorm", "Zenrith", "Stillwater", "Ironmeditate", "Peacewalker",
            "Voidheart", "Silentflow", "Nirzuk", "Kithrak", "Zenpath", "Quietstream", "Soulgaze",
            "Freedthinker", "Mindpeace", "Tranquilfist", "Serenityblade", "Deepbreath", "Wisdomseek",
            "Harmonyforge"
        ],
        "archetypes": ["Monk", "Mystic", "Ascetic", "Sage"],
        "backgrounds": ["Hermit", "Philosopher", "Rebel", "Meditator"],
        "innate_abilities": ["Mental Discipline", "Githzerai Psionics", "Monastic Training", "Mind Over Body"],
        "preferred_classes": ["Monk", "Wizard", "Rogue", "Sorcerer"],
        "culture": "Githzerai society values meditation, discipline, and self-control, residing in monastic communities within the Elemental Chaos or Limbo. They seek enlightenment and personal improvement, eschewing materialism and conflict unless absolutely necessary.",
        "alignment": [
            "Neutral Good",
            "True Neutral",
            "Chaotic Good"
        ],
        "lore": "The Githzerai split from the Githyanki following their rebellion against the mind flayers, choosing a path of contemplation and self-mastery over conquest. Their monks and wizards are among the multiverse's most disciplined minds, capable of imposing order on chaos itself.",
        "physical_characteristics": {
            "Male": {"height": (170, 190), "weight": (55, 70)},
            "Female": {"height": (160, 180), "weight": (50, 65)}
        },
        "male_names": [
            "Zerthimon", "Dak'kon", "Kithrak", "Mennu", "Vith", "Zerth", "Quith", "Rathenn", "Sumat", "T'zar",
            "Zenoth", "Harth", "Nimozaran", "Zetch'r'r", "Fenkenkabradon", "Geth", "Hith", "Jor", "Keth", "Lor",
            "Mith", "Noth", "Orth", "Peth", "Qar", "Ruth", "Sith", "Teth", "Uth", "Verth", "Weth", "Xun", "Yeth",
            "Zarth", "Aen", "Borth", "Ceth", "Dorth"
        ],
        "female_names": [
            "Anith", "Erza", "Ithra", "Jysse", "Kalla", "Minthka", "Nerth", "Ossa", "Pirra", "Senna",
            "Thissa", "Ula", "Vessa", "Wynna", "Xara", "Yessa", "Zinna", "Aetha", "Betha", "Cirth", "Dirth",
            "Eirth", "Firth", "Girtha", "Hirth", "Irtha", "Jirth", "Kirth", "Lirth", "Mirth", "Nirth",
            "Oirth", "Pirth", "Qirtha", "Rirth", "Sirth", "Tirth", "Uirth", "Virth", "Wirth", "Xirth",
            "Yirth", "Zirth"
        ]
    },
    "Hobgoblin": {
        "last_names": [
            "Steelmark", "Bloodaxe", "Dreadmarch", "Skullcrusher", "Stormblade", "Thunderfist",
            "Battleborn", "Darkhelm", "Firebrand", "Grimstrike", "Ironfist", "Ragehammer",
            "Shadowstalker", "Vengeancekeeper", "Warforge", "Bladestorm", "Doombringer", "Frostblade",
            "Gorefang", "Hardcut", "Raveneye", "Shieldbasher", "Swordwielder", "Battlechanter",
            "Crimsonhand", "Nightblade", "Stonebreaker", "Flamebearer", "Windrider", "Earthshaker",
            "Stormcaller", "Wolfhunter", "Mightymaul"
        ],
        "archetypes": ["Legionnaire", "Tactician", "Commander", "Warlock"],
        "backgrounds": ["Military Officer", "Strategist", "Mercenary Leader", "Enforcer"],
        "innate_abilities": ["Martial Training", "Saving Face", "Iron Discipline", "Tactical Genius"],
        "preferred_classes": ["Fighter", "Warlock", "Wizard", "Rogue"],
        "culture": "Hobgoblin society is militaristic and organized, with a strong emphasis on discipline, hierarchy, and martial prowess. They live in well-ordered communities, often at the heart of expansive empires, and value strength, loyalty, and martial honor.",
        "alignment": [
            "Lawful Neutral",
            "True Neutral",
            "Lawful Evil"
        ],
        "lore": "Hobgoblins are the disciplined and militaristic cousins of goblins and bugbears, known for their strategic minds and formidable armies. They build their societies on the principles of strength and order, often clashing with other races in their expansionist endeavors.",
        "physical_characteristics": {
            "Male": {"height": (155, 185), "weight": (70, 100)},
            "Female": {"height": (150, 180), "weight": (65, 95)}
        },
        "male_names": [
            "Azrok", "Brug", "Durnn", "Gharn", "Hark", "Karguk", "Lhurusk", "Mog", "Narug", "Olg",
            "Rhogar", "Thorgak", "Ulgar", "Vark", "Zog", "Skarn", "Grumbar", "Targ", "Fulgrim", "Drang",
            "Irk", "Krug", "Marzok", "Nurk", "Prak", "Quar", "Rend", "Sog", "Turk", "Urg", "Vorg",
            "Warg", "Xurk", "Yarg", "Zurk"
        ],
        "female_names": [
            "Anya", "Betha", "Ezra", "Grenza", "Hura", "Kyniska", "Lashka", "Murna", "Narsa", "Orsha",
            "Phara", "Renza", "Surina", "Tura", "Vesha", "Wurna", "Xasha", "Yurna", "Zasha", "Arsha",
            "Briska", "Curna", "Draka", "Erna", "Firsha", "Gurna", "Harnsha", "Irsha", "Jurna", "Korsha",
            "Lurna", "Masha", "Norsha", "Prisha", "Quasha"
        ]
    },
    "Leonin": {
        "last_names": [
            "Goldfur", "Sunspear", "Thunderpelt", "Braveheart", "Clawstrike", "Dawnhunter",
            "Fierceeye", "Galemane", "Highclaw", "Lionheart", "Nightstalker", "Quickmane",
            "Ridgeguard", "Savannahroar", "Stormtail", "Truepride", "Windrunner", "Brightmane",
            "Duskmaw", "Swiftstride", "Plainstrider", "Sundancer", "Moonwatcher", "Starroar",
            "Wildmane", "Stormbringer", "Beastcaller", "Fangbearer", "Grassrunner", "Skygazer"
        ],
        "archetypes": ["Guardian", "Hunter", "Champion", "Pride Leader", "Sunwalker", "Ancestral Speaker"],
        "backgrounds": ["Soldier", "Nomad", "Hunter", "Gladiator", "Priest", "Emissary"],
        "innate_abilities": ["Daunting Roar", "Hunters Instincts", "Prideful", "Leonin Courage", "Keen Smell"],
        "preferred_classes": ["Fighter", "Paladin", "Barbarian", "Cleric"],
        "culture": "Leonin societies are pride-centric, with a strong emphasis on honor, strength, and community. They inhabit savannahs or grasslands, forming tight-knit prides led by the strongest among them. Leonins value courage and are fiercely protective of their territories and pride members.",
        "alignment": [
            "Lawful Good",
            "Neutral Good",
            "Lawful Neutral"
        ],
        "lore": "Originating from realms where the wilds dominate the landscape, Leonins are as majestic as they are formidable. Their society is built around the concept of the pride, a close-knit family unit that hunts together, fights together, and thrives together.",
        "physical_characteristics": {
            "Male": {"height": (190, 220), "weight": (90, 120)},
            "Female": {"height": (180, 210), "weight": (80, 110)}
        },
        "male_names": [
            "Ajas", "Kyro", "Mavros", "Nemis", "Pyrrhos", "Sarros", "Theros", "Vantas", "Xanthos", "Zethos",
            "Leonar", "Gaios", "Daxos", "Cimber", "Balasar", "Ephoros", "Galenos", "Hesperos", "Ikaros", "Karnos",
            "Lycos", "Myron", "Nikos", "Orestes", "Pylades", "Soter", "Theon", "Urian", "Varis", "Zephyros",
            "Alector", "Basil", "Cosmas", "Demitrios", "Eurion", "Faust", "Gyrus", "Helios", "Isidor", "Janus"
        ],
        "female_names": [
            "Althaia", "Dione", "Eirene", "Halia", "Ione", "Kleonai", "Nysa", "Olympia", "Phila", "Selene",
            "Thalia", "Xanthe", "Zoisa", "Galea", "Mirin", "Anthea", "Bryseis", "Chryseis", "Danaë", "Electra",
            "Eudora", "Galatea", "Hermione", "Ianthe", "Kalypso", "Leda", "Maia", "Nyssa", "Ophira", "Penelope",
            "Rhea", "Sapphira", "Theia", "Xenia", "Yseult", "Zephyra", "Ariadne", "Calliope", "Daphne", "Evadne"
        ]
    },
    "Vedalken": {
        "last_names": [
            "Cloudbreaker", "Dreamwinder", "Thoughtweaver", "Puzzleknot", "Chronostalker", "Aetherflux",
            "Voidwatcher", "Etherseeker", "Skybridge", "Mindforge", "Logicchain", "Blueprinter",
            "Inkthinker", "Cloudreacher", "Spellmatrix", "Knowledgepool", "Gadgetgrasp", "Mechanobinder",
            "Quantumspinner", "Plasmaflect"
        ],
        "archetypes": ["Alchemist", "Scholar", "Arcanist", "Inventor", "Philosopher", "Mediator"],
        "backgrounds": ["Sage", "Artisan", "Guild Artisan", "Researcher", "Academic", "Engineer"],
        "innate_abilities": ["Vedalken Dispassion", "Tireless Precision", "Enhanced Intellect", "Gift of the Guildpact", "Logical"],
        "preferred_classes": ["Wizard", "Artificer", "Cleric", "Rogue"],
        "culture": "Vedalken are known for their pursuit of knowledge and perfection. They thrive in societies where innovation and discovery are valued, often dedicating their lives to academic or scientific endeavors. Vedalken are methodical and believe in improving themselves and their surroundings through careful study and meticulous work.",
        "alignment": [
            "Lawful Neutral",
            "True Neutral",
            "Lawful Good"
        ],
        "lore": "Vedalken have an innate drive for perfection, pushing the boundaries of magic and science alike. They are often seen as aloof or detached, but this demeanor belies a deep commitment to their chosen fields of study and an intense curiosity about the world.",
        "physical_characteristics": {
            "Male": {"height": (180, 210), "weight": (70, 90)},
            "Female": {"height": (175, 205), "weight": (65, 85)}
        },
        "male_names": [
            "Arlunn", "Belin", "Cyrn", "Davn", "Elocin", "Firn", "Gelv", "Halmi", "Ithim", "Jiln",
            "Kovin", "Lumn", "Moln", "Nirin", "Olnim", "Peln", "Qiln", "Ralm", "Sivin", "Talmn",
            "Ulvim", "Veln", "Wilm", "Xiln", "Yalmn", "Zenv",
            "Arvad", "Brevn", "Celn", "Drivn", "Elvon", "Fenv", "Girv", "Haln", "Ivon", "Jurn",
            "Keln", "Lirv", "Mivn", "Nalv", "Orvn", "Pelv", "Qurn", "Rilv", "Siln", "Tirv", "Ulnv", "Vorv", "Wurn", "Xenv", "Yurv", "Ziln"
        ],
        "female_names": [
            "Alinvi", "Belna", "Cervi", "Delvi", "Elna", "Firvi", "Gelni", "Halvi", "Ivni", "Jelva",
            "Kelni", "Lirva", "Milvi", "Nilva", "Olvni", "Pelva", "Qilna", "Rivna", "Silvi", "Tilva",
            "Ulvni", "Velna", "Wilva", "Xilvi", "Yalna", "Zelvi",
            "Ardi", "Breni", "Cilvi", "Divna", "Ervi", "Fenvi", "Greni", "Hilva", "Irni", "Jenva",
            "Karni", "Lenvi", "Marni", "Nirva", "Orni", "Parni", "Qervi", "Reni", "Sarni", "Tervi", "Urni", "Varni", "Wervi", "Xarni", "Yervi", "Zarni"
        ]
    },
    "Tortle": {
         "last_names": [
            "Sandshaper", "Wavehider", "Deepshell", "Sunbasker", "Mudgrafter", "Tidewalker",
            "Reefcutter", "Seaburrow", "Shellcrafter", "Saltweaver", "Turtlefriend", "Brightshell",
            "Moonshell", "Starbask", "Coralcarver", "Shellgatherer", "Seaspeaker", "Tidecaller",
            "Shellseeker", "Oceanwhisper"
        ],
        "archetypes": ["Shellguard", "Wayfarer", "Naturalist", "Survivalist", "Beastfriend", "Shaman"],
        "backgrounds": ["Hermit", "Sailor", "Fisher", "Guide", "Explorer", "Monk"],
        "innate_abilities": ["Shell Defense", "Survival Instinct", "Natural Armor", "Hold Breath", "Claws"],
        "preferred_classes": ["Druid", "Fighter", "Monk", "Ranger"],
        "culture": "Tortle communities are often found in coastal or island regions, living simple lives in harmony with nature. They have a deep respect for the world around them, often following the tenets of druidism or worshipping nature deities. Tortles are known for their wisdom, patience, and a strong sense of community.",
        "alignment": [
            "Neutral Good",
            "True Neutral",
            "Chaotic Good"
        ],
        "lore": "Tortles carry their homes on their backs, wandering the lands and waters with a serene confidence. They are born travelers and explorers, taking to the sea with the same ease as they traverse the land. Their long lifespans grant them a broad perspective on the world and its cycles.",
        "physical_characteristics": {
            "Male": {"height": (150, 180), "weight": (200, 250)},
            "Female": {"height": (150, 180), "weight": (200, 250)}
        },
        "male_names": [
            "Bash", "Click", "Dov", "Gorb", "Harb", "Juk", "Kurm", "Lor", "Morv", "Nort",
            "Orb", "Ploq", "Quott", "Rast", "Sunt", "Turm", "Urt", "Volt", "Wont", "Xest",
            "Yolt", "Zorp", "Arp", "Bort", "Cott", "Durt", "Erp", "Folt", "Gunt", "Holt",
            "Jort", "Kolt", "Lurt", "Mott", "Nurt", "Ort", "Punt", "Rolt", "Sort", "Tunt", "Vort", "Wurt", "Xort", "Yurt", "Zott"
        ],
        "female_names": [
            "Anala", "Birta", "Curla", "Dorna", "Erla", "Furna", "Gurna", "Hurna", "Irta", "Jolta",
            "Kurna", "Lurta", "Morna", "Nurta", "Orla", "Purta", "Qirta", "Rosta", "Sulta", "Turta",
            "Urna", "Vurna", "Wirta", "Xurna", "Yurta", "Zolta",
            "Arla", "Borna", "Corla", "Durla", "Erna", "Folta", "Gorla", "Holta", "Irla", "Jorla",
            "Korla", "Lorla", "Murla", "Norla", "Orna", "Porla", "Qorla", "Rorla", "Sorla", "Torla", "Uorla", "Vorla", "Worla", "Xorla", "Yorla", "Zorla"
        ]
    },
}

def generate_character(genders, race_details):
    gender = random.choice(genders)
    race = random.choice(list(race_details.keys()))
    details = race_details[race]

    first_name = random.choice(details["male_names"] if gender == "Male" else details["female_names"])
    last_name = random.choice(details["last_names"])
    archetype = random.choice(details["archetypes"])
    background = random.choice(details["backgrounds"])
    
    height_range = details["physical_characteristics"][gender]['height']
    weight_range = details["physical_characteristics"][gender]['weight']

    # Correctly generate height and weight within the specified range
    height = f"{random.randint(height_range[0], height_range[1])} cm"
    weight = f"{random.randint(weight_range[0], weight_range[1])} kg"
    
    alignment = random.choice(details["alignment"])

    character = {
        "Name": f"{first_name} {last_name}",
        "Gender": gender,
        "Race": race,
        "Alignment": alignment,
        "Archetype": archetype,
        "Background": background,
        "Height": height,
        "Weight": weight,
        "Culture": details["culture"],
        "Lore": details["lore"],
    }
    
    return character

def generate_characters_list(n, genders, race_details):
    characters = [generate_character(genders, race_details) for _ in range(n)]
    return json.dumps(characters, indent=4)

def save_characters_to_file(characters_json):
    num_characters = json.loads(characters_json).__len__()
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"{num_characters}_characters_{date_str}.json"
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(characters_json)
    
    print(f"Saved {num_characters} characters to {filename}")

def main():
    num_characters = int(input("How many characters would you like to generate? "))
    characters_json = generate_characters_list(num_characters, genders, race_details)
    save_characters_to_file(characters_json)

if __name__ == "__main__":
    main()

def validate_race_details(race_details):
    for race, details in race_details.items():
        for gender in ['Male', 'Female']:
            height_range = details["physical_characteristics"][gender]['height']
            weight_range = details["physical_characteristics"][gender]['weight']
            if not (isinstance(height_range, tuple) and len(height_range) == 2 and all(isinstance(num, (int, float)) for num in height_range)):
                print(f"Error in {race} {gender} height_range: {height_range}")
            if not (isinstance(weight_range, tuple) and len(weight_range) == 2 and all(isinstance(num, (int, float)) for num in weight_range)):
                print(f"Error in {race} {gender} weight_range: {weight_range}")


#validate_race_details(race_details)
                
