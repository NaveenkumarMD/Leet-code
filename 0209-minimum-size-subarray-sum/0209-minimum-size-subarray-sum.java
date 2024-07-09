class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int res=Integer.MAX_VALUE;
        int right=0;
        int left=0;
        int sum=0;
        while(right<nums.length){
            int curr=nums[right];
            sum+=curr;
            while(sum>=target){
                sum-=nums[left];
                res=Math.min(res,right-left+1);
                left++;
                
                
            }
            right++;
        }
        return res==Integer.MAX_VALUE?0:res;
        
    }
}