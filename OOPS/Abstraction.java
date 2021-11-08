interface Shape{
    abstract double area();
    abstract double perimeter();
}
class Square implements Shape{
    private double side;
    Square(double side){
        this.side = side;
    }
    @Override
    public double area(){
        return side*side;
    }
    @Override
    public double perimeter(){
        return 4*side;
    }
}
class Abstraction {
    public static void main(String[] args) {
        Square s = new Square(5);
        System.out.println("Area of square is: "+s.area());
        System.out.println("Perimeter of square is: "+s.perimeter());
    }
}
