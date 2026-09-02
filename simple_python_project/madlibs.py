"""
A Mad Libs style word game.
Collects a few words from the user and inserts them
into a short pre-written story template.
"""


def main():
    print("=== Mad Libs ===")
    print("Answer the following prompts to build your story!\n")

    adjective = input("Enter an adjective: ").strip()
    noun = input("Enter a noun: ").strip()
    verb = input("Enter a verb (past tense): ").strip()
    place = input("Enter a place: ").strip()
    animal = input("Enter an animal: ").strip()

    story = (
        f"\nOnce upon a time, a {adjective} {noun} {verb} all the way to {place}. "
        f"There, it met a talking {animal}, and they became best friends forever.\n"
    )

    print(story)


if __name__ == "__main__":
    main()
