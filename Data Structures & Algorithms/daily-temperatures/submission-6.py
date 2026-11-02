class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]: # see a warmer temp
                stackT = stack.pop()
                stackInd = stackT[-1]
                stackT = stackT[0]
                output[stackInd] = i - stackInd

            stack.append((temperatures[i],i))

        return output