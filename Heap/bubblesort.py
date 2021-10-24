arr=[34,23,12,34,23,45,45,34,2211,12,0]

def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-1-i):
            if(arr[j]>arr[j+1]):
                arr[j+1],arr[j]=arr[j],arr[j+1]
bubblesort(arr)
print(arr)            