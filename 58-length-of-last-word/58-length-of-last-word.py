class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr=[]
        s+='0'
        temp=""
        for i in s:
            if i.isalpha():
                temp+=i
            else:
                if temp:
                    arr.append(temp)
                    temp=""
        return len(arr[-1])
        