arr=[1,3,8,9,7,6,5,2]

def sort(arr):
    for i in range(len(arr)):
        smallest=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[smallest]:
                smallest=j
        if smallest!=i:
            arr[smallest],arr[i]=arr[i],arr[smallest]
    return arr
  
print(sort(arr))