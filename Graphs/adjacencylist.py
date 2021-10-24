class AdjNode:
    def __init__(self,location):
        self.vertex=location
        self.next=None
class Graph:
    def __init__(self,V):
        self.V=V
        self.graph=[None for i in range(self.V)]
    def add_edge(self,src,dest):
        srcNode=AdjNode(src)
        srcNode.next=self.graph[dest]
        self.graph[dest]=srcNode
        
        destNode=AdjNode(dest)
        destNode.next=self.graph[src]
        self.graph[src]=destNode
    def print(self):
        for i in range(self.V):
            temp=self.graph[i]
            print("vertex is {}\n".format(i))
            while temp:
                print("-> {}".format(temp.vertex),end="")
                temp=temp.next
            print("\n")
            
if __name__ =='__main__':
    graph = Graph(5)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.print()