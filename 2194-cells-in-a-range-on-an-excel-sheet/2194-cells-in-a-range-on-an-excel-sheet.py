class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        arr=[]
        for i in range(ord(s[0]),ord(s[3])+1):
            res=""
            for j in range(int(s[1]),int(s[4])+1):
                res+=chr(i)+str(j)
                arr.append(res)
                res=""
        return arr
        