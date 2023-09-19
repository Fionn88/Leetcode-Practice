"""
Runtime
97ms
Beats 71.85%of users with Python3

Memory
20.94MB
Beats 84.53%of users with Python3
"""

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        new_dict = {k: v for k, v in sorted(Counter(nums).items(), key=lambda item: item[1],reverse=True)}
        for index in range(k):
            result.append(list(new_dict)[index])
        return result
