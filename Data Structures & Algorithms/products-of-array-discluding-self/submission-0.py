class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, post = 1,1
        o = []
        n = 0
        while n < len(nums):
            o.append(pre)
            pre *= nums[n]
            n += 1
        n -= 1
        while n >= 0:
            o[n] *= post
            post *= nums[n]
            n -= 1
        return o
            
                  
