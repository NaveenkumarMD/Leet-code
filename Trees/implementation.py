class TreeNode:
    def __init__(self,data=None,parent=None):
        self.data=data
        self.parent=parent
        self.children=[]
    def add_children(self,child_node):
        if child_node in self.children:
            return 
        else:
            self.children.append(child_node)
            child_node.parent=self
    def get_level(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent
        return level
            
    def printTree(self):
        print(self.get_level()*" "+self.data)
        if not self.children:
            return 
        for child in self.children:
            child.printTree()
def implement():
    electronics=TreeNode("electronics")
    
    tvs=TreeNode("Tvs")
    
    fridges=TreeNode("fridges")
    electronics.add_children((fridges))
    electronics.add_children(tvs)
    print(fridges.get_level())
    print(electronics.get_level())
    return electronics

if __name__=='__main__':
    root=implement()
    root.printTree()
    pass