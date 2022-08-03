class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre={i:[] for i in  range(numCourses)}
        for cors,prereq in prerequisites:
            pre[cors].append(prereq)
        s=set()
        def dfs(cr):
            if cr in s:
                return False
            if pre[cr]==[]:
                return True
            s.add(cr)
            for i in pre[cr]:
                if not dfs(i):return False
            s.remove(cr)
            pre[cr]=[]
            return True
        for i in range(numCourses):
             if not dfs(i):return False
        return True
            
                