class Vehicle:
    def setter(self,name,speed):
        self.__name=name
        self.__speed=speed
    def getter(self):
        print(self.__name,self.__speed)
if __name__ == '__main__':
    v=Vehicle()
    v.setter('car',100)
    v.getter()

