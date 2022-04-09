class Solution:
    def longestCommonPrefix(self, strs) -> str:
        j=1        
        res=""
        if len(strs)==1:
            return strs[0]
        while j<=len(strs[0]):
            x=strs[0][:j]
            for i in range(1,len(strs)):
                try:
                    if strs[i].index(x)!=0:
                        return res
                    else:
                        continue
                except:
                    return res
            res=x
            j+=1
        return res if len(res)>0 else ""
            