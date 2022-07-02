class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfsutil(g,vis,path,src,dest,res):
            vis.add(src)
            path.append(src)
            if src==dest:
                res.append(path.copy())
            else:
                for i in g[src]:
                    if i not in vis:
                        print(i)
                        dfsutil(g,vis,path,i,dest,res)
            path.pop()
            vis.remove(src)
        vis=set()
        res=[]
        path=[]
        dfsutil(graph,vis,path,0,len(graph)-1,res)
        return res