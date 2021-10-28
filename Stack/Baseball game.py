class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack=[]
        for i in ops:
            try :
                x=int(i)
                stack.append(x)
            except:
                if i=="C":
                    stack.pop()
                if i=="D":
                    stack.append(stack[-1]*2)
                if i=="+":
                    stack.append(stack[-1]+stack[-2])
                
        return sum(stack)