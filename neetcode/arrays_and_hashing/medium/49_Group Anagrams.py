"""
Runtime
93ms
Beats 85.39%of users with Python3

Memory
20 MB
Beats 61.07%of users with Python3
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # print(strs) => ["eat","tea","tan","ate","nat","bat"]
        D = dict()
        # group the anagrams
        for i in range(len(strs)):
            D.setdefault(''.join(sorted(strs[i])), []).append(strs[i])

        # {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat']}

        # Sort the value of the dictionary
        for key,value in D.items():
            D[key] = sorted(value)

        # {'aet': ['ate', 'eat', 'tea'], 'ant': ['nat', 'tan'], 'abt': ['bat']}
        
        # Sort by length of the value
        sorted_items = sorted(D.items(), key=lambda x: len(x[1]))

        # [('abt', ['bat']), ('ant', ['nat', 'tan']), ('aet', ['ate', 'eat', 'tea'])]

        # Get the value of the sorted_items
        output = [item[1] for item in sorted_items]
        
        # [['bat'], ['nat', 'tan'], ['ate', 'eat', 'tea']]
        return output