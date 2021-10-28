def topKFrequent(self, nums, k):
    dit={}
    for i in nums:
        if i in dit:
            continue
        else:
            dit[i]=nums.count(i)
    print (dit)
    x=sorted(dit,key=dit.get,reverse=True)
    return x[:k]