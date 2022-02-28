class Solution:
    def longestWord(self, words) -> str:
        words.sort(key=len,reverse=True)
        print(words)
        arr=set(words)
        s=[]
        for i in words:
            if s and len(i)<len(s[-1]):
                break                
            for j in range(1,len(i)):
                if i[:j] in arr:
                    if j== len(i)-1:
                        s.append(i)
                    continue
                else:
                    break
        print(s)
        if len(s)==1:
            return s[0]
        elif len(s)==0:
            x=sorted(words)[0]
            return x if len(x)==1 else ""
        else:
            
            s=sorted(s)
            return s[0]
            
                
            
                    
            