import re

CATEGORY_KEYWORDS = {
    "animal": [
        "dog", "cat", "octopus", "shark", "bird", "elephant", "lion", "tiger",
        "bee", "ant", "spider", "fish", "whale", "snake", "frog", "insect",
        "mammal", "species", "animal", "pig", "cow", "horse", "chicken",
        "owl", "bat", "wolf", "penguin", "rabbit", "mouse", "monkey", "bear",
    ],
    "ocean": [
        "ocean", "sea", "wave", "underwater", "reef", "beach", "tide", "coral",
    ],
    "space": [
        "moon", "star", "planet", "space", "sun", "galaxy", "universe",
        "earth", "mars", "astronaut", "orbit", "comet", "asteroid", "nasa",
    ],
    "food": [
        "food", "eat", "fruit", "vegetable", "apple", "banana", "chocolate",
        "coffee", "tea", "pizza", "cheese", "sugar", "honey", "drink", "cook",
        "recipe", "meal", "bread", "rice", "potato",
    ],
    "body": [
        "brain", "heart", "blood", "bone", "muscle", "skin", "hair", "eye",
        "ear", "nose", "tooth", "teeth", "lung", "stomach", "nerve", "cell",
        "dna", "sneeze", "yawn",
    ],
    "history": [
        "war", "wwii", "ww1", "ww2", "battle", "king", "queen", "ancient",
        "century", "history", "empire", "revolution", "president", "army",
        "navy", "military", "soldier", "medieval", "pirate", "pilot",
        "fighter plane",
    ],
    "science": [
        "atom", "chemical", "physics", "chemistry", "science", "scientist",
        "electron", "gravity", "energy", "experiment", "technology",
        "computer", "robot", "internet", "invented", "invention",
    ],
    "nature": [
        "tree", "plant", "forest", "flower", "leaf", "mountain", "volcano",
        "weather", "rain", "storm", "desert", "river", "lake",
    ],
}

CATEGORY_ORDER = [
    "animal", "ocean", "space", "food", "body", "history", "science", "nature",
]

CATEGORY_PATTERNS = {
    category: [re.compile(r"\b" + re.escape(keyword) + r"(e?s)?\b") for keyword in keywords]
    for category, keywords in CATEGORY_KEYWORDS.items()
}


def categorize(text):
    lowered = text.lower()
    for category in CATEGORY_ORDER:
        for pattern in CATEGORY_PATTERNS[category]:
            if pattern.search(lowered):
                return category
    return "general"


def run(input):
    input["category"] = categorize(input.get("text", ""))
    return input
