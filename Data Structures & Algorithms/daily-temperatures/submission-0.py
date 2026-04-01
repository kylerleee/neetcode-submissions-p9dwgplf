class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        
        for i, temp in enumerate(temperatures):
            stack.append([temp, i])
            if len(stack) == 1:
                continue
            else:
                while len(stack) > 1 and stack[-1][0] > stack[-2][0]:
                    print(stack)
                    result[stack[-2][1]] = stack[-1][1] - stack[-2][1]
                    stack.pop(-2)
                    
                
        return (result)