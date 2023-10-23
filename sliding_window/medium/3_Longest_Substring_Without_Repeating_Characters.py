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
            # 複製字串就是複雜度
            cutWord = s[l:r+1]
            if len(set(cutWord)) == len(cutWord):
                count = max(count,len(cutWord))
                r += 1
            else:
                l += 1
                r = l +1

        return count
    
"""
Runtime
59ms
Beats 67.60%of users with Python3

Memory
16.32MB
Beats 65.96%of users with Python3
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 如字串都無重複直接 return 字串長度
        if len(set(s)) == len(s):                  
            return len(s)
        substring = ''
        maxLen = 1
        # 走訪該字串
        for i in s:
            # 如果字串中沒有出現在 子字串中
            if i not in substring:   
                # 把字串加進字串裡                   
                substring = substring + i
                # 更新並計算最大長度
                maxLen = max(maxLen, len(substring))   
            else:
                # 如在字串內 
                # 更新 substring
                substring = substring.split(i)[1] + i   
                
        return maxLen
    
"""
Runtime
54ms
Beats 85.12%of users with Python3

Memory
16.19MB
Beats 99.09%of users with Python3

The Sample Answer
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = set()
        l = 0
        maxN = 0
        for r in range(len(s)):
            while s[r] in ans:
                ans.remove(s[l])
                l += 1
            ans.add(s[r])
            maxN = max(len(ans),maxN)
                
        return maxN
    