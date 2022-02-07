
class Solution:
    def longestPalindrome(self, s):
        dit={}
        for i in s:
            if i in dit:
                dit[i]+=1
            else:
                dit[i]=1
        ans=0
        for i in dit.values():
            ans+=i// 2 *2
            if ans %2 ==0 and i%2==1:
                ans+=1
        return ans
            
        
        