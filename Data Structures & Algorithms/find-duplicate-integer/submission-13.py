class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        s, f = 0,0
        while True:
            s = nums[s]
            f = nums[nums[f]]
            if s == f:
                break
        
        start = 0
        while start != s:
            start = nums[start]
            s = nums[s]
        return s