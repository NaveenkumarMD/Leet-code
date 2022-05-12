class MyHashMap:

    def __init__(self):
        self.keys=[]
        self.values=[]

    def put(self, key: int, value: int) -> None:
        if key not in self.keys:
            self.keys.append(key)
            self.values.append(value)
        else:
            x=self.keys.index(key)
            self.values[x]=value

    def get(self, key: int) -> int:
        if key not in self.keys:
            return -1
        else:
            return self.values[self.keys.index(key)]
    def remove(self, key: int) -> None:
        if key not  in self.keys:
            return 
        else:
            x=self.keys.index(key)
            self.keys.pop(x)
            self.values.pop(x)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)