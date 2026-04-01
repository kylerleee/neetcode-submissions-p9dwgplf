class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        lm, rm = height[l], height[r]
        total = 0

        while l < r:
            if lm < rm:
                l+=1
                if (lm - height[l]) < 0:
                    total += 0
                else:
                    total += lm - height[l]
                lm = max(lm, height[l])
                
            else:
                r-=1
                rm = max(rm, height[r])
                total += rm - height[r]
                
        
        return total