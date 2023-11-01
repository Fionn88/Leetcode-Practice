"""
Runtime
669ms
Beats 62.30%of users with Python3

Memory
73.94MB
Beats 60.98%of users with Python3
"""

# Time complexity: O(log n)
# Space Complexity：O(1)
# Approach 1 ：Search for a value within the dictionary using Binary Search, looking for the value that is less than but closest to the given timestamp.
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value,timestamp))


    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key,[])
        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l + r) // 2
            # If the value is less than or equal to the timestamp, then search the right half and update the 'res' value.
            if values[mid][1] <= timestamp:
                l = mid + 1
                res = values[mid][0]
            else:
                r = mid - 1
        return res
        
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
