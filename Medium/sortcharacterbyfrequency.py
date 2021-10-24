from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        dit=dict(Counter(s))
        dits=sorted(dit,reverse=True,key=lambda x:dit[x])
        s=""
        for i in dits:
            s+=i*dit[i]
        print(s)
c=Solution()
c.frequencySort('tree')
