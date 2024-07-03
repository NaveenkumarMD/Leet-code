class Solution {
    public int strStr(String haystack, String needle) {
        char[] arr= haystack.toCharArray();
        char[] temp= needle.toCharArray();
        
        int i=0;
        int len= arr.length;
        
        int j=0;
        int tempLen=temp.length;
        
        int result=-1;
        while(i<len){
            char curr=arr[i];
            if(curr==temp[j]){
                j++;
            }
            else{
                i=i-j;
                j=0;
            }
                     
            if(j==tempLen){
                System.out.print(j);
                System.out.print(i);
                result=i-tempLen+1;
                break;
            }
            i++;

        }
        return result;
        
    }
}