class Index{
    static int findMissing(int[] arr){
        int res;
        int n=arr.length;
        int sumfromformula=((n+1)*(n+2)) / 2;
        int sum=0;
        for (int i : arr) {
            sum+=i;
        }
        return sumfromformula-sum;
    }
    public static void main(String [] args){
        int[] arr = {1, 2, 3, 5, 6, 7, 8, 9, 10};
        System.out.println(findMissing(arr));
    }
}