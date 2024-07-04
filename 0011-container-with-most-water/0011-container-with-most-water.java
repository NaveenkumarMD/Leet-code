class Solution {
    public int maxArea(int[] height) {
        int i=0;
        int j=height.length-1;
        int m =-1;
        while(i<j){
            int curr=calculate(height[i],height[j],i,j);
            System.out.println(curr);
            m=Math.max(curr,m);
            if(height[i]<height[j]){
                i++;
            }
            else{
                j--;
            }
        }
        return m;
        
    }
    private int calculate(int x,int y,int i,int j){
        return (j-i)*Math.min(x,y);
    }
}