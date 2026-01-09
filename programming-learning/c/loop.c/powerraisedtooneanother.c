#include<stdio.h>
int main()
{
    int a,b,pow=1;
    printf("enter first number");
    scanf("%d",&a);
    printf("enter second number");
    scanf("%d",&b);
    for(int i=1;i<=b;i++)
    {
        pow=pow*a;
    }
    printf("power  =  %d",pow);
    return 0;
}
