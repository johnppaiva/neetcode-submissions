class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        store = {}

        for num in nums:
            store[num] = 1 + store.get(num,0)
        
        arr = []
        for i in range(len(nums) + 1):
            arr.append([])
    
        for key ,val in store.items():
            arr[val].append(key)
        res = []

        for i in range(len(arr) - 1, 0, -1):
            for num in arr[i]:
                res.append(num)
                if len(res) == k:
                    return res