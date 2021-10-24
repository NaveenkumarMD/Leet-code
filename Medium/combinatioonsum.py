if __name__ == "__main__":
    candidates = [2, 3, 6, 7]
    target = 7

    def combinationsum(candidates, target):
        res = []
        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if i >= len(candidates) or total > target:
                return
            curr.append(candidates[i])
            dfs(i,curr,total+candidates[i])
            curr.pop()
            dfs(i+1,curr,total)
        dfs(0,[],0)
        return res        
        
    res=candidatescombinationsum(candidates,target)
    print(res)
    pass

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:       
        
        result = []
        
        def backtracking(remain, comb, start):
            
            if remain == 0:
                ## here we do deepcoy of 'comb' or else it does
                ##shallow copy where it will append empty list because
                ## we pop all elements from comb at the end which reflects
                ## in the 'result' array
                result.append(comb[:])
                return 
            
            if remain < 0:
                return 
            
            for i in range(start, len(candidates)):
                
                comb.append(candidates[i])
                
                backtracking(remain - candidates[i], comb, i)
                
                comb.pop()
        
        
        backtracking(target, [], 0)
        
        
        return result