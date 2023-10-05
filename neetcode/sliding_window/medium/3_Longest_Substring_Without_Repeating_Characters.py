"""
Runtime
3970ms
Beats 5.01%of users with Python3

Memory
16.37MB
Beats 66.38%of users with Python3
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l , r = 0,1
        count = 1
        while r < len(s):
            if l == r:
                r += 1
                continue
            if len(set(s[l:r+1])) == len(s[l:r+1]):
                count = max(count,len(s[l:r+1]))
                r += 1
            else:
                l += 1
                r = l +1

        return count