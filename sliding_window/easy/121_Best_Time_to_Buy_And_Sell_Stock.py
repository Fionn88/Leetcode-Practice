"""
Runtime
901ms
Beats 19.22%of users with Python3

Memory
27.25MB
Beats 80.95%of users with Python3
"""

# Time Complexity：O(n)
# Space Complexity：O(1)
# Approach 1 ：Using the sliding window approach to find the best selling point for the right maximum value and the left minimum value.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l , r = 0,1
        maxP = 0
        # When the right pointer goes beyond the last element, stop the loop.
        while r < len(prices):
            if l == r:
                r += 1
                continue
            # If the number on the left is greater than the number on the right, move the left pointer one step.
            if prices[l] > prices[r]:
                l += 1
            # If the above conditions are not met, determine if it maximizes the profit.
            else:
                maxP = max(maxP,prices[r] - prices[l])
                r += 1
        return maxP
            