class vehicle{
    private String name;
    private int speed;
    public void setter(String name, int speed){
        this.name = name;
        this.speed = speed;
    }
    public void getter(){
        System.out.println("Name: "+name);
        System.out.println("Speed: "+speed);
    }

}
public class Encapsulation {
    public static void main(String[] args) {
        vehicle v = new vehicle();
        v.setter("Car",100);
        v.getter();
    }
}
