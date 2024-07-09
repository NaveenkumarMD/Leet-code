import java.util.*;
public class Solution {
    public int  lengthOfLongestSubstring(String s) {
        HashMap<Character,Boolean> map=new HashMap();
        char[] arr= s.toCharArray();
        int start=0;
        int res=-1;
        for(int i=0;i<arr.length;i++){
            char curr=arr[i];
            while(map.containsKey(curr)){
                map.remove(arr[start]);
                start+=1;
            }
            map.put(curr,true);
            res=Math.max(i-start+1,res);
        }
        return res>0 ? res : 0;
    }
}