def check(n,arr,votes):
    i=0
    count=len(votes)
    fifty=count//2
    while i<len(votes[0]):
        if n==1:
            for i in dit:
                return arr[i-1]
        dit={i:0 for i in range(1,n+1)}
        for j in range(len(votes)):
            dit[votes[j][i]]+=1
        small=999
        for i,j in dit.items():
            if j>fifty:
                return arr[i-1]
            if j<small:
                small=j

        x=dit
        dit = {key:val for key, val in dit.items() if val != small}
        if len(dit)==0:
            for i in x:
                return arr[i-1]
        i+=1

if __name__=="__main__":
    n=3
    arr=[
        "John Doe",
        "jane Smith",
        "Sriharan Sirhan"
    ]
    votes=[
        [1,2,3],
        [2,1,3],
        [2,3,1],
        [1,2,3],
        [3,1,2]
    ]
    x=check(n,arr,votes)
    print(x)