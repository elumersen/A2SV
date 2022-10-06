class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            if char != ')':
                stack.append(char)
            else:
                word = ""
                while stack and stack[-1] != '(':
                    word += stack.pop()
                stack.pop()
                stack.extend(list(word))
        return ''.join(stack) 
