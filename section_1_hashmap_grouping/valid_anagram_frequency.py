"""
Problem: Valid Anagram
Pattern: Frequency Counting (HashMap)

My Understanding:
I build frequency maps for both strings and compare them.
If both maps match → strings contain same characters with same counts.

Why this matters in financial systems:
Used to verify two datasets contain identical records regardless of order
(e.g., reconciliation between two systems).

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dict_s = {}
        for ele in s:
            if ele in dict_s:
                dict_s[ele]+=1
            else:
                dict_s[ele]=1

        dict_t = {}
        for ele in t:
            if ele in dict_t:
                dict_t[ele]+=1
            else:
                dict_t[ele]=1

        if dict_s == dict_t:
            return True
        else:
            return False
