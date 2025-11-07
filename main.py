"""A larger demo entry-point for Intro_to_Python.

This file defines a "super big" demonstration function that showcases
many small Python features you might find helpful while learning.

Run this file with: python main.py
"""

from typing import List, Dict
import math
import os


def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def divide(a: float, b: float) -> float:
    """Divide a by b, raising a ValueError on division by zero."""
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError("Cannot divide by zero")


def factorial(n: int) -> int:
    """Compute factorial recursively (small demo; not optimized)."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)


def summarize_list(numbers: List[float]) -> Dict[str, float]:
    """Return a small summary (min, max, mean) for a list of numbers."""
    if not numbers:
        return {"min": 0.0, "max": 0.0, "mean": 0.0}
    return {
        "min": min(numbers),
        "max": max(numbers),
        "mean": sum(numbers) / len(numbers),
    }


def super_big_function(verbose: bool = True) -> None:
    """A large demonstration function that prints and returns little examples.

    It intentionally contains several small examples of common Python constructs:
    - arithmetic and helper functions
    - error handling
    - loops and list comprehensions
    - dictionaries and formatting
    - recursion
    - simple file I/O (writes and reads a tiny file)
    """

    if verbose:
        print("=== Super Big Function: Python Feature Demo ===\n")

    # Basic arithmetic
    a, b = 8, 3
    if verbose:
        print(f"Numbers: a={a}, b={b}")
        print("add(a, b) ->", add(a, b))
        try:
            print("divide(a, b) ->", divide(a, b))
        except ValueError as e:
            print("Division error:", e)

    # Demonstrate list handling and comprehensions
    numbers = [i * 0.5 for i in range(1, 11)]  # 0.5, 1.0, 1.5, ... 5.0
    summary = summarize_list(numbers)
    if verbose:
        print("\nList sample:", numbers)
        print("Summary:")
        for k, v in summary.items():
            print(f"  {k}: {v}")

    # Dictionary usage
    person = {"name": "Alex", "age": 29, "languages": ["Python", "SQL"]}
    if verbose:
        print("\nPerson dict:", person)

    # Loops and control flow
    evens = [n for n in range(20) if n % 2 == 0]
    if verbose:
        print("\nFirst 10 even numbers:", evens[:10])

    # Recursion example (factorial)
    n = 5
    try:
        fact_n = factorial(n)
        if verbose:
            print(f"\n{n}! = {fact_n}")
    except ValueError as e:
        print("Factorial error:", e)

    # Small math demonstration
    circle_radius = 2.5
    circle_area = math.pi * circle_radius ** 2
    if verbose:
        print(f"\nCircle with radius {circle_radius} has area {circle_area:.3f}")

    # File I/O (write then read) — uses a filename in the same directory
    filename = os.path.join(os.path.dirname(__file__), "example_output.txt")
    try:
        if verbose:
            print(f"\nWriting a short example file to: {filename}")
        with open(filename, "w", encoding="utf-8") as f:
            f.write("This is a small demo file.\n")
            f.write(f"Numbers summary: {summary}\n")

        if verbose:
            print("Reading the file back:")
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                if verbose:
                    print("  ", line.strip())
    except OSError as e:
        print("File I/O error:", e)

    if verbose:
        print("\n=== Demo complete ===")


def main() -> None:
    """Call the large demo function. Kept small so this file can be imported safely."""
    super_big_function(verbose=True)


if __name__ == "__main__":
    main()



