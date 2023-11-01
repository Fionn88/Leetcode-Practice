"""
Runtime
386ms
Beats 25.19%of users with Python3

Memory
17.82MB
Beats 56.05%of users with Python3
"""

# Time complexity: O(n * log n)
# Space Complexity：O(1)
# Approach 1 ：To obtain the minimum value of 'bananas-per-hour' using Binary Search, we determine the 'k' value.
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1,max(piles)
        res = r

        while l <= r:
            k = (l + r) //2
            hours = 0
            for p in piles:
                # Divide the number of bananas by the amount you can eat at once to calculate how many hours it takes to eat this pile of bananas.
                hours += math.ceil(p / k)

            # If it's less than or equal to the time the guard comes back, update the minimum value in 'res'.
            if hours <= h:
                res = min(res,k)
                r = k - 1
            else:
                l = k + 1
            
        return res
