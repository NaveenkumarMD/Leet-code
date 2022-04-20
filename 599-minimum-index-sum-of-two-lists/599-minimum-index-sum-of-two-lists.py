class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dit={}
        for i in list1:
            if i in list2:
                dit[i]=list1.index(i)+list2.index(i)
        dit={
            k:v for k,v in sorted(dit.items(),key=lambda item:item[1])
        }
        x=min(dit.values())
        arr=[]
        for i,j in dit.items():
            if j==x:
                arr.append(i)
            elif j>x:
                return arr
        return arr
        