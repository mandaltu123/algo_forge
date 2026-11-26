import pytest

from arrays_and_hashing.p002_valid_anagrams import (
    is_anagram_sorting,
    is_anagram_dictionary,
)


TEST_CASES = [
    ("anagram", "nagaram", True),
    ("rat", "car", False),
    ("paparoach", "roachpapa", True),
    ("aabb", "abbb", False),
    ("", "", True),
]


@pytest.mark.parametrize("algorithm", [
    is_anagram_sorting,
    is_anagram_dictionary,
])
@pytest.mark.parametrize("s, t, expected", TEST_CASES)
def test_valid_anagram(algorithm, s, t, expected):
    assert algorithm(s, t) == expected