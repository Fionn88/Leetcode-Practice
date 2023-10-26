"""
Runtime
Details
52ms
Beats 44.03%of users with Python3
Memory
Details
16.67MB
Beats 93.66%of users with Python3
"""

# Time Complexity： O(log(m * n))
# Space Complexity：O(1)
# Approach 1 ：For each item in the list, then use binary search to find the target.
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for nums in matrix:
            l = 0 
            r = len(nums) - 1
            while l <= r:
                mid = (l+r) // 2
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    return True

        return False
        