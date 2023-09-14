"""
Runtime O(N^2)
2797ms
Beats 16.91% of users with Python3

Memory
17.00MB
Beats 99.21% of users with Python3
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for front_index in range(len(nums)-1):
            for behine_index in range(front_index+1,len(nums)):
                if nums[front_index] + nums[behine_index] == target:
                    return [front_index, behine_index]
        return [0,0]

"""
Runtime O(2N)
62ms
Beats 80.87% of users with Python3

Memory
Details
17.50MB
Beats 50.55% of users with Python3
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        D = dict()
        for i in range(len(nums)):
            D[nums[i]] = i
        for i in range(len(nums)-1):
            rest = target - nums[i]
            if D.get(rest) and i != D[rest]:
                return [i,D[rest]]

"""
Runtime O(N)
"""

# Two Pointer
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = 1
        while True:
            if nums[left] + nums[right] == target:
                return [left, right]
            right += 1
            if right == len(nums):
                left += 1
                right = left+1
                if left == len(nums):
                    break
        return [0, 0]
 