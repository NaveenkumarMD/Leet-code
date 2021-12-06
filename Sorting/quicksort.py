def partition(arr,start,end):
    pivot_index=start
    pivot=arr[start]

    while start<end:

        while start<len(arr) and arr[start]<=arr[pivot_index]:
            start+=1
            
        while arr[pivot_index]<arr[end]:
            end-=1

        if start<end:
            arr[end],arr[start]=arr[start],arr[end]
    arr[pivot_index],arr[end]=arr[end],arr[pivot_index]
    return end 
def quicksort(arr,start,end):
    if start< end:
        j=partition(arr, start, end)
        quicksort(arr, start, j-1)
        quicksort(arr, j+1, end)
if __name__=="__main__":
    arr=[4,5,6,4,3,9,2,-1]
    quicksort(arr, 0, len(arr)-1)
    print(arr)