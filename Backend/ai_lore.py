import random

monster_names = [
    "Shadow Beast",
    "Void Stalker",
    "Infernal Wraith",
    "Bone Reaper",
    "Night Terror",
    "Crimson Ghoul",
    "Abyss Watcher",
    "Dark Phantom"
]

monster_lore = [
    "A dark creature born from cursed forests.",
    "An ancient monster that hunts in forgotten ruins.",
    "A terrifying entity that feeds on fear.",
    "A beast summoned from another dimension.",
    "A corrupted guardian twisted by dark magic.",
    "A creature forged in the shadows of the underworld.",
    "A night predator feared by all who see it.",
    "A mysterious monster emerging from the void."
]

rarity_levels = [
    "Common",
    "Rare",
    "Epic",
    "Legendary"
]


def generate_monster_lore(prompt):

    name = random.choice(monster_names)
    lore = random.choice(monster_lore)
    rarity = random.choice(rarity_levels)

    stats = {
        "intensity": random.randint(40, 100),
        "stealth": random.randint(40, 100),
        "rift_affinity": random.randint(40, 100)
    }

    return name, lore, rarity, stats