"""
Runtime
43ms
Beats 49.77%of users with Python3

Memory
16.57MB
Beats 72.05%of users with Python3
"""
# Time Complexity：O(4^n/n^(1/2))
# Space Complexity：O(1)
# Approach 1：Generate all possible combinations of parentheses using a recursive backtracking approach.
# Q: Why does this generate all possible combinations?
# A: 
# combinations of 3: 
# | (0,0)(1,0)(1,1)(2,1)(2,2)(3,2)(3,3)
# | (0,0)(1,0)(1,1)(2,1)(3,1)(3,2)(3,3)
# | (0,0)(1,0)(2,0)(2,1)(2,2)(3,2)(3,3)
# | (0,0)(1,0)(2,0)(2,1)(3,1)(3,2)(3,3)
# | (0,0)(1,0)(2,0)(3,0)(3,1)(3,2)(3,3)

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def backtrack(s, left, right):
            # Check the validity of parentheses.
            if len(s) == 2 * n:
                result.append(s) 
                return
            if left < n:
                backtrack(s + '(', left + 1, right)
            if right < left:
                backtrack(s + ')', left, right + 1)
        # Starting from an empty string, recursively add left and right parentheses.
        backtrack('', 0, 0)
        return result
