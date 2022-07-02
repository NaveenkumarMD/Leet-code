import java.util.Arrays;

class Index {
    static int[] rearrange(int arr[]) {
        int start = 0;
        int end = arr.length - 1;
        int temp[] = new int[end + 1];
        int i = 0;
        while (start <= end) {
            if (i % 2 == 0) {
                temp[i] = arr[end];
                end -= 1;
            } else {
                temp[i] = arr[start];
                start += 1;
            }
            i++;
        }
        return temp;
    }

    public static void main(String args[]) {
        int arr[] = { 1, 2, 3, 4, 5, 6, 7 };
        System.out.print(Arrays.toString(rearrange(arr)));
    }

}
