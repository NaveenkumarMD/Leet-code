
if __name__=="__main__" :
    arr=[1,3,2,6,1,2]
    k=5
    def check(arr,k):
        arr1=[]
        for i in arr:
            if(k-1<=0):
                arr1.append(k-1)
            else:
                arr1.append(k-(i%k))
        print(arr)
        print(arr1)
        s=0
        for i in range(len(arr)):
            if(arr1[i] in arr):
                print(arr[i])
                s+=1
        return s
    x=check(arr,3)
    print(x)