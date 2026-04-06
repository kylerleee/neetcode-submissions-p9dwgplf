class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        l, r = 1,0
        max_area = 0
        for i in range(len(heights)):
            area = heights[i]
            r = i+1
            l = i-1
            while l >= 0 and heights[l] >= heights[i]:
                area += heights[i]
                l -= 1
            while r < len(heights) and heights[r] >= heights[i]:
                area += heights[i]
                r += 1
            max_area = max(max_area, area)

        return(max_area)