class Solution:
    def search(self, nums: List[int], target: int) -> bool:
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