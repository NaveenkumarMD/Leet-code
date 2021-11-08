// class Vehicle {
//     int registration_no;
//     int no_of_wheels;
//     String color;
//     Vehicle(int registration_no,int no_of_wheels,String color){
//         this.registration_no=registration_no;
//         this.no_of_wheels=no_of_wheels;
//         this.color=color;
//     }
//     void getDetails(){
//         System.out.println("Registration number is "+this.registration_no);
//         System.out.println("Number of wheels is "+this.no_of_wheels);
//         System.out.println("Color is "+this.color);
//     }
// }
// class Fourwheeler extends Vehicle{
//     int torque;
//     String gear_box_type;
//     Fourwheeler(int registration_no,int no_of_wheels,String color,int torque,String gear_box_type){
//         super(registration_no, no_of_wheels, color);
//         this.gear_box_type=gear_box_type;
//         this.torque=torque;
//     }
//     void getDetails(){
//         super.getDetails();
//         System.out.println("Torque is "+this.torque);
//         System.out.println("Gear box type is  "+this.gear_box_type);
//     }
// }
// public class Inheritance{
//     public static void main(String [] args){
//         Fourwheeler f1=new Fourwheeler(1234, 4,"gray", 345, "automatic");
//         f1.getDetails();
//     }
// }