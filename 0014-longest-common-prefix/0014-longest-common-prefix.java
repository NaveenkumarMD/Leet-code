public class Solution {
    public String longestCommonPrefix(String[] strs) {

        if(strs.length==1)return strs[0];
        String prefix="";
        int i=0;
        while(i<strs[0].length()){
            char curr = strs[0].charAt(i);
            for(int j=1;j<strs.length;j++){
                try{
                    if(strs[j].charAt(i)==curr){
                    
                    }
                    else{
                        return prefix;
                    }
                }
                catch (Exception e){
                    return prefix;
                }
                
            }
            i++;
            prefix+=curr;
        }
        return prefix;

    }
}