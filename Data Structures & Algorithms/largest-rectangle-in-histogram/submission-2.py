class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        nsRight = [-1]*len(heights)
        nsLeft = [-1]*len(heights)
        highest = 0
        stack = [0]
        i = 1
        while i < len(heights):
            while len(stack) > 0 and heights[i] < heights[stack[-1]]:
                nsRight[stack.pop()] = i
            stack.append(i)
            i+=1
        stack = [len(heights)-1]
        i = len(heights) - 2

        while i >= 0:
            while len(stack) > 0 and heights[i] < heights[stack[-1]]:
                nsLeft[stack.pop()] = i
            stack.append(i)
            i-=1
        
        highest_area = 0
        for i in range(len(nsRight)):
            total = 0
            if nsRight[i] != -1:
                total += (nsRight[i] - i - 1) * heights[i]
            else:
                total += ((len(heights)-1) - i) * heights[i]
            
            if nsLeft[i] != -1:
                total += (i - nsLeft[i] - 1) * heights[i]
            else:
                total += i * heights[i]
            total += heights[i]
            
            highest_area = max(highest_area, total)
        return highest_area

            
        