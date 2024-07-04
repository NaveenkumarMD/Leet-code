class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int i=0;
        int k=numbers.length-1;
        
        while(i<k){
            int sum=numbers[i]+numbers[k];
            if(sum>target){
                k--;
            }
            else if (sum<target){
                i++;
            }
            else{
                int[] res=new int[2];
                res[0]=i+1;
                res[1]=k+1;
                return res;
            }
        }
        return new int[2];
    }
}