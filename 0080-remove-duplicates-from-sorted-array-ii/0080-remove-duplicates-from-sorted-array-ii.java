class Solution {
    public int removeDuplicates(int[] nums) {
        if(nums.length<1)return nums.length;
        int i=1;
        for(int k=2;k<nums.length;k++){
            if(nums[k]!=nums[i-1]){
                nums[++i]=nums[k];
            }
        }
        return i+1;
    }
}