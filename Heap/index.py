def heapify(arr,i,n):
    largest=i
    rightchild=(2*i)+2
    leftchild=(2*i)+1
    if leftchild<n and arr[rightchild]>arr[largest]:
        largest=rightchild
    if rightchild<n and arr[leftchild]>arr[largest]:
        largest=leftchild
    if i!=largest:
        arr[largest],arr[i]=arr[i],arr[largest]
        heapify(arr,largest,n)
def heapsort(arr):
    l=len(arr)
    for i in range((l//2)-1,-1,-1):
        heapify(arr,i,l)
    print(arr)
    return arr
if __name__=="__main__":
    x=heapsort([1,2,3,4,5,6,7,4,5,6,4,5,6])
    print(x)