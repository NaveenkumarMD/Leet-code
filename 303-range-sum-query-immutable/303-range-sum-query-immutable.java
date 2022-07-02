class NumArray {
    int ar[];

    public NumArray(int[] nums) {
        int len = nums.length;
        ar = new int[len];
        ar[0] = nums[0];
        for (int i = 1; i < len; i++) {
            ar[i] = ar[i - 1] + nums[i];
        }
    }

    public int sumRange(int left, int right) {
        if (left == 0)
            return ar[right];
        else
            return (ar[right] - ar[left - 1]);
    }
}