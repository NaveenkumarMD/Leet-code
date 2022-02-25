from collections import Counter
class Solution:
    def findErrorNums(self, nums):
        repated=max([i for i in nums if nums.count(i)>1])
        print(repated)
        arr=[i for i in range(1,len(nums)+1)]
        print(arr)
        print(nums)
        for i in nums:
            print(i)
            if i in arr:
                arr.remove(i)
        return [repated,*arr]


x=Solution()
y=x.findErrorNums([3,2,2])
print(y)