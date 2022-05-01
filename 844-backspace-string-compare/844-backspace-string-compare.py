class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def check(s):
            stack=[]
            for i in s:
                if stack and i=="#":
                    stack.pop()
                elif i.isalpha():
                    stack.append(i)
            return stack
        return check(s)==check(t)