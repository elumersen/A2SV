class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        warmer_days = [0] * len(temperatures)
        stack=[]
        for i , temp in enumerate(temperatures):
            while len(stack)!=0 and temp > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                warmer_days[stackIndex] = i-stackIndex
            stack.append([temp, i])
        return warmer_days
