"""
Runtime
65ms
Beats 79.62%of users with Python3

Memory
17.30MB
Beats 38.63%of users with Python3
"""

# Time Complexity：O(n)
# Space Complexity：O(1)
# Approach 1 ：When creating the answer list, sequentially append characters while making a condition check.
class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        res = []
        for value in s:
            # If the answer list is empty or the last character of the string is not equal to the current character, then add the current character to the answer list.
            if not res or value != res[-1]: 
                res.append(value)
            else:
                res.pop()
        return ''.join(res)