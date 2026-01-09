import java.util.Scanner;

public class conditionalstatements2 {
    public static void main(String[] args){
        Scanner sc =new Scanner(System.in);
        System.out.println("Enter your age:");
        int a=sc.nextInt();
        if(a<=18 && a>0)
        {
            System.out.println("You are minor....");
        }
         if(a<=0)
         {
        System.out.println("Invalid age formate....");
        }
        else if (a==100)
      {
      System.out.println("centuary");
      }
        else {
        System.out.println("you are not minor....");
        }
    
    