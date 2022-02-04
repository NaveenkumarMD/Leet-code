class Solution:
    def count(self,x):
        temp=x[0]
        temp_count=1
        s=""
        for i in range(1,len(x)):
            if temp == x[i]:
                temp_count+=1
            else:
                s+=str(temp_count)+temp
                temp=x[i]
                temp_count=1
        return s+str(temp_count)+temp
    def countAndSay(self, n: int) -> str:
        arr=['1']
        for i in range(n-1):
            arr.append(self.count(str(arr[i])))
        return arr[-1]
        