class Solution:
    def rotate(self, nums, k: int) -> None:
        def rev(nums,start,end):
            while start<end:
                nums[start],nums[end]=nums[end],nums[start]
                start+=1
                end-=1

        n=len(nums)-1
        k=k%(n+1)
        rev(nums,0,n)
        rev(nums, 0, k-1)
        rev(nums, k, n)
        print(nums)