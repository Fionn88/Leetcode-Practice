"""
Runtime
48ms
Beats 7.05%of users with Python3

Memory
16.26MB
Beats 72.06%of users with Python3
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  
        D = {")":"(","}":"{","]":"["}
        for c in s:
            if c == '(' or c == '{' or c == '[':  
                stack.append(c)  
            elif c == ')' or c == '}' or c == ']':  
                if len(stack) > 0 and (stack[-1] == D.get(c)): 
                    stack.pop() 
                else:
                    return False
        if len(stack) == 0: 
            return True
        else:
            return False