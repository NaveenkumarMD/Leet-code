class Solution:
    def calPoints(self, ops) -> int:
        stack=[]
        for i in ops:
            try:
                x=int(i)
                stack.append(int(i))
            except:                
                if i=='C':
                    stack.pop()
                elif i=='D':
                    stack.append(stack[-1]*2)
                elif i=='+':
                    x,y=stack[-1],stack[-2]
                    stack.append(x+y)
        return sum(stack)