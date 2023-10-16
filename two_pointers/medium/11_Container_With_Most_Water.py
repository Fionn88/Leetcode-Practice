"""
Runtime
592ms
Beats 70.34%of users with Python3

Memory
29.26MB
Beats 71.46%of users with Python3
"""
# Time Complexity：O(n)
# Space Complexity：O(1)
# Approach 1: Using two pointers to move the pointers and calculate the maximum area.
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        res = 0
        while l < r:
            # Obtaining the minimum height and multiplying it by the distances to the indices where the heights are.
            area = min(height[l], height[r]) * (r - l)
            res = max(res, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res

        