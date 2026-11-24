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


class DuplicateDetection:
    def containsDuplicate(self, nums: list[int]) -> bool:
        if len(nums) == 0:
            print("no number present in the list")
            return False

        lookupSet = set()
        for num in nums:
            if num in lookupSet:
                return True
                break
            else:
                lookupSet.add(num)
        return False


if __name__ == "__main__":
    detection = DuplicateDetection()
    numbers = [1, 2, 3, 1]
    print(detection.containsDuplicate(numbers))
