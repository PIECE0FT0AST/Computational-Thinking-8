import random

# Pick a word at random
word_list = ["aisle", "amiss", "annex", "axiom", "azure",
"bacon", "badge", "banal", "binge", "blitz", "bough", "brace",
"cairn", "caper", "chasm", "civic", "clout", "crimp", "cynic",
"deign", "deter", "dowel", "drier", "droll", "dunce", "dwelt",
"eclat", "edict", "egret", "elude", "ember", "enact", "ennui",
"fable", "fecal", "feign", "feral", "finer", "flair", "fluke",
"gawky", "girth", "glint", "gnash", "gnome", "grime", "guile",
"harem", "haste", "hinge", "hoard", "hound", "humid", "hyena",
"icily", "imbue", "inert", "irate", "irony",
"jaunt", "jelly", "jerky", "joust", "judge",
"karma", "kayak", "kneel", "knelt", "knoll",
"lapse", "larva", "latch", "lithe", "loath", "lurch",
"mangy", "melee", "merit", "mirth", "modal", "moray",
"nasal", "niche", "niece", "nudge", "nymph",
"oaken", "obese", "occur", "onset", "otter",
"pansy", "peril", "plume", "poise", "prone",
"quell", "query", "quill", "quirk", "quota",
"rabid", "recap", "rinse", "rouge", "ruder",
"salve", "scald", "scone", "serum", "shard", "skimp", "slate",
"smirk", "snare", "spore", "spurn", "squib", "stack",
"tacit", "taint", "tenet", "thorn", "thrum", "tithe",
"ulcer", "umbra", "unfed", "untie", "usher",
"vague", "valve", "venom", "vicar", "vigor",
"waive", "waltz", "weary", "widen", "wince",
"xenon",
"yearn", "yeast", "yield",
"zonal", "zesty"]
hidden_word = random.choice(word_list)

print("WORDLE:")

# Repeat for 6 guesses
for i in range(6):
    # Guess a word
    guess_word = input()
    output = ""

    # First letter (in python, counting starts at 0 not 1)
    if guess_word[0] == hidden_word[0]:
        output += "🟩"
    elif guess_word[0] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
    
# Second letter (in python, counting starts at 0 not 1)
    if guess_word[0] == hidden_word[0]:
        output += "🟩"
    elif guess_word[0] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
   
   # Third letter (in python, counting starts at 0 not 1)
    if guess_word[0] == hidden_word[0]:
        output += "🟩"
    elif guess_word[0] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

# Fourth letter (in python, counting starts at 0 not 1)
    if guess_word[0] == hidden_word[0]:
        output += "🟩"
    elif guess_word[0] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

        # Fifth letter (in python, counting starts at 0 not 1)
    if guess_word[0] == hidden_word[0]:
        output += "🟩"
    elif guess_word[0] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

    # Result
    print(output)
    if output == "🟩🟩🟩🟩🟩":
        print("You win")
        break

print(f"You used {i+1} guesses")