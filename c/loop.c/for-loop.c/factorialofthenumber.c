#include<stdio.h>
int main()
{
    int n,fac=1;
    printf("enter the number");
    scanf("%d",&n);
    for(int i=n;i!=0;i--)
    {
        fac=fac*i;
       
    }
    printf("factorial of given number is %d",fac);
    return 0;

}