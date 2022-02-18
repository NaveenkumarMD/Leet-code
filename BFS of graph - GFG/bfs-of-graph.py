#User function Template for python3

class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        queue=[]
        visited=[False]*V
        queue.append(0)
        visited[0]=True
        arr=[]
        while queue:
            root=queue.pop(0)
            arr.append(root)
            for i in adj[root]:
                if not visited[i]:
                    queue.append(i)
                    visited[i]=True
        return arr
#{ 
#  Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends