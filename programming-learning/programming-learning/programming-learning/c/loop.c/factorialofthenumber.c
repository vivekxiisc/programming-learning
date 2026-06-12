#include<stdio.h>
int main()
{
    int n,fac=1;
    printf("enter the number");
    scanf("%d",&n);
    int i=n;
    while(i!=0)
    {
        fac=fac*i;
        i--;
       
    }
    printf("factorial of given number is %d",fac);
    return 0;

}