class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        counter = 0
        stack = []
        for x in pushed:
            stack.append(x)
            # check if appended value is next to be popped out
            while stack and counter < len(popped) and stack[-1] == popped[counter]:
                stack.pop()
                counter = counter + 1
        return counter == len(popped)
