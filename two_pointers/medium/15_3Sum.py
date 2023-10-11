"""
Runtime
941ms
Beats 79.15%of users with Python3

Memory
20.33MB
Beats 81.51%of users with Python3

運用 Two_Sum_II_Input_Array_Is_Sorted.py 的方法
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()        
        res = []
        print(nums)

        for index,value in enumerate(nums):
            # 如果當前值等於前一個值，則跳過，以避免重複計算
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
                    # 接下來，確保我們不再添加重複的三數之和到結果中
                    while nums[l] == nums[l-1] and l < r :
                        l += 1
        return res