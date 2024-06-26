import java.util.*;
public class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer,Integer> h=new HashMap<Integer,Integer>();
        for(int i:nums){
            if(h.get(i)!=null){
                h.put(i,h.get(i)+1);
            }
            else{
                h.put(i,1);
            }
        }
        System.out.println(h);
        int i=-1;
        int key=0;
        for(Map.Entry<Integer,Integer> m : h.entrySet()){
            if(m.getValue()>i){
                i=m.getValue();
                key=m.getKey();
                
            }
        }
    return key;
    }
}