class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        word=s
        sequence=t
        m=len(word)-1
        n=len(sequence)-1
        if m==n:
            return s==t
        if(m<=0):
            return True
        if(n<=0 and m!=0):
            return False

        def check(wordlen,seqlen):
            if wordlen==-1:
                return True
            if seqlen==-1:
                return False
            if (word[wordlen]!=sequence[seqlen]):
                return check(wordlen,seqlen-1)
            return check(wordlen-1,seqlen-1)        
        return check(m,n)
        