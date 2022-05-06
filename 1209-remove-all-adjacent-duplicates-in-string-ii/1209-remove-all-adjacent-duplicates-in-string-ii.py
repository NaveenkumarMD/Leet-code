class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack=[]
        for ch in s:
            if stack and stack[-1][0]==ch:
                stack[-1][1]+=1
                if stack[-1][1]==k:
                    stack.pop()
            else:
                stack.append([ch,1])
        return "".join(s[0]*s[1] for s in stack)
        