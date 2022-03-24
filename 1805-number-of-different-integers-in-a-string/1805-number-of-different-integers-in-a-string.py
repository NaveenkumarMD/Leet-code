class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        s=set()
        word+='.'
        temp=""
        for i in word:
            if i.isdigit():
                temp+=i
            else:
                if temp:
                    s.add(int(temp))
                    temp=""
        return len(s)
            
                
                
        