"""
Runtime O(N log N)
89ms
Beats 93.77% of users with Python3

Memory
19.59MB
Beats 83.48% of users with Python3
"""    

# Time Complexity：O(n)
# Space Complexity：O(n)
# Approach 1 ：Creating a dictionary to group words with the same combinations into the same key and then extracting the values to find a solution.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # print(strs) => ["eat","tea","tan","ate","nat","bat"]
        D = dict()
        result_list = []
        
        # group the anagrams
        for i in range(len(strs)):
            D.setdefault(''.join(sorted(strs[i])), []).append(strs[i])

        # {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat']}
        
        # append value to the result list
        for value in D.values():
            result_list.append(value)

        # [["eat","tea","ate"],["tan","nat"],["bat"]]
        return result_list