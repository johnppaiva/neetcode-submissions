class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] in store.keys():
                return [store[nums[i]],i]
            store[diff] = i


