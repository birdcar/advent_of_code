"""
--- Day 2: Password Philosophy ---
Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers; we can't log in!" You ask if you can take a look.

Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc

Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?

--- Part Two ---
While it appears you validated the passwords correctly, they don't seem to be what the Official Toboggan Corporate Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job at the sled rental place down the street! The Official Toboggan Corporate Policy actually works a little differently.

Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.

How many passwords are valid according to the new interpretation of the policies?
"""
import re
from typing import Literal

from .utils import DATA_DIR, gen_inputs

RE_POLICY_PARSER = re.compile(
    r"""
    (?P<low>\d+)                    # Minimum number of times the target_char
                                    # must be present in password
    -
    (?P<high>\d+)                   # Maximum number of times target_char must
                                    # be present in password
    \s
    (?P<target_char>[a-zA-Z])       # The target_char
    :\s
    (?P<password>\w+)               # The user's password, in plain text 😬
    """,
    re.VERBOSE,
)


def sled_rental_password_validity(password_policy: str) -> Literal[0, 1]:
    """
    Returns a 1 if a given password is valid according to its policy at the
    time, and a 0 otherwise
    """
    match = RE_POLICY_PARSER.match(password_policy)
    low, high, target_char, password = (
        int(match.group("low")),
        int(match.group("high")),
        match.group("target_char"),
        match.group("password"),
    )
    appearance_count = password.count(target_char)

    return 1 if low <= appearance_count <= high else 0


def toboggan_password_validity(password_policy: str) -> Literal[0, 1]:
    """
    Returns a 1 if a given password is valid according to its policy at the
    time, and a 0 otherwise
    """
    match = RE_POLICY_PARSER.match(password_policy)
    low, high, target_char, password = (
        int(match.group("low")),
        int(match.group("high")),
        match.group("target_char"),
        match.group("password"),
    )
    first_position = password[low - 1] == target_char
    second_position = password[high - 1] == target_char

    return (
        1
        if (first_position or second_position)
        and not (first_position and second_position)
        else 0
    )


if __name__ == "__main__":
    # part one
    inputs = gen_inputs(DATA_DIR / "day2.txt", map_fn=sled_rental_password_validity)
    print("Part One =>", sum(inputs))

    # part two
    inputs = gen_inputs(DATA_DIR / "day2.txt", map_fn=toboggan_password_validity)
    print("Part Two =>", sum(inputs))