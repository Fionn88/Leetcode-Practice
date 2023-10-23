"""
Runtime O(N log N)
56ms
Beats 57.16% of users with Python3

Memory
17.54MB
Beats 15.23% of users with Python3
"""

# Time Complexity：O(nlog(n))
# Space Complexity：O(1)
# Approach 1 ：Sorting both strings and then checking if they are the same.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

# Time Complexity：O(n)
# Space Complexity：O(1)
# Approach 2 ：Checking if the frequency of letters in both strings is the same.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
    