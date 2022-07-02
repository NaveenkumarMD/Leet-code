
class Index {
    static double kadane(int arr[]){
        double max_so_far=Double.NEGATIVE_INFINITY;
        int max_ending_here=0;
        for (int i : arr) {
            max_ending_here+=i;
            if (max_ending_here>max_so_far){
                max_so_far=max_ending_here;
            }
            if(max_ending_here<0){
                max_ending_here=0;
            }

        }
        return max_so_far;
    }
    public static void main(String args[]){
        int[] arr = {-2, -3, 4, -1, -2, 1, 5, -3};
        System.out.println((int)kadane(arr));
    }
}
