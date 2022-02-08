class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        arr=[nums[0]]
        for i in range(1,len(nums)):
            arr.append(arr[i-1]+nums[i])
        print(arr)
        x=len(nums)
        for i in range(len(nums)):
            leftsum=arr[i]-nums[i]
            rightsum=arr[x-1]-arr[i]
            print(leftsum,rightsum)
            if leftsum==rightsum:
                return i
        return -1