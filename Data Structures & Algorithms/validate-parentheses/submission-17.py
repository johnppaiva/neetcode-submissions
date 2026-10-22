class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        closeToOpen = {"}" : "{", "]" : "[", ")" : "("}

        for p in s:
            if stack and p in closeToOpen:
                if stack[-1] == closeToOpen[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        return len(stack) == 0