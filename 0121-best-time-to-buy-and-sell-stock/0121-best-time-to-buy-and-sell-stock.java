
class Solution {
    public int maxProfit(int[] prices) {
        int small=prices[0];
        int max=0;
        int i=1;
        while(i<prices.length){
            if(prices[i]<small){
                small=prices[i];
            }
            else{
                max=Math.max(max,prices[i]-small);
            }
            i++;
        }
        return max;
    }
}