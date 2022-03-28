class Solution:
    def search(self, nums, target: int) -> bool:
        def binsearch(arr,k):
            low=0
            high=len(arr)-1
            while low<=high:
                mid=low+(high-low)//2
                if arr[mid]==k:
                    return True
                if arr[mid]<k:
                    low=mid+1
                else:
                    high=mid-1
            return False
        start=0
        for i in range(len(nums)-1):
            if nums[i+1]<nums[i]:
                start=i
                break
        s=start+1
        arr=nums
        return binsearch(arr[:s],target) or binsearch(arr[s:],target)
x=Solution()
y=x.search([1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1],2)
print(y)