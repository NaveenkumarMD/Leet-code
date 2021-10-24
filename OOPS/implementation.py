class Car:
    count=0
    def __init__(self,modelname,year):
        self.modelname=modelname
        self.year=year
        Car.count+=1
    def display(self):
        print(self.modelname,self.year)

ford=Car("z1",2015)
ford.display()
mitusbo=Car("f2",2012)
print(Car.count)