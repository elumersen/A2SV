class Solution:
    def isValid(self, s: str) -> bool:
        stack1 =[]
        stack2=[]
        stack3=[]
        pairBrackets = {'(': ')', '[':']', '{':'}'}
        for i in s:
            if i =='(' or i=='[' or i=='{':
                stack1.append(i)
            if i ==')' or i==']' or i=='}':
                stack2.append(i)
        if len(stack1)!= len(stack2):
            return False
        for i in s:
            if i in stack1:
                stack3.append(i)
            if i in stack2:
                if stack3 and pairBrackets[stack3[-1]]==i:
                    stack3.pop()
        if len(stack3) !=0:
            return False
        else:
            return True
