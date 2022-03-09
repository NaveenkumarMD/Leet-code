class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def getvalue(s):
            dit={}
            j=0
            for i in range(97,107):
                dit[chr(i)]=str(j)
                j+=1
            h=""
            for i in s:
               h+=dit[i]
            print(h)
            return int(h)
        if getvalue(firstWord)+getvalue(secondWord)==getvalue(targetWord):
            return True
        return False