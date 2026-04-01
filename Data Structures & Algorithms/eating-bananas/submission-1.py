import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        total = 0
        while low <= high:
            mid = (high + low) // 2
            for i in piles:
                total += math.ceil(i/mid)
            if total <= h:
                high = mid - 1
                total = 0
            elif total > h:
                low = mid + 1
                total = 0
        return low