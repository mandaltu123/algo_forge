def prepare_char_count_dict(input_str: str) -> dict[str, int]:
    lookup_dict = {}

    for char in input_str:
        lookup_dict[char] = lookup_dict.get(char, 0) + 1

    return lookup_dict


def is_anagram_sorting(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    return sorted(s) == sorted(t)


def is_anagram_dictionary(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    return prepare_char_count_dict(s) == prepare_char_count_dict(t)


if __name__ == "__main__":

    s = "paparoach"
    t = "roachpapa"
    f = "papajohns"
    print(is_anagram_sorting(s, t))
    print(is_anagram_sorting(s, f))
    print("calling is_anagram_dictionary")

    print(is_anagram_dictionary(s, t))
    print(is_anagram_dictionary(s, f))