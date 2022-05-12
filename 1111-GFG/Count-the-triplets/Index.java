import java.util.Arrays;

class Index {
    static boolean binarysearch(int arr[],int sum) {
        int start=0;
        int end=arr.length-1;
        while (start <= end) {
            int mid = (start + end) / 2;
            if (arr[mid] == sum) {
                return true;
            } else if (arr[mid] > sum) {
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }
        return false;
    }

    static int[] sort(int arr[]) {
        int n = arr.length;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (arr[i] > arr[j]) {
                    int temp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp;
                }
            }
        }
        return arr;
    }

    int findtriplet(int arr[]) {
        int n = arr.length;
        int count = 0;
        arr = sort(arr);
        System.out.println(Arrays.toString(arr));
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                if (binarysearch(arr, arr[i] + arr[j])) {
                    count++;
                }
            }
        }
        return count;
    }

    public static void main(String[] args) {
        int arr[] = { 1, 4, 2, 3 };

        Index obj = new Index();
        int res=obj.findtriplet(arr);

    
        System.out.println(res);
    }
}
