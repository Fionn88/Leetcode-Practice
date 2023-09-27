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

"""
Runtime
39ms
Beats 95.39%of users with Python3

Memory
17.5MB
Beats 35.32%of users with Python3
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ''.join(e for e in s if e.isalnum()).lower()
        return new_string == new_string[::-1]

"""
Runtime
51ms
Beats 53.06%of users with Python3

Memory
17.75MB
Beats 32.10%of users with Python3
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ''.join(e for e in s if e.isalnum()).lower()
        r = 0
        l = len(new_string) -1
        while r < l:
            if new_string[r] != new_string[l]:
                return False
            r += 1
            l -= 1
        return True