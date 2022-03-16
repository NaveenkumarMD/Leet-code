class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack=[]
        i=0
        for el in pushed:
            stack.append(el)
            while stack and stack[-1]==popped[i]:
                stack.pop()
                i+=1
        return len(pushed)==i
                
        