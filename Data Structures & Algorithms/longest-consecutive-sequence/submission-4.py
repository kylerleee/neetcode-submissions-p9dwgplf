class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        output = []
        count = 1
        if not nums:
            return 0
        else:
            for i in range(len(nums)):
                if i == len(nums) - 1:
                    output.append(count)
                    return sorted(output)[-1]
                if nums[i] == nums[i+1]:
                    continue
                elif nums[i] == nums[i+1] - 1:
                    count+=1
                else: 
                    output.append(count)
                    count = 1 

