"""
Runtime
48ms
Beats 7.05%of users with Python3

Memory
16.26MB
Beats 72.06%of users with Python3
"""

# Time Complexity：O(n)
# Space Complexity：O(1)
# Approach 1 ：Create a valid parenthesis dictionary and check if the last value is the corresponding parenthesis when adding a right parenthesis.
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  
        D = {")":"(","}":"{","]":"["}
        for c in s:
            # Unconditionally add a right parenthesis.
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            # When adding a right parenthesis, check if the stack is not empty and whether the last value in the stack is the corresponding opening parenthesis.
            elif c == ')' or c == '}' or c == ']':
                if len(stack) > 0 and (stack[-1] == D.get(c)):
                    stack.pop()
                else:
                    return False
        # This is to ensure that a right parenthesis is added at the end, which would result in a non-empty stack.
        if len(stack) == 0:
            return True
        else:
            return False
        