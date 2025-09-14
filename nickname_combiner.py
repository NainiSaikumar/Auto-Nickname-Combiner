"""Nickname Combiner - generates fun nicknames from two names."""

import random


def style_basic(name1: str, name2: str) -> str:
    """First 2 letters of name1 + last 2 letters of name2."""
    return name1[:2] + name2[-2:]


def style_half(name1: str, name2: str) -> str:
    """First half of name1 + second half of name2."""
    half1 = len(name1) // 2
    half2 = len(name2) // 2
    return name1[:half1] + name2[half2:]


def style_three(name1: str, name2: str) -> str:
    """First 3 letters of each name."""
    return name1[:3] + name2[:3]


def style_random(name1: str, name2: str) -> str:
    """Random 5 characters from both names."""
    pool = name1 + name2
    if not pool:  # if both empty
        pool = "nick"
    return "".join(random.choice(pool) for _ in range(5))


def nickname_generator():
    """Interactive nickname generator with history."""
    history = []

    while True:
        print("\n--- Nickname Combiner ---")
        name1 = input("Enter first name (or 'exit' to quit): ").strip()
        if name1.lower() == "exit":
            print("Goodbye!")
            break

        name2 = input("Enter second name: ").strip()

        nicknames = [
            style_basic(name1, name2),
            style_half(name1, name2),
            style_three(name1, name2),
            style_random(name1, name2),
        ]

        print("\nNickname Suggestions:")
        for i, nick in enumerate(nicknames, start=1):
            print(f"{i}. {nick}")
            history.append(nick)

        print("\nHistory so far:", ", ".join(history))


if __name__ == "__main__":
    nickname_generator()
