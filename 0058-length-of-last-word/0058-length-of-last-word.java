
public class Solution {
    public int lengthOfLastWord(String s) {
        String[] arr= s.split(" ");
        int res=-1;
       for(String x: arr){
           System.out.println(x);
           if(x.length()>0){
               res=x.length();
           }
       }
        return res;
    }
}