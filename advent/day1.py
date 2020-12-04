"""
--- Day 1: Report Repair ---
After saving Christmas five years in a row, you've decided to take a vacation at a nice resort on a tropical island. Surely, Christmas will go on without you.

The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of a starfish; the locals just call them stars. None of the currency exchanges seem to have heard of them, but somehow, you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.

To save your vacation, you need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456
In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?
"""
from itertools import combinations
from math import prod
from pathlib import Path
from typing import Generator, Iterable, Tuple

from . import DATA_DIR


def gen_inputs(file_path: Path) -> Generator[int, None, None]:
    """
    Gather input data from a file and yield each line as an int
    """
    with open(file_path) as f:
        yield from (int(line.strip()) for line in f)


def find_n_complement_values(nums: Iterable[int], target: int, n_terms: int) -> tuple:
    """
    Given an iterable of integers, a target number, and a number of terms;
    return a Tuple of integers representing the combination of terms found
    in the iterable that -- when summed together -- equal the target integer.

    If no match is found, return a tuple of zeros with a length equal to
    n_terms.
    """
    product_filter = lambda combination: sum(combination) == target
    possible_combinations = combinations(nums, n_terms)

    try:
        return next(filter(product_filter, possible_combinations))

    except StopIteration:
        return tuple([0] * n_terms)


if __name__ == "__main__":
    answer_one = prod(
        find_n_complement_values(gen_inputs(DATA_DIR / "day1.txt"), 2020, 2)
    )
    print(f"{answer_one = }" if answer_one != 0 else "No solution for part one")

    answer_two = prod(
        find_n_complement_values(gen_inputs(DATA_DIR / "day1.txt"), 2020, 3)
    )
    print(f"{answer_two = }" if answer_two != 0 else "No solution for part two")
