class Car:
    def __init__(self,name,amount):
        self.name=name
        self.amount=amount
    def get(self):
        return self.name
    def __del__(self):
        print("Object cleaned")
x=Car("Audi",1000)
print(x.name)
print(x.get())
