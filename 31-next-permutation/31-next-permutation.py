class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        latest_peak = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                latest_peak = i
                
        if latest_peak == 0:
            nums.reverse()
            return
        
        pre_peak = latest_peak - 1
        min_after_peak = latest_peak
        for i in range(latest_peak, len(nums)):
            if nums[i] > nums[pre_peak] and nums[i] < nums[min_after_peak]:
                min_after_peak = i
          
        temp = nums[pre_peak]
        nums[pre_peak] = nums[min_after_peak]
        nums[min_after_peak] = temp
        
        nums[latest_peak:] = sorted(nums[latest_peak:])