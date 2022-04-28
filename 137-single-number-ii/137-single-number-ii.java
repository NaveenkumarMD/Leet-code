class Solution {
    public int singleNumber(int[] arr) {
        int[] count=new int[32];
        for(int i:arr){
          int j=0;
          while(i!=0 && j<32){
             if((i&1)==1) count[j]++; //Storing the occurence of set bits of all the array elements
                 i>>=1;
                 j++;
              }
          }
          int ans=0;
          for(int i=0;i<32;i++){
              if(count[i]%3!=0)//Elements occuring 3 times makes the set bit occurence also a multiple of 3 
                  ans|=(1<<i);
         }
         return ans;
    }
}