class Solution {
    public void rotate(int[] nums, int k) {
         k = k % nums.length;

    if (k == 0) return;
                int[] arr=nums.clone();
        for(int i=0;i<k;i++){
            nums[i]=arr[nums.length-k+i];
        }
        for(int j=k;j<nums.length;j++){
            nums[j]=arr[j-k];
        }
    }
}