class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        store = []
        for p,s in zip(position,speed):
            store.append((p,s))
        store.sort()
       
        stack = []

        for p,s in store:
            time = (target - p) / s
            while stack and stack[-1] <= time:
                stack.pop()
            stack.append(time)
        
        return len(stack)



