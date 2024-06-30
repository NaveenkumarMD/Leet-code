public class Solution {
    public String reverseWords(String s) {

        int i=0;
        int j=0;
        s=s.trim();
        char[] arr =s.toCharArray();

        reverse(arr,0,s.length()-1);

        while(j<arr.length){
            if(!Character.toString(arr[j]).equals(" ") || (j + 1 < arr.length && !Character.toString(arr[j + 1]).equals(" "))){
                arr[i]=arr[j];
                i++;
            }
            j++;
        }

        int len=i;

        int start=0;
        for(int k=0;k<len;k++){

            if(Character.toString(arr[k]).equals(" ")  ){

                reverse(arr,start,k-1);
                start=k+1;
            }
            if(k==len-1){
                reverse(arr,start,k);
            }
        }
        String res=String.valueOf(arr);

        return res.substring(0,i);
    }
    private void reverse(char[] arr,int start,int end){
        while(start<end){
            char temp=arr[start];
            arr[start++]=arr[end];
            arr[end--]=temp;
        }
    }
}