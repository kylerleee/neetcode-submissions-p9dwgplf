class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        sum = 0
        n = str(n)
        while True:
            for num in n:
                sum += int(num) ** 2
            if sum == 1:
                return True
            n = str(sum)
            if sum in seen:
                return False
            seen.add(sum)
            sum = 0
            
        