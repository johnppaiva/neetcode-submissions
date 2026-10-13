class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max_area = 0

        l = 0
        r = len(heights) - 1
        
        
        while l <= r:
            if heights[l] > heights[r]:
                height = min(heights[l],heights[r])
                width = abs(l - r)
                max_area = max(max_area,height * width)
                r -= 1
            else:
                height = min(heights[r],heights[l])
                width = abs(l - r)
                max_area = max(max_area,height * width)
                l += 1
           
           
        return max_area
            