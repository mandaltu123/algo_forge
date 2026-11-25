import pytest
from arrays_and_hashing.p001_contains_duplicate import DuplicateDetection

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

@pytest.mark.parametrize("numbers, expected", TEST_CASES)
def test_contains_duplicate_hashing(numbers, expected):
    detection = DuplicateDetection()
    assert detection.contains_duplicate_hashing(numbers.copy()) == expected

@pytest.mark.parametrize("numbers, expected", TEST_CASES)
def test_contains_duplicate_brute_force(numbers, expected):
    detection = DuplicateDetection()
    assert detection.contains_duplicate_brute_force(numbers.copy()) == expected

@pytest.mark.parametrize("numbers, expected", TEST_CASES)
def test_contains_using_set_one_line(numbers, expected):
    detection = DuplicateDetection()
    assert detection.contains_using_set_one_line(numbers.copy()) == expected

@pytest.mark.parametrize("numbers, expected", TEST_CASES)
def test_find_duplicates_using_sorting(numbers, expected):
    detection = DuplicateDetection()
    assert detection.find_duplicates_using_sorting(numbers.copy()) == expected