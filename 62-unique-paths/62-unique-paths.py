class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.dit={}
        def util(m,n):
            key=str(m)+","+str(n)
            if key in self.dit:
                return self.dit[key]
            if m==0 or n==0:
                return 0
            if m==1 and n==1:
                return 1
            self.dit[key]=util(m-1,n)+util(m,n-1)
            return self.dit[key]
        return util(m,n)