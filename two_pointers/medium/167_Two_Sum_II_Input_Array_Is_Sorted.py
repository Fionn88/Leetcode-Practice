"""
Runtime
122ms
Beats 42.21%of users with Python3

Memory
17.08MB
Beats 98.01%of users with Python3
"""
# Time Complexity：O(n)
# Space Complexity：O(1)
# Approach 1: Using two pointers to determine if they equal the target. The list is sorted. If the current value is greater than the target, move the right pointer to the left. If the current value is smaller than the target, move the left pointer to the right.
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        # If the current value is greater than the target, move the right pointer to the left. If the current value is smaller than the target, move the left pointer to the right.
        while l < r:
            if numbers[r] + numbers[l] > target:
                r -= 1
            elif numbers[r] + numbers[l] < target:
                l += 1
            elif numbers[r] + numbers[l] == target:
                return [l+1,r+1]