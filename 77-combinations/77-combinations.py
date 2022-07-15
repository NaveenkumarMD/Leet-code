class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = [i+1 for i in range(n)]
        res = []

        def util(i, temp):
            if len(temp) == k:
                if temp not in res:
                    res.append(temp[:])
            elif len(temp) > k:
                return
            for j in range(i,len(arr)):
                temp.append(arr[j])
                util(j+1,temp)
                temp.pop()
        util(0,[])
        return res