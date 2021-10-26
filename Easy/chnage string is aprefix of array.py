class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        
        a = ''
    
        for i in words:
            
            a += i
            
            if a == s:
                return True
            if not s.startswith(a):
                break
                     
        return False
x=Solution()
y=x.isPrefixString("iloveleetcode",["apples","i","love","leetcode"])
print(y)