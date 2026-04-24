import json
import os

# File to store discovered elements
SAVE_FILE = "discoveries.json"

# Default elements
elements = ["Water", "Fire", "Earth", "Air"]

# Recipes (you can expand this infinitely)
recipes = {
    ("Water", "Fire"): "Steam",
    ("Earth", "Water"): "Mud",
    ("Air", "Fire"): "Smoke",
    ("Earth", "Fire"): "Lava",
    ("Water", "Air"): "Rain",
    ("Earth", "Rain"): "Plant",
    ("Plant", "Fire"): "Ash",
    ("Lava", "Water"): "Stone"
}


def load_game():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            return json.load(f)
    return elements.copy()


def save_game(discovered):
    with open(SAVE_FILE, "w") as f:
        json.dump(discovered, f)


def combine(a, b):
    pair = (a, b)
    reverse_pair = (b, a)

    if pair in recipes:
        return recipes[pair]
    elif reverse_pair in recipes:
        return recipes[reverse_pair]
    else:
        return None


def main():
    discovered = load_game()

    print("🌍 Infinite Craft (Python Edition)")
    print("Type 'exit' to quit.\n")

    while True:
        print("\nDiscovered elements:")
        print(", ".join(discovered))

        a = input("\nFirst element: ").strip().title()
        if a.lower() == "exit":
            break

        b = input("Second element: ").strip().title()
        if b.lower() == "exit":
            break

        if a not in discovered or b not in discovered:
            print("❌ You haven't discovered one of those elements yet.")
            continue

        result = combine(a, b)

        if result:
            if result not in discovered:
                discovered.append(result)
                print(f"✨ New discovery: {result}!")
            else:
                print(f"✔ You already discovered {result}.")
        else:
            print("❌ Nothing happened...")

        save_game(discovered)

    print("Game saved. Goodbye!")


if __name__ == "__main__":
    main()