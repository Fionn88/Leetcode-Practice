"""
Memory Limit Exceeded
"""
from itertools import permutations
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) == len(s2):
            if Counter(s1) == Counter(s2):
                return True
            else:
                return False
        perm = list(permutations(s1))
        r = len(s1) - 1
        l = 0
        while r < len(s2):
            for i in perm:
                print(''.join(i),s2[l:r+1])
                if ''.join(i) == s2[l:r+1]:
                    return True
            l += 1
            r += 1
        return False
            
"""
Time Limit Exceeded
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        l = s2.index(s1[0])
        r = l + len(s1)
        while r < len(s2) :
            if s2[l:r] == s1 or s2[l:r] == reversed(s1):
                return True
            elif l == 0:
                l = s2.index(s1[0])
                r = l + len(s1)
                l += 1
                r += 1
            else:
                r -= 1
                l -= 1
        return False

"""
Runtime
65ms
Beats 75.40%of users with Python3

Memory
16.36MB
Beats 71.14%of users with Python3
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Count, s2Count = [0] * 26,[0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1
        l = 0
        for r in range(len(s1),len(s2)):
            if matches == 26:
                return True
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1
            
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26