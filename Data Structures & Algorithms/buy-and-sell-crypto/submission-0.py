class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        price = -1
        profit = 0
        for i in prices[::-1]:
            if i > price:
                price = i
            elif (price - i) > profit:
                profit = price - i
        
        return profit
                