"""
Runtime
102ms
Beats 7.41%of users with Python3

Memory
16.56MB
Beats 91.40%of users with Python3
"""

# Time Complexity：O(n^2)
# Space Complexity：O(1)
# Approach 1 : To determine whether it is an operator and decide whether to perform an operation or append it to the list.
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            # Cannot use 'isdigit' because it returns False for negative numbers.
            if c not in '+-*/': 
                stack.append(int(c))
            else:
                # Performing calculations using 'eval' with a time complexity of O(N)
                x = stack.pop() 
                stack.append(int(eval(str(stack.pop()) + c + str(x))))
        return stack[0]

"""
Runtime
70ms
Beats 75.39%of users with Python3

Memory
16.66MB
Beats 65.99%of users with Python3
"""

# Time Complexity：O(n)
# Space Complexity：O(1)
# Approach 2 : To determine whether it is an operator and decide whether to perform an operation or append it to the list.
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        answer = []
        for c in tokens:

            if c == "+":
                answer.append(int(answer.pop()) + int(answer.pop()))
            elif c == "-":
                num1 = int(answer.pop())
                num2 = int(answer.pop())
                answer.append(int(num2) - int(num1))
            elif c == "*":
                answer.append(int(answer.pop()) * int(answer.pop()))
            elif c == "/":
                num1 = int(answer.pop())
                num2 = int(answer.pop())
                answer.append(int(num2 / num1))
            else:
                answer.append(int(c))
                
        return answer[0]
