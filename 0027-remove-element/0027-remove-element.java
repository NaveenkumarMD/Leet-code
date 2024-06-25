public class Solution {
    public int removeElement(int[] nums, int val) {
        int i=nums.length-1;
        int k=0;
        while(i>=0){
            int curr=nums[i];
            int j=i+1;
            if(curr==val) {
                while (j < nums.length && nums[j] != val) {
                    nums[j-1]=nums[j];
                    j++;
                }
                nums[j-1]=curr;
                k++;
            }
            i--;

        }
        return nums.length-k;
    }

}