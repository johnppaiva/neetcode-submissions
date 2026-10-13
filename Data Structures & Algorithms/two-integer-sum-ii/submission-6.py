class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l = 0

        r = len(numbers) - 1

        while l <= r:
            m = l + (r - l) // 2

            if target < numbers[m]:
                r = m - 1
            elif target > numbers[m]:
                l = m + 1
            else:
                return [l - 1,r - 1]