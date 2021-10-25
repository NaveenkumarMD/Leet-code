class Solution:
    def nextGreaterElements(self,nums):
        arr=nums*2
        n=len(nums)
        ans=[-1 for _ in range(n)]
        stack=[]
        for index,value in enumerate(arr):
            while stack and arr[stack[-1]]<value:
                c=stack.pop()
                ans[c%n]=value
            stack.append(index)
        return ans
x=Solution()
y=x.nextGreaterElements([1,2,1])
print(y)