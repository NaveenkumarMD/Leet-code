import java.util.ArrayList;
import java.util.Arrays;

class Index{
    static int [] subarraysum(int [] arr,int s){
        int start=0;
        int end=0;
        int currsum=0;
        int n=arr.length;
        int [] res={0,0};
        for(int i=0;i<n;i++){
            while(currsum>s && start<i-1){
                currsum-=arr[start];
                start++;
            }
            if (currsum==s){
                res[0]=start;
                res[1]=i;
                return res;
            }
            if(currsum<s){
                currsum+=arr[i];
                end++;
            }
        }
        return res;
    }
    public static void main(String[] args){
        int arr[]={1, 4, 20, 3, 10, 5};
        int s=33;
        int [] res=subarraysum(arr,s);
        System.out.println(Arrays.toString(res));
    }
}
