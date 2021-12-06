class Solution:
    def combinationSum2(self, candidates, target: int):
        result=[]
        def dfs(curr,index,temp):
            if temp==0:
                if sorted(curr) not in result:
                    result.append(sorted(curr[:]))
                return
            if temp<0:
                return 
            for i in range(index,len(candidates)):
                curr.append(candidates[i])
                dfs(curr,i+1,temp-candidates[i])
                curr.pop()
        dfs([],0,target)
        print(result)
    

x=Solution()
y=x.combinationSum2([10,1,2,7,6,1,5],8)
        