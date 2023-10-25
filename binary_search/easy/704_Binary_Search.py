"""
Runtime
217ms
Beats 40.19%of users with Python3

Memory
17.60MB
Beats 95.65%of users with Python3
"""

# Time Complexity： O(log n)
# Space Complexity：O(1)
# Approach 1 ：Using binary search to find the target. If the search value is greater than the middle value, increment the middle index and select the right half. If the search value is less than the middle value, increment the middle index and select the left half. Continue this process until the search value matches the middle value, then return the result.
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) - 1
        while l <= r:
            mid = (l+r) // 2
            # If the search value is greater than the middle value, increment the middle index and select the right half.
            if nums[mid] < target:
                l = mid + 1
            # If the search value is less than the middle value, increment the middle index and select the left half. 
            elif nums[mid] > target:
                r = mid - 1
            # Continue this process until the search value matches the middle value, then return the result.
            else:
                return mid
        return -1

