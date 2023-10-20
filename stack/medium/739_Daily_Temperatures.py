"""
Runtime
1054ms
Beats 71.19%of users with Python3

Memory
30.40MB
Beats 76.27%of users with Python3
"""

# Time Complexity：O(n)
# Space Complexity：O(n)
# Approach 1：iterating through the temperatures list and using a stack to keep track of indices for potential higher temperatures in the future while calculating the number of days to wait.
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for currentDay in range(len(temperatures)):
            # If the current temperature is higher than the temperature at the top of the stack, we update the waiting days.
            while stack and temperatures[currentDay] > temperatures[stack[-1]]:
                j = stack.pop()
                result[j] = currentDay - j

            stack.append(currentDay)
        return result