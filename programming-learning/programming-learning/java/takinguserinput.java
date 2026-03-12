import java.util.Scanner;
public class takinguserinput {
    public static void main(String[] args){
        System.out.println("Taking user input");
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter first number");
        int a=sc.nextInt();
        System.out.println("Enter second number");
        int b=sc.nextInt();
        int product=a*b;
        System.out.println("the product of the given two numbers is ::");
        System.out.println(product);
    }
}
