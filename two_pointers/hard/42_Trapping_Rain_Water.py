"""
Runtime
7784ms
Beats 5.00%of users with Python3

Memory
18.68MB
Beats 26.24%of users with Python3
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0]
        maxRight = [0]
        res = []
        for i in range(1,len(height)):
            maxLeft.append(max(max(maxLeft),height[i-1]))
        for i in range(len(height)-1,0,-1):
            maxRight.insert(0,max(max(maxRight),height[i]))
        
        for i in range(len(height)):
            container = min(maxLeft[i],maxRight[i]) - height[i]
            if container < 0:
                res.append(0)
            else:
                res.append(container)
        return sum(res)

"""
Runtime
119ms
Beats 43.86%of users with Python3

Memory
18.06MB
Beats 95.45%of users with Python3
"""
class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0
        l = 0
        r = len(height) - 1
        maxLeft = height[l]
        maxRight = height[r]

        res = 0
        while l < r:
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(maxLeft,height[l])
                res += maxLeft - height[l]
            else:
                r -= 1
                maxRight = max(maxRight,height[r])
                res += maxRight - height[r]

        return res