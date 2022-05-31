class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        need=1<<k
        got=set()
        for i in range(0,len(s)-k+1):
            temp=s[i:i+k]
            print(temp)
            if temp not in got:
                got.add(temp)
                need-=1
                if need==0:
                    return True
        return False
                