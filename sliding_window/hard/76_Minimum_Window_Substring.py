"""
Time Limit Exceeded
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        elif s == t:
            return s
        elif t in s:
            return t
        elif len(t) == 1:
            if t in s:
                return t
            else:
                return ""

        counterT = Counter(t)
        l = 0
        r = 1
        D = {}
        D[s[l]] = 1
        length = 100000
        ans = ""
        while r < len(s) and l < r:
            D[s[r]] = D.get(s[r], 0) + 1

            intersection = {key: min(D[key], counterT[key]) for key in D if key in counterT}
            if intersection == counterT:
                length = min(length,r - l + 1)
                ans = s[l:r+1]

            if r - l + 1 >= length:
                l += 1
                r = l + 1
                D = {}
                D[s[l]] = 1
            elif r == len(s) - 1 and l != len(s) -2:
                l += 1
                r = l + 1
                D = {}
                D[s[l]] = 1
            else:
                r += 1

        return ans
"""
Runtime
90ms
Beats 95.71%of users with Python3

Memory
17.14MB
Beats 45.53%of users with Python3
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""