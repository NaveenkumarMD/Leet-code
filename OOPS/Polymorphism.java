class Animal {
    String name;
    Animal(String name) {
        this.name = name;
    }
    public void speak() {
        System.out.println("I am an animal");
    }
}

class Dog extends Animal {
    Dog(String name) {
        super(name);
    }
    public void speak() {
        System.out.println("I am a dog");
    }
}

class Cat extends Animal {
    Cat(String name) {
        super(name);
    }
    public void speak() {
        System.out.println("I am a cat");
    }
}

public class Polymorphism {
    public static void main(String[] args) {
        Animal a = new Animal("animal");
        a.speak();
        Dog d = new Dog("dog");
        d.speak();
        Cat c = new Cat("cat");
        c.speak();
    }
}
