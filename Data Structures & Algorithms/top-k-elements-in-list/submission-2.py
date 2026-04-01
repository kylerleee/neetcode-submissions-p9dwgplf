class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        idk = {}
        nums = sorted(nums)
        freq = [[] for i in range(len(nums) + 1)]
        ans = []
        for num in nums:
            if num in idk:
                idk[num] += 1
            else:
                idk[num] = 1
        for key, value in idk.items():
            freq[value].append(key)
        for val in range(len(freq) -1, -1, -1):
            if freq[val] != []:
                ans += freq[val]
            if len(ans) == k:
                return ans

        
        

