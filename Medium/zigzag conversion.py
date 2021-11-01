class Solution:
    def convert(self, s: str, numRows: int) -> str:
        arr=["" for _ in range(numRows)]
        curr=0
        flag=False
        for i in s:
            arr[curr]+=i
            if curr==0 or curr==numRows-1:
                flag=not flag
            curr+=1 if flag else -1
        return "".join(arr)

x=Solution()
y=x.convert("PAYPALISHIRING",3)
print(y)