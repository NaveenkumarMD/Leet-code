import java.util.*;
class Solution {
    public int hIndex(int[] citations) {
        Arrays.sort(citations);
        int l=citations.length;

        for(int i=0;i<l;i++){
            int curr=citations[i];
            if(l-i<=curr){
                return l-i;
            }
        }
        return 0;
    }
}