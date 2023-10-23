"""
Runtime
134ms
Beats 31.52%of users with Python3

Memory
16.44MB
Beats 28.28%of users with Python3
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
    
"""
Runtime
99ms
Beats 62.60%of users with Python3

Memory
16.29MB
Beats 87.60%of users with Python3
"""    

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)
            maxf = max(maxf, count[s[r]])
            print(maxf,count)
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            print(res)
            res = max(res, r - l + 1)
        return res
    