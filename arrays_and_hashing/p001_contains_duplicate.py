"""
https://leetcode.com/problems/contains-duplicate/description/?utm_source=chatgpt.com

https://leetcode.com/problems/contains-duplicate/

Given an integer array nums, return True if any value appears in the array or False if every
element is distinct.

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
from traceback import print_tb


class DuplicateDetection:
    def contains_duplicate_hashing(self, nums: list[int]) -> bool:
        lookup_set = set()

        for num in nums:
            if num in lookup_set:
                return True

            lookup_set.add(num)

        return False

    def contains_duplicate_brute_force(self, nums: list[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True

        return False

    def contains_using_set_one_line(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))

    def find_duplicates_using_sorting(self, nums: list[int]) -> bool:
        sorted_nums = sorted(nums)
        print(f"sorted numbers {sorted_nums}")
        n = len(sorted_nums)

        for i in range(n):
            try:
                if sorted_nums[i] == sorted_nums[i + 1]:
                    return True
            except:
                return False
        return False



if __name__ == "__main__":
    detection = DuplicateDetection()
    numbers = [1, 2, 1, 3, 1]
    distinct_numbers = [1, 2, 3, 4, 5, 6]
    print(detection.contains_duplicate_hashing(numbers))
    print(detection.contains_duplicate_brute_force(distinct_numbers))
    print(detection.contains_duplicate_brute_force(numbers))
    print(detection.find_duplicates_using_sorting(numbers))
    print(detection.find_duplicates_using_sorting(distinct_numbers))

