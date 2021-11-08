class Vehicle:
    def __init__(self,reg_no,color):
        self.reg_no=reg_no
        self.color=color
    def getColor(self):
        print("The color of the car is",self.color)

if __name__=="__main__":
    f1=Vehicle(1233,"red")
    f1.getColor()
        