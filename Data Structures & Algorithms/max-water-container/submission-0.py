class Solution:
    def maxArea(self, heights: List[int]) -> int:
        h = heights
        l, r = 0, len(h) - 1
        width = r - l
        height = h[l] if h[l] < h[r] else h[r]
        curr_area = width * height
        while l < r:
            if h[l] < h[r]:
                l += 1
            else:
                r -= 1
            width = r - l
            height = h[l] if h[l] < h[r] else h[r]
            curr_area = max(curr_area, width*height)
        return(curr_area)
        
        