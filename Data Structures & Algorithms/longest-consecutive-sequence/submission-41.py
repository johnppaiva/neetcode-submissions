class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        numSet = set(nums)
        max_length = 0
        for i in range(len(nums)):
            if nums[i] - 1 in numSet:
                continue
            length = 1
            while nums[i] + length in numSet:
                length += 1

            max_length = max(max_length, length)
        return max_length