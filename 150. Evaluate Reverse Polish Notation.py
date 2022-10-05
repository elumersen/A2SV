class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operator = ["+","-","*","/"]
        for i in tokens:
            if i not in operator:
                stack.append(i)
            if i in operator:
                value1=int(stack.pop())
                value2=int(stack.pop())
                if i=="+":
                    result=value2+value1
                if i=="-":
                    result=value2-value1
                if i=="*":
                    result=value2*value1
                if i=="/":
                    result=int(value2/value1)
                stack.append(result)
        return stack[0]
