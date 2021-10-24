def heapify(arr,n,i):
    largest=i
    leftchild=2*i+1
    rightchild=2*i+2
    if leftchild<n and arr[leftchild]>arr[largest]:
        largest=leftchild
    if rightchild<n and arr[rightchild]>arr[largest]:
        largest=rightchild
    if largest!=i:
        arr[i],arr[largest]=arr[largest],arr[i]
        heapify(arr,n,largest)
        
def heapsort(arr):
    n=len(arr)
    for i in range(n//2 -1,-1,-1):
        heapify(arr,n,i)
    for i in range(n-1,0,-1):
        arr[0],arr[i]=arr[i],arr[0]
        heapify(arr,i,0)
    
if __name__ == '__main__':
    arr=[23,45,24,2,4,5]
    heapsort(arr)
    print(arr)