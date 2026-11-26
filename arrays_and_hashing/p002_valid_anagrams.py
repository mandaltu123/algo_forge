"""
https://leetcode.com/problems/valid-anagram/description/?utm_source=chatgpt.com
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false



Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""

class ValidAnagram:
    def is_anagram(self, s: str, t: str) -> bool:
        """"
        Sorting	O(n log n)	O(n)	Simplest implementation
        """
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

if __name__ == "__main__":
    detect = ValidAnagram()
    s = "paparoach"
    t = "roachpapa"
    f = "papajohns"
    print(detect.is_anagram(s, t))
    print(detect.is_anagram(s, f))