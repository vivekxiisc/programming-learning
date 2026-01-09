import java.util.Scanner;
public class userinput2 {
    public static void main(String[] args){
        Scanner sc= new Scanner(System.in);
        System.out.println("ENTER YOUR BIRTH YEAR");
        int a=sc.nextInt();
        String b="You are very ugly.\nYou are very lazy.\nYou are very talkative.\nYou are very poor.\nYou are not good in study\n";
        String c="YOU ARE VERY INTELLIGENT AND BRILLIANT ";
        if(a==2005){
            System.out.println("FEW THINGS ABOUT YOU");
            System.out.println(b);
        }
        else
        System.out.println(c);
    }
}
