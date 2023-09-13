"""
Runtime
2797ms
Beats 16.91% of users with Python3

Memory
17.00MB
Beats 99.21% of users with Python3
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for front_index in range(len(nums)-1):
            for behine_index in range(front_index+1,len(nums)):
                if nums[front_index] + nums[behine_index] == target:
                    ans.append(front_index)
                    ans.append(behine_index)
                    break
        return ans