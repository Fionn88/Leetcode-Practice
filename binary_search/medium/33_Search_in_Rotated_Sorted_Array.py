"""
Runtime
52ms
Beats 23.66%of users with Python3

Memory
16.63MB
Beats 45.84%of users with Python3
"""

# Time Complexity： O(log n)
# Space Complexity：O(1)
# Approach 1 ：Using binary search to find the target. Move the pointers for the left and right points. First, check if it forms a segment for serialization.
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid

            # check if it forms a segment for serialization.
            if nums[low] <= nums[mid]:
                # If the target is greater than the middle pointer or the target is smaller than the left pointer, then search the right half.
                if target > nums[mid] or target < nums[low]:
                    low = mid + 1
                else:
                    high = mid - 1

                continue

            # If it's not serialized, and the middle pointer is greater than the target or the right pointer is smaller than the target, then search the left half.
            if target < nums[mid] or target > nums[high]:
               high = mid - 1
            else:
                low = mid + 1

        return -1
        