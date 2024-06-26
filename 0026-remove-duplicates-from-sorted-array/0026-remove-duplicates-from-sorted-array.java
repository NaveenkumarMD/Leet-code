class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0) return 0;

        int i = 0;
        for (int k = 1; k < nums.length; k++) {
            if (nums[k] != nums[i]) {
                i++;
                nums[i] = nums[k];
            }
        }
        return i + 1;
    }
}