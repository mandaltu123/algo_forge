import pytest

from arrays_and_hashing.p002_valid_anagrams import ValidAnagram

TEST_CASES = [
    ([1, 2, 3, 1], True),
    ([1, 2, 3, 4], False),
    ([1], False),
    ([5, 5], True),
    ([], False),
    ([-1, -2, -1], True),
    ([0, 0], True),
    ([7, 7, 7, 7], True),
    ([1, 2, 3, 4, 5, 5], True),
]