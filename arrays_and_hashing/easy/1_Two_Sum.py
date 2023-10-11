"""
Runtime O(N^2)
2797ms
Beats 16.91% of users with Python3

Memory
17.00MB
Beats 99.21% of users with Python3
"""
# Time Complexity：O(n^2)
# Space Complexity：O(1)
# Approach 1 ：Use two nested loops to find all possible combinations and then check if they equal the target.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # find first element
        for front_index in range(len(nums)-1):
            # find second element
            for behine_index in range(front_index+1,len(nums)):
                # check if they equal the target
                if nums[front_index] + nums[behine_index] == target:
                    return [front_index, behine_index]
        return [0,0]

"""
Runtime O(2N)
62ms
Beats 80.87% of users with Python3

Memory
Details
17.50MB
Beats 50.55% of users with Python3
"""

# Time Complexity：O(n)
# Space Complexity：O(1)
# Approach 2 ：Using key-value pairs to store values and their index, we can search the dictionary to see if there's a number that matches when subtracted from the target.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        D = dict()
        # Creating key-value pairs.
        for i in range(len(nums)):
            D[nums[i]] = i
        # Searching the dictionary to see if there's a number that matches when subtracted from the target
        for i in range(len(nums)-1):
            rest = target - nums[i]
            # Ensuring that the values and the two numbers found are not at the same index.
            if D.get(rest) and i != D[rest]:
                return [i,D[rest]]

# Time Complexity：O(n)
# Space Complexity：O(1)
# Approach 3 ：Use `Sliding Window` to find if the sum of two numbers equals the target.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = 1
        while True:
            # Check if they equal the target
            if nums[left] + nums[right] == target:
                return [left, right]
            # Move the right pointer one position to the right when it's not equal to the target.
            right += 1
            # When the right pointer is at the far right, move the left pointer to the right, and shift the right pointer to the right of the left pointer
            if right == len(nums):
                left += 1
                right = left+1
                # Stop the infinite loop if the left pointer is at the far right after moving.
                if left == len(nums):
                    break
        return [0, 0]
 