class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dit={}
        for i in list1:
            if i in list2:
                dit[i]=list1.index(i)+list2.index(i)

        x=min(dit.values())
        arr=[]
        for i,j in dit.items():
            if j==x:
                arr.append(i)
        return arr
        