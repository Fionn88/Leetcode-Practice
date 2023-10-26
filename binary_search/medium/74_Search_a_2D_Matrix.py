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

# Time Complexity： O(m log n)
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

"""
Runtime
57ms
Beats 12.02%of users with Python3

Memory
16.70MB
Beats 93.66%of users with Python3
"""

# Time Complexity： O(n^2)
# Space Complexity：O(1)
# Approach 2：Traverse the two-dimensional array and flatten it into a one-dimensional array, then perform a binary search to find the target.
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flattened_list = [item for sublist in matrix for item in sublist]
        l = 0 
        r = len(flattened_list) - 1
        while l <= r:
            mid = (l+r) // 2
            if flattened_list[mid] < target:
                l = mid + 1
            elif flattened_list[mid] > target:
                r = mid - 1
            else:
                return True

        return False

"""
Runtime
44ms
Beats 89.31%of users with Python3

Memory
16.62MB
Beats 93.66%of users with Python3
"""

# Time Complexity： O(log(m * n))
# Space Complexity：O(1)
# Approach 3：First, use binary search to search the rows to find out if the target exists within a row's range, and then search the range within that row using binary search.
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if matrix[row][-1] < target:
                top = row + 1
            elif matrix[row][0] > target:
                bot = row - 1
            else:
                # If the conditions mentioned earlier are not satisfied, it indicates that the corresponding row has been located.
                break

        # If the loop doesn't exit due to a "break," it means that the target range doesn't exist.
        if not (top <= bot):
            return False
        mid = (top + bot) // 2
        l, r = 0, COLS - 1
        # Search the range within that row using binary search.
        while l <= r:
            m = (l+r) // 2
            if matrix[mid][m] < target:
                l = m + 1
            elif matrix[mid][m] > target:
                r = m - 1
            else:
                return True

        return False
    