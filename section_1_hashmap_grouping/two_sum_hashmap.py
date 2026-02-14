"""
Problem: Two Sum
Pattern: HashMap Lookup

Why Important:
Represents matching two financial entries whose sum balances a constraint
(e.g., debit-credit reconciliation).

Approach:
Store seen values in a dictionary.
For each number, check if the complement already exists.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            remaining = target - num

            if remaining in seen:
                return [seen[remaining], i]   # stop immediately once found

            seen[num] = i

        return []  # edge case safety
