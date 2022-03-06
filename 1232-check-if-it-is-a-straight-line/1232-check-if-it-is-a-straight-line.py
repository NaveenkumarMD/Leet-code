class Solution:
    def slope(self,p1,p2):
        a=p2[0]-p1[0]
        if a ==0:return float('inf')
        b=p2[1]-p1[1]
        return b/a
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        arr=[]
        f=coordinates
        m=self.slope(f[0],f[1])
        return all([m==self.slope(f[0],p) for p in f[2:]])
        
        