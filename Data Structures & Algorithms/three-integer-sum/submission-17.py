class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            
            l,r = i+1, len(nums) - 1
            complement = 0 - a
            while l < r:
                if nums[l] + nums[r] > complement:
                    r-=1
                elif nums[l] + nums[r] < complement:
                    l+=1
                else:
                    output.append([a, nums[l], nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
        return output
                
        

            