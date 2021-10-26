class Solution:
    def minTimeToType(self, word: str) -> int:
        ans=len(word)
        prev='a'
        for i in word:
            x=(ord(i)-ord(prev))%26
            prev=i
            ans+=min(x,26-x)
        print(ans)

x=Solution()
y=x.minTimeToType(word="abc")
print(y)