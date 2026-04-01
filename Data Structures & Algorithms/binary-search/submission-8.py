class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l,r = 0, len(nums) - 1
        if len(nums) == 1 and target == nums[0]:
            return 0
        while l != r:
            middle = (r+l) // 2
            if nums[middle] < target:
                l = middle + 1
                if nums[l] == target:
                    return l
            elif nums[middle] > target:
                r = middle
            else:
                return middle
        
        return -1
        