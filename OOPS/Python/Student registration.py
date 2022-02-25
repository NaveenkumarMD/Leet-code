import random
class Registartion:
    loginarray=[]
    def __init__(self, name,login,password):
        self.name = name
        self.login = login
        self.password = password
        self.id=None
    def validate(self):
        print("login contains",Registartion.loginarray)
        if self.login in Registartion.loginarray:
            print("Login already taken",Registartion.loginarray)
            return False
        else:
            # check the password contains atleast 6 digits and first letter uppercase   and 1 digit
            if len(self.password)>=6 and self.password[0].isupper() and any(char.isdigit() for char in self.password):
                return True
            return False
    def register(self):
        if self.validate():
            Registartion.loginarray.append(self.login)
            #assign a random 5 digit number to id
            self.id=random.randint(10000,99999)
            print(self.id,self.login,self.password)
            return True
        else:
            print("Registration Failed")
            return False
if __name__=="__main__":
    n=int(input("Enter the number of students: "))
    for i in range(n):
        name=input("Enter the name: ")
        login=input("Enter the login: ")
        password=input("Enter the password: ")
        obj=Registartion(name,login,password)
        obj.register()

