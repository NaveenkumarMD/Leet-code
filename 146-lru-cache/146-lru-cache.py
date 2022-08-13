class Node:
    def __init__(self,key,val):
        self.key,self.val=key,val
        self.prev=None
        self.next=None
            
class LRUCache:

    def __init__(self, capacity: int):
        self.size=capacity
        self.dit={}
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head
    def insert(self,node):
        pre,nex=self.tail.prev,self.tail
        pre.next=nex.prev=node
        node.next,node.prev=nex,pre
    def remove(self,node):
        prv,nex=node.prev,node.next
        prv.next=nex
        nex.prev=prv

    def get(self, key: int) -> int:
        if key in self.dit:
            node=self.dit[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dit:
            self.remove(self.dit[key])
        self.dit[key]=Node(key,value)
        self.insert(self.dit[key])
        if len(self.dit)>self.size:
            lru=self.head.next
            self.remove(lru)
            del self.dit[lru.key]
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)