# static metods implementation
class Car:
    x="Audi"
    @staticmethod
    def Announce(carname=x):
        print("{0} is on sale".format(carname))
    def Anotherstaticmethod():
        print('called a static method')
    
x=Car()
Car.Announce()
Car.Anotherstaticmethod=staticmethod(Car.Anotherstaticmethod)
Car.Anotherstaticmethod()