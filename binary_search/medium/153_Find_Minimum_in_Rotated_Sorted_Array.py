"""
Runtime
45ms
Beats 72.27%of users with Python3

Memory
16.68MB
Beats 22.59%of users with Python3
"""

# Time Complexity：O(log n)
# Space Complexity：O(1)
# Approach 1 ：Based on the characteristics of the list in the question, use binary search to find the minimum value.
class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        minimum = nums[0]
        while low <= high:
            # To verify if the interval has the minimum serialization and, if it meets the criteria, calculate and update the minimum value.
            if nums[low] < nums[high]:
                minimum = min(nums[low],minimum)
                break

            mid = (low + high) // 2
            minimum = min(nums[mid], minimum)
            
            # When the middle value is greater than the lowest point number, then search the right half.
            if nums[mid] >= nums[low]:
                low = mid + 1
            else:
                high = mid - 1

        return minimum