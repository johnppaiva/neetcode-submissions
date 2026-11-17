class Solution:
    def trap(self, height: List[int]) -> int:
        
        l = 0
        r = len(height) - 1

   
        total = 0
        h = 0
        leftmax = height[l]
        rightmax = height[r]
        while l <= r:

            if leftmax < rightmax:

                h = max(height[l],leftmax)

                total += h - height[l]

                leftmax = max(leftmax,h)
                l += 1
            else:
                h = max(height[r],rightmax)

                total += h - height[r]
                
                rightmax = max(rightmax,h)

                r -= 1


        return total