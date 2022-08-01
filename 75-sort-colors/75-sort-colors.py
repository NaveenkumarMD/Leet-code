class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low=0
        mid=0
        arr=nums
        high=len(nums)-1
        while mid<=high:
            if arr[mid]==0:
                arr[mid],arr[low]=arr[low],arr[mid]
                low+=1
                mid+=1
                continue
            if arr[mid]==1:
                mid+=1
                continue
            if arr[mid]==2:
                arr[mid],arr[high]=arr[high],arr[mid]
                high-=1
                continue
        print(arr)
    
        