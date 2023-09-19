"""
Runtime O(N log N)
56ms
Beats 57.16% of users with Python3

Memory
17.54MB
Beats 15.23% of users with Python3
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)