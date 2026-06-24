"""
Blossom Guess — a cute little word-guessing game.

How to play:
- The game picks a secret word.
- You guess letters one at a time.
- Each wrong guess wilts the flower a little.
- Guess all the letters before the flower fully wilts!

Run it with: python blossom_guess.py
"""

import random

WORD_BANK = {
    "easy": ["pink", "sweet", "cloud", "berry", "sunny", "happy", "peach", "petal"],
    "medium": ["sparkle", "blossom", "ribbon", "lullaby", "marigold", "twinkle", "cherry"],
    "hard": ["strawberry", "watermelon", "butterfly", "raspberry", "chrysanthemum"],
}

MAX_LIVES = 6

STAGES = [
    """
       \\   |   /
        \\  |  /
     ----( ❀ )----
        /  |  \\
       /   |   \\
    """,
    """
       \\   |
        \\  |
     ----( ❀ )----
        /  |
       /   |
    """,
    """
           |
           |
     ----( ❀ )----
           |
           |
    """,
    """
           |
           |
     ----( ❁ )
           |
           |
    """,
    """
           |
           |
        ( ❁
           |
           |
    """,
    """
           .
           .
          (.)
           .
           .
    """,
    """
           .
           .
           .
           .
           .
    """,
]


def pick_word():
    print("\nChoose a difficulty:")
    print("  1) easy")
    print("  2) medium")
    print("  3) hard")

    choice = input("Your choice (1-3): ").strip()
    difficulty = {"1": "easy", "2": "medium", "3": "hard"}.get(choice, "easy")
    word = random.choice(WORD_BANK[difficulty])
    print(f"\nAlright — a {difficulty} word has been picked. ✿\n")
    return word.lower()


def display_progress(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)


def play_round():
    word = pick_word()
    guessed_letters = set()
    wrong_guesses = 0

    while wrong_guesses < MAX_LIVES:
        stage_index = min(wrong_guesses, len(STAGES) - 1)
        print(STAGES[stage_index])
        print("Word:", display_progress(word, guessed_letters))
        print(f"Lives left: {MAX_LIVES - wrong_guesses}")

        if set(word) <= guessed_letters:
            print(f"\n🌸 You guessed it! The word was '{word}'. Yay!\n")
            return True

        guess = input("Guess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print("You already tried that letter — try a new one.\n")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Yes! '{guess}' is in the word.\n")
        else:
            wrong_guesses += 1
            print(f"Sorry, no '{guess}' here. The flower wilts a little...\n")

    print(STAGES[-1])
    print(f"The flower has wilted. The word was '{word}'. Better luck next time!\n")
    return False


def main():
    print("=" * 40)
    print("   🌷  BLOSSOM GUESS  🌷")
    print("=" * 40)
    print("Guess the secret word before the flower wilts!")

    wins = 0
    rounds = 0

    while True:
        rounds += 1
        if play_round():
            wins += 1

        print(f"Score so far: {wins} win(s) out of {rounds} round(s)")
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            break

    print("\nThanks for playing Blossom Guess! ✿ See you next time.")


if __name__ == "__main__":
    main()