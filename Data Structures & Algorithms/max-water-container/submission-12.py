class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max_area = 0

        l = 0
        r = len(heights) - 1
       
        while l <= r:
            height = min(heights[r],heights[l])
            width = abs(l - r)
            max_area = max(max_area,height * width)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return max_area
            