class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        arr = []
        res = []

        for i in range(len(nums)):
            heapq.heappush(arr, (-nums[i],i))

            if i >= k - 1:
                while arr[0][1] <= i - k:
                    heapq.heappop(arr)
                res.append(-arr[0][0])
        
        return(res)