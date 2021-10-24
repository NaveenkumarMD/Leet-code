class Car{
    int modelyear;
    String modelname;
    Car(String modelname,int modelyear){
        this.modelname=modelname;
        this.modelyear=modelyear;
    }
    void display(){
        System.out.println(this.modelname+this.modelyear);
    }
}
class Main{
    public static void main(String args[]){
        Car ford=new Car("forda2",34);
        ford.display();
    }
}