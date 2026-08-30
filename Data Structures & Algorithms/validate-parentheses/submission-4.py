class Solution:
    def isValid(self, s: str) -> bool:
        right = ["(","{","["]
        stack = []
        for char in s:
            if char in right:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                if char == "}":
                    if stack.pop() != "{":
                        return False
                elif char == ")":
                    if stack.pop() != "(":
                        return False
                elif char == "]":
                    if stack.pop() != "[":
                        return False
        if len(stack) != 0:
            return False
        return True