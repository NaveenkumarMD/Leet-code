import java.util.*;
class Solution {
    public int romanToInt(String s) {
        HashMap<Character,Integer> map=new HashMap<Character,Integer>();
        map.put('I',1);
        map.put('V',5);
        map.put('X',10);
        map.put('L',50);
        map.put('C',100);
        map.put('D',500);
        map.put('M',1000);
        map.put('O',0);
        s=s+'O';
        int value=0;
        Stack<Integer> stack=new Stack<>();
        char[] arr=s.toCharArray();
        for(int i=0;i<arr.length-1;i++){
            int currValue=map.get(arr[i]);
            int nextValue=map.get(arr[i+1]);
            if(currValue<nextValue){
                value-=currValue;
            }
            else{
                value+=currValue;
            }
        }
        
        return value;
        
    }
}