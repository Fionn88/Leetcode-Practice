"""
Runtime
901ms
Beats 19.22%of users with Python3

Memory
27.25MB
Beats 80.95%of users with Python3
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l , r = 0,1
        maxP = 0
        while r < len(prices):
            if l == r:
                r += 1
                continue
            if prices[l] > prices[r]:
                l += 1
            else:
                maxP = max(maxP,prices[r] - prices[l])
                r += 1
        return maxP
            