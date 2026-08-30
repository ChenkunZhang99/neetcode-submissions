class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        Output = [0] * len(temperatures)
        for i in range (len(temperatures)):
            while stack:
                if temperatures[stack[-1]] >= temperatures[i]:
                    stack.append(i)
                    break
                else:
                    Output[stack[-1]] = i - stack[-1]
                    stack.pop()
            if not stack:
                stack.append(i)
                continue
        return Output