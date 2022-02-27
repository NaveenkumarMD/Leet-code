class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count=0
        for i in words:
            try:
                if i.index(pref)==0:
                    count+=1
            except:
                pass
        return count
        