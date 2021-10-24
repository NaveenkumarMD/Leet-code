def solve(arr):
    c=0
    for i in range(len(arr)):
        if arr[i]!=c:
            temp=0
            for j in range(i+1,len(arr)):
                if arr[j]==c:
                    temp=j
                    break
            if temp!=0:
                arr[temp],arr[i]=arr[i],arr[temp]
            else:
                c+=1
    return arr            

                
if __name__=="__main__":
    x=solve([int(x) for x in input().split()])
    print(x)