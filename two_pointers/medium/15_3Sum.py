"""
Runtime
941ms
Beats 79.15%of users with Python3

Memory
20.33MB
Beats 81.51%of users with Python3

運用 Two_Sum_II_Input_Array_Is_Sorted.py 的方法
"""
# Time Complexity：O(n)
# Space Complexity：O(1)
# Approach 1: After sorting the list, using it as the third value in a loop, and then using two pointers to move and find if three numbers equal to 0.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()        
        res = []
        print(nums)

        for index,value in enumerate(nums):
            # If the current value is equal to the previous value, skip it to avoid redundant calculations.
            if index > 0 and value == nums[index-1]:
                continue
            r = len(nums) - 1
            l = index + 1
            while l < r:
                threesum = value + nums[r] + nums[l]
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    res.append([value,nums[r],nums[l]])
                    l += 1
                    # Ensure that we do not add duplicate three-sums to the result.
                    while nums[l] == nums[l-1] and l < r :
                        l += 1
        return res