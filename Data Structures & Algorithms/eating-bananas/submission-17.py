class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max(piles)

        res = r
        while l < r:

            k = (l + r) // 2
            hours = 0
            print(l,r,k)
            for p in piles:
                hours += math.ceil(p / k)
            print(hours)
            if hours <= h: # valid eating rate
                res = min(res,k)
                r = k - 1
            else:
                l = k + 1

        return res