class Vehicle:
    def __init__(self,registraion_no,no_of_wheels,color):
        self.registration_no=registartion_no
        self.no_of_wheels=no_of_wheels
        self.color=color
    def getDetails(self):
        print("Registration number is ",self.registration_no)
        print("Number of wheels is ",self.no_of_wheels)
        print("Color is ",color)
class Fourwheeler(Vehicle):
    def __init__(self, registraion_no, no_of_wheels, color,torque,gear_box_type):
        super().__init__(registraion_no, no_of_wheels, color)
        self.torque=torque
        self.gear_box_type=gear_box_type
    def getDetails(self):
        super().getDetails()
        print("Torque is ",self.torque)
        print("Gear box type is ",self.gear_box_type)
if __name__=="__main__":
    f1=Fourwheeler(1234,4,"gray",345,"automatic")
    f1.getDetails()
