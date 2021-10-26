class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        i=0
        n=len(s)
        s=list(s)
        goal=list(goal)
        while i<n:
            s.append(s.pop(0))
            if s==goal:
                return True
            i+=1
        return False
        