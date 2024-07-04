class Solution {
    public boolean isPalindrome(String s) {
        String arr= cleanString(s);
        if(arr.length()<=1){
            return true;
        }
        int i=0;
        int j=arr.length()-1;
        
        while(i<j){
            if(arr.charAt(i) != arr.charAt(j)){
                return false;
            }
            i++;j--;
        }
        return true;
    }
    private String cleanString(String s){
        StringBuilder res= new StringBuilder();
        for(char c: s.toCharArray()){
            if(Character.isLetterOrDigit(c)){
                res.append(Character.toLowerCase(c));
            }
        }
        return res.toString();
    }
}