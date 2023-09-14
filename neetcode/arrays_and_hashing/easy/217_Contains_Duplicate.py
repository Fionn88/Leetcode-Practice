"""
Runtime
483ms
Beats 51.94% of users with Python3

Memory
Details
30.86MB
Beats 83.18%of users with Python3
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(list(set(nums))) != len(nums)
    
