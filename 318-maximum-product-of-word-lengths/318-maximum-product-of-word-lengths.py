class Solution:
    def getcommon(self,x,y):
        for i in x:
            if i in y:
                return False
        return True
    def maxProduct(self, words: List[str]) -> int:
        x=0
        for i in range(len(words)):
            for j in range(i,len(words)):
                if self.getcommon(words[i],words[j]):
                    x=max(len(words[i])*len(words[j]),x)
        return x
        