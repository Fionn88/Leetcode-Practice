"""
427 ms
Time Cost

5.09 MB
Memory Cost

94.80%
Beats
"""

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        ans = []
        for index,value in enumerate(strs):
            if index == len(strs) - 1:
                ans.append(value)
            else:
                ans.append(value)
                ans.append(":;")
        return ''.join(ans)

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        return str.split(":;")
            