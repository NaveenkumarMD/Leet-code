public class Solution {
    public int removeElement(int[] nums, int val) {
    int i=0,k=0;
        
    while(i<nums.length){
        if(nums[i]!=val){
            nums[k++]=nums[i];
        }
        i++;
    }
    return k;
    }
}