def findMedianSortedArrays(nums1, nums2):
    i=0
    j=0
    arr=[]
    while(i<len(nums1) and j<len(nums2)):
        if(nums1[i]<=nums2[j]):
            arr.append(nums1[i])
            i+=1
        else:
            arr.append(nums2[j])
            j+=1
    while i<len(nums1):
        arr.append(nums1[i])
        i+=1
    while j<len(nums2):
        arr.append(nums2[j])
        j+=1
    print(arr)
    if(len(arr)%2==1):
        return arr[len(arr)//2]
    else:
        return (arr[len(arr)//2]+arr[(len(arr)//2)-1] )/2

x=findMedianSortedArrays([1,2],[3,4])
print(x)