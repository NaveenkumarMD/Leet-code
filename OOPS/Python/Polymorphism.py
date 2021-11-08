class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("I am an animal")
class Cat(Animal):
    def speak(self):
        print("I am a cat")
class Dog(Animal):
    def speak(self):
        print("I am a Dog")
if __name__ == "__main__":
    animal = Animal("Animal")
    cat = Cat("Cat")
    dog = Dog("Dog")
    animal.speak()
    cat.speak()
    dog.speak()