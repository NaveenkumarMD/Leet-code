class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def getvalue(s):
            h=""
            for i in s:
               h+=str(ord(i)-97)
            print(h)
            return int(h)
        if getvalue(firstWord)+getvalue(secondWord)==getvalue(targetWord):
            return True
        return False