import pytest

from arrays_and_hashing.p002_valid_anagrams import (
    is_anagram_sorting,
    is_anagram_dictionary, is_anagram_reverse_counting, is_anagram_fixed_sized_frequency_array,
    is_anagram_fixed_sized_frequency_array_one_iteration, is_anagram_using_collection_counter,
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
    is_anagram_reverse_counting,
    is_anagram_fixed_sized_frequency_array,
    is_anagram_fixed_sized_frequency_array_one_iteration,
    is_anagram_using_collection_counter
])
@pytest.mark.parametrize("s, t, expected", TEST_CASES)
def test_valid_anagram(algorithm, s, t, expected):
    assert algorithm(s, t) == expected

