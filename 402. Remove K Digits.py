class Solution(object):
    def removeKdigits(self, num, k):
        stack=[]  
        for i in num:
            while k > 0 and stack and stack[-1] > i:
                k -= 1
                stack.pop()
            stack.append(i)
        stack = stack[: len(stack) - k]
        result = "".join(stack)
        if result:
            return str(int(result))
        else:
            return "0"
        
        """
        :type num: str
        :type k: int
        :rtype: str
        """
