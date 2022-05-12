class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        self.res = []
        
        def helper(nums, res, target):
            if (not target) and (len(res) == k):
                self.res.append(res)
                return
            
            if target < 0:
                return
            
            if len(res) >= k:
                return 
            
            for i in range(len(nums)):
                if nums[i] <= target:
                    helper(nums[i+1:], res+[nums[i]], target-nums[i])
        
        helper([i for i in range(1, 10)], [], n)
        
        return self.res