class Animal{
    void shout(){
        System.out.println("ooo");
    }

    public void test() {
    }  
}
class Cat extends Animal{
    void shout(){
        System.out.println("meow");
    }   
    public void test(){
        System.out.println("Works");
    } 
}
class X{
    public static void main(String[] args) {
        Animal a=new Animal();
        a.shout();
        Cat c=new Cat();
        c.test();
        Animal b=new Cat();
        b.shout();
        b.test();

    }   
}