"""
Runtime
44ms
Beats 84.21%of users with Python3

Memory
17.72MB
Beats 32.23%of users with Python3
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = re.sub('[^A-Za-z0-9]+', '', s).lower()
        return new_string == new_string[::-1]