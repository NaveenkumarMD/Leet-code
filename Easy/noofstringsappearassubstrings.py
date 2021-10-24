class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        x=0
        for i in patterns:
            if i in word:
                x+=1
        return x
        