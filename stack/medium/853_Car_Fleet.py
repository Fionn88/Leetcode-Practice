"""
Runtime
723ms
Beats 89.08%of users with Python3

Memory
39.43MB
Beats 21.75%of users with Python3
"""

# Time Complexity：O(nlogn)
# Space Complexity：O(n)
# Approach 1：Sorting the positions of cars and calculating the time it takes for each car to reach the finish line, determining if the trailing cars catch up with the preceding one, and popping out elements, then calculating the length as the answer.
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        mix = sorted(zip(position, speed), reverse=True)
        stack = []
        for p,s in mix:
            stack.append((target - p) / s)
            # determining if the trailing cars catch up with the preceding one, and popping out elements
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
