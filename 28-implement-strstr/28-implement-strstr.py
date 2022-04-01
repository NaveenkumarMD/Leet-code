class Solution(object):
    def strStr(self, haystack, needle):
        m=len(needle)
        if(haystack==needle):
            return 0
        for i in range(len(haystack)-len(needle)+1):
            print(haystack[i])
            j=0
            if(len(needle)==0):
                return 0
            while j<m:
                if(haystack[i+j]!=needle[j]):
                    break
                j+=1
            if(j==m):
                return i
        return -1