"""
Runtime
122ms
Beats 42.21%of users with Python3

Memory
17.08MB
Beats 98.01%of users with Python3
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r = 0
        l = len(numbers) - 1
        while r < l:
            if numbers[r] + numbers[l] > target:
                l -= 1
            elif numbers[r] + numbers[l] < target:
                r += 1
            elif numbers[r] + numbers[l] == target:
                return [r+1,l+1]