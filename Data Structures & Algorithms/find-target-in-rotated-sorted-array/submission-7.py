class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = l + (r-l)//2
            
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        left1, left2 = 0, l
        right1, right2 = l-1, len(nums) - 1

        if target > nums[right2]:
            while left1 < right1:
                m = (left1+right1)//2
                
                if target > nums[m]:
                    left1 = m + 1
                else:
                    
                    right1 = m
                    
            if nums[right1] == target:
                return right1
            else:
                return -1
        else:
            while left2 < right2:
                m = (left2+right2)//2

                if target > nums[m]:
                    left2 = m +1
                else:
                    right2 = m
                
            if nums[right2] == target:
                return right2
            else:
                return -1
        