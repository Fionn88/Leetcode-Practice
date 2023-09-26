"""
Runtime
398ms
Beats 51.93%of users with Python3

Memory
33.81MB
Beats 15.07%of users with Python3
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(set(nums)) == 0:
            return 0
        elif len(set(nums)) == 1:
            return 1
        else:
            nums = sorted(set(nums))
            print(nums)
        
        L = []

        for index,value in enumerate(nums):
            if index == 0:
                count = 1
                L.append(count)
                current = value
            elif current + 1 == value:
                count += 1
                L.append(count)
                current = value
            else:
                current = value
                count = 1
                L.append(count)
        return max(L)
"""
Runtime
355ms
Beats 85.93%of users with Python3

Memory
30.99MB
Beats 86.80%of users with Python3

不使用排序，並且用 -1 +1 的方式
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        answer = 0
        nums_set = set(nums)
        
        for i in nums_set:
            if i-1 not in nums_set:
                now = 1
                while (now+i) in nums_set:
                    now += 1
                answer = max(answer,now)
        return answer