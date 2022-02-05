class Solution:
    def getmax(self,arr):
        maxleft=[]
        maxl=0
        for i in arr:
            if i>=maxl:
                maxleft.append(maxl)
                maxl=i
            else:
                maxleft.append(maxl)
        return maxleft
    def trap(self, height) -> int:
        maxleft=self.getmax(height)
        maxright=list(reversed(self.getmax(list(reversed(height)))))
        minarr=[]
        for i in range(len(maxleft)):
            minarr.append(min(maxleft[i],maxright[i]))
        print(minarr)
        total=0
        for i in range(len(height)):
            total+=max(minarr[i]-height[i],0)
        return total