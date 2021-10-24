def migratoryBirds(arr):
    m=0
    dit=[]
    s=set(arr)
    for i in s:
        if arr.count(i)>m:
            m=arr.count(i)
            dit.clear()
            dit.append(i)
        elif arr.count(i)==m:
            dit.append(i)
    return min(dit)