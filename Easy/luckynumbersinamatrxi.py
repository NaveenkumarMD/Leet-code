if __name__=="__main__":
    arr=[[7,8],[1,2]]
    def lucky(arr):
        arrt=[max(i) for i in list(zip(*arr))]
        print (arrt)
        res=[]
        for i in range(len(arr)):
            x=min(arr[i])
            index=arr[i].index(x)
            if arrt[index]==x:
                res.append(x)                   
        return res
    
    x=lucky(arr)
    print(x)