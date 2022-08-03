class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        x=jug1Capacity
        y=jug2Capacity
        target=targetCapacity
        z=x+y
        q=[0]
        visited=set()
        if target>z:
            return False
        def check(s):
            if s>=0 and s<=z:
                return True
            return False
        while q:
            curr=q.pop(0)
            nexts=[]
            if curr==target:
                return True
            if check(curr+x) and curr+x not in visited:
                nexts.append(curr+x)
                visited.add(curr+x)
            if check(curr-x) and curr-x not  in visited:
                nexts.append(curr-x)
                visited.add(curr-x)
            if check(curr+y) and curr+y not in visited:
                nexts.append(curr+y)
                visited.add(curr+y)
            if check(curr-y) and curr-y not  in visited:
                nexts.append(curr-y)
                visited.add(curr-y)
            for i in nexts:
                q.append(i)
                
        return False
                
                
            
        
        
        