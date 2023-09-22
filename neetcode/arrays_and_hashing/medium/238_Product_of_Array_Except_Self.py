"""
Runtime
250ms
Beats 7.47% of users with Python3

Memory
40.38MB
Beats 5.87% of users with Python3
"""
import numpy as np
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product,answer = [],[]
        all_product = 1
        for i in nums:
            all_product = all_product * i
        if all_product == 0:
            for index in range(len(nums)):
                if index == 0:
                    product.append(nums[1:len(nums)])
                elif index == len(nums):
                    product.append(nums[:len(nums)-1])
                else:
                    right = nums[index+1:len(nums)]
                    left = nums[:index]
                    right.extend(left)
                    product.append(right)

            for j in product:
                answer.append(np.prod(j))
        else:
            for k in nums:
                answer.append(all_product // k)
            
        return answer
"""
The Better Solution Comming Soon
"""