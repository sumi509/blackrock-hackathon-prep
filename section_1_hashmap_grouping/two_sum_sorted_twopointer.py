"""
Problem: Two Sum II (Sorted Input)
Pattern: Two Pointer Technique

Why Important:
When financial data is already sorted (timestamps, prices, IDs),
we should avoid extra memory and scan efficiently.

Approach:
Use two pointers from both ends.
If sum too large → move right pointer
If sum too small → move left pointer

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = numbers
        left, right = 0, len(nums) - 1

        while left < right:
            s = nums[left] + nums[right]

            if s == target:
                return [left + 1, right + 1]  # 1-based indexing
            elif s > target:
                right -= 1
            else:
                left += 1

        return []  # safety
