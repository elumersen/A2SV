class Solution(object):
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        warmer_days = [0] * n
        stack = []
        for i, temp in enumerate(temperatures):
            while len(stack)!=0 and temp > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                warmer_days[stackIndex] = i - stackIndex
            stack.append([temp, i])
        return warmer_days
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
