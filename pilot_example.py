#!/usr/bin/env python3
"""Small example script for the Copilot code-review pilot demo."""


def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b


def main() -> None:
    result = add(21, 21)
    print(f"21 + 21 = {result}")


if __name__ == "__main__":
    main()
