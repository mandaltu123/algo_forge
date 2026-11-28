
"""
Problem 002: Valid Anagram
LeetCode 242
https://leetcode.com/problems/valid-anagram/

Category: Arrays and Hashing

Problem Description:
    Given two strings s and t, return True if t is an anagram of s,
    otherwise return False.

    An anagram contains exactly the same characters with exactly
    the same frequencies, regardless of their order.

Examples:
    s = "anagram", t = "nagaram" -> True
    s = "rat",     t = "car"     -> False

Problem-solving Patterns:
    1. Sorting
    2. Hashing-based frequency counting
    3. Reverse frequency counting
    4. Direct addressing
    5. Parallel iteration using zip()
    6. Standard library frequency counting

Complexity Analysis:
+---------------------------+------------+--------+------------------------------------------+
| Algorithm                 | Time       | Space  | Description                              |
+---------------------------+------------+--------+------------------------------------------+
| Sorting                   | O(n log n) | O(n)   | Sort both strings and compare.           |
| Two Dictionaries          | O(n)       | O(k)   | Build and compare frequency dictionaries.|
| Reverse Counting          | O(n)       | O(k)   | Increment and decrement one dictionary.  |
| Fixed Frequency Array     | O(n)       | O(1)   | Map characters to 26 array indices.      |
| Frequency Array with Zip  | O(n)       | O(1)   | Process both strings in a single loop.   |
| collections.Counter       | O(n)       | O(k)   | Compare built-in frequency counters.     |
+---------------------------+------------+--------+------------------------------------------+

Notation:
    n = Length of each input string.
    k = Number of distinct characters across both strings.

Complexity Notes:
    - Space complexity refers to auxiliary space.
    - Dictionary operations assume average-case O(1) access.
    - Sorting complexity represents worst-case running time.
    - For lowercase English letters, k <= 26.
      Therefore, O(k) simplifies to O(1).
    - Fixed-size frequency arrays assume lowercase English letters.
    - Dictionary and Counter approaches support Unicode code points.
    - Combining loops reduces loop iterations, not frequency updates.
    - Actual execution performance requires benchmarking.

Python Concepts Covered:
    - sorted()
    - dict.get()
    - dict.keys()
    - dict.values()
    - dict.items()
    - Dictionary equality
    - List initialization using multiplication
    - ord()
    - Character-to-index mapping
    - Direct addressing
    - zip()
    - collections.Counter
    - Type annotations
    - First-class functions
    - Parametrized unit testing using pytest
    - Module-level docstrings
    - __name__ == "__main__"

Interview Recommendations:
    - Sorting: Simple baseline solution.
    - Dictionary: Flexible character-frequency solution.
    - Reverse counting: Avoids maintaining two dictionaries.
    - Frequency array: Optimal for a known, bounded alphabet.
    - Counter: Concise, idiomatic Python solution.
"""

import collections


# -------------------------------------------------------------------
# Helper Function: Character Frequency Dictionary
# -------------------------------------------------------------------


def prepare_char_count_dict(input_str: str) -> dict[str, int]:
    """
    Build a dictionary containing the frequency of each character.

    Time Complexity: O(n) average
    Space Complexity: O(k)
    """
    lookup_dict = {}

    for char in input_str:
        lookup_dict[char] = lookup_dict.get(char, 0) + 1

    return lookup_dict


# -------------------------------------------------------------------
# Approach 1: Sorting
# -------------------------------------------------------------------


def is_anagram_sorting(s: str, t: str) -> bool:
    """
    Sort both strings and compare their sorted character sequences.

    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    if len(s) != len(t):
        return False

    # Anagrams produce identical sequences after sorting.
    return sorted(s) == sorted(t)


# -------------------------------------------------------------------
# Approach 2: Two Frequency Dictionaries
# -------------------------------------------------------------------


def is_anagram_dictionary(s: str, t: str) -> bool:
    """
    Build separate frequency dictionaries and compare them.

    Time Complexity: O(n) average
    Space Complexity: O(k)
    """
    if len(s) != len(t):
        return False

    # Dictionary equality compares keys and their associated values,
    # regardless of insertion order.
    return prepare_char_count_dict(s) == prepare_char_count_dict(t)


# -------------------------------------------------------------------
# Approach 3: Single Dictionary - Reverse Counting
# -------------------------------------------------------------------


def is_anagram_reverse_counting(s: str, t: str) -> bool:
    """
    Increment frequencies using the first string and decrement
    frequencies using the second string.

    All frequencies must be zero for the strings to be anagrams.

    Time Complexity: O(n) average
    Space Complexity: O(k)
    """
    if len(s) != len(t):
        return False

    lookup_dictionary = {}

    # Count characters in the first string.
    for char in s:
        lookup_dictionary[char] = lookup_dictionary.get(char, 0) + 1

    # Decrement frequencies using the second string.
    for char in t:
        lookup_dictionary[char] = lookup_dictionary.get(char, 0) - 1

    # A nonzero frequency indicates a character-count mismatch.
    for value in lookup_dictionary.values():
        if value != 0:
            return False

    return True


# -------------------------------------------------------------------
# Approach 4: Fixed-size Frequency Array - Direct Addressing
# -------------------------------------------------------------------


def is_anagram_fixed_sized_frequency_array(s: str, t: str) -> bool:
    """
    Use a fixed-size frequency array instead of a hash table.

    Character-to-index mapping:
        'a' -> ord('a') - ord('a') -> 0
        'b' -> ord('b') - ord('a') -> 1
        'z' -> ord('z') - ord('a') -> 25

    Constraint:
        Both strings must contain only lowercase English letters.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if len(s) != len(t):
        return False

    # Initialize 26 frequency slots, one for each English letter.
    frequency = [0] * 26

    # Increment character frequencies using the first string.
    for char in s:
        index = ord(char) - ord('a')
        frequency[index] += 1

    # Decrement character frequencies using the second string.
    for char in t:
        index = ord(char) - ord('a')
        frequency[index] -= 1

    # Positive or negative frequencies indicate a mismatch.
    for value in frequency:
        if value != 0:
            return False

    return True


# -------------------------------------------------------------------
# Approach 5: Fixed-size Frequency Array - Combined Iteration
# -------------------------------------------------------------------


def is_anagram_fixed_sized_frequency_array_one_iteration(
    s: str,
    t: str,
) -> bool:
    """
    Process both strings simultaneously using zip().

    zip() returns a lazy iterator containing pairs of characters,
    avoiding the creation of an intermediate list.

    Constraint:
        Both strings must contain only lowercase English letters.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Note:
        Combining two loops reduces loop iterations from 2n to n,
        but the total number of frequency updates remains 2n.
        This does not change the asymptotic time complexity.
    """
    if len(s) != len(t):
        return False

    frequency = [0] * 26

    # Process corresponding characters from both strings.
    for char_s, char_t in zip(s, t):
        index_for_s = ord(char_s) - ord('a')
        index_for_t = ord(char_t) - ord('a')

        frequency[index_for_s] += 1
        frequency[index_for_t] -= 1

    # Negative frequencies during iteration are valid because
    # subsequent characters may balance them.
    # Validate frequencies only after processing both strings.
    for value in frequency:
        if value != 0:
            return False

    return True


# -------------------------------------------------------------------
# Approach 6: Standard Library - collections.Counter
# -------------------------------------------------------------------


def is_anagram_using_collection_counter(s: str, t: str) -> bool:
    """
    Use Python's built-in Counter to calculate character frequencies.

    Counter is a dictionary subclass designed for counting
    hashable elements.

    Example:
        Counter("aabbc") -> Counter({'a': 2, 'b': 2, 'c': 1})

    Time Complexity: O(n) average
    Space Complexity: O(k)
    """
    if len(s) != len(t):
        return False

    return collections.Counter(s) == collections.Counter(t)


# -------------------------------------------------------------------
# Manual Execution
# -------------------------------------------------------------------


if __name__ == "__main__":
    test_cases = [
        ("paparoach", "roachpapa", True),
        ("paparoach", "papajohns", False),
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("aabb", "abbb", False),
        ("", "", True),
        ("abc", "abcd", False),
        ("a", "a", True),
        ("a", "b", False),
        ("az", "za", True),
    ]

    # Python functions are first-class objects.
    # They can be stored in collections and invoked dynamically.
    algorithms = [
        is_anagram_sorting,
        is_anagram_dictionary,
        is_anagram_reverse_counting,
        is_anagram_fixed_sized_frequency_array,
        is_anagram_fixed_sized_frequency_array_one_iteration,
        is_anagram_using_collection_counter,
    ]

    for algorithm in algorithms:
        print(f"\nAlgorithm: {algorithm.__name__}")
        print("-" * 70)

        for s, t, expected in test_cases:
            result = algorithm(s, t)
            status = "PASSED" if result == expected else "FAILED"

            print(
                f"s={s!r:14} "
                f"t={t!r:14} "
                f"Expected={str(expected):5} "
                f"Actual={str(result):5} "
                f"{status}"
            )
