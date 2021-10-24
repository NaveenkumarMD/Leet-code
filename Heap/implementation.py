import math
class Heap:
    def __init__(self,maxsize):
        self.heap=[0]*(maxsize+1)
        self.size=1
        self.maxsize=maxsize
        self.front=1
        self.heap[0]=-1*math.inf
    def parent(self,i):
        return i//2
    def leftchild(self,i):
        return i*2
    def rightchild(self,i):
        return i*2+1
    def isleaf(self,i):
        if i>=(self.size//2) and i<=self.size:
            return True
        return False
    def swap(self,i,j):
        self.heap[i],self.heap[j]=self.heap[j],self.heap[i]
    def insert(self,data):
        if self.size>=self.maxsize:
            return 
        self.size+=1
        self.heap[self.size]=data
        current=self.size
        
        while self.heap[current]>self.heap[self.parent(current)]:
            self.swap(current,self.parent(current))
        current=self.parent(current)
    def maxheapify(self,pos):
        if not self.isleaf(pos):
            if self.heap[pos]<self.heap[self.leftchild(pos)] or self.heap[pos]<self.heap[self.rightchild(pos)]:
                if self.heap[self.leftchild(pos)]>self.heap[self.leftchild(pos)]:
                    self.swap(pos,self.leftchild(pos))
                    self.maxheapify(self.leftchild(pos))
                else:
                    self.swap(pos,self.rightchild(pos))
                    self.maxheapify(self.rightchild(pos))
    def builtheap(self):
        for i in range((self.size//2)+1,0,-1):
            self.maxheapify(i)
                
            
    def print(self):
        print(self.heap)
        for i in range(1,(self.size//2)+1):
            x="Node is :{} \n\t left child is {} \n\t right child is {}"
            print(x.format(self.heap[i],self.heap[i*2],self.heap[(i*2)+1]))
        
if __name__ == '__main__':
    maxheap=Heap(20)
    maxheap.insert(4)
    maxheap.insert(5)
    maxheap.insert(6)
    maxheap.insert(7)
    maxheap.insert(8)
    maxheap.insert(9)
    maxheap.insert(10)
    maxheap.print()
    maxheap.builtheap()
    maxheap.print()