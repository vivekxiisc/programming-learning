#include<stdio.h>
#include<math.h>
int main()
{
    int a,b,c;
    printf("enter first number");
    scanf("%d",&a);
    printf("enter second number");
    scanf("%d",&b);
    c=pow(a,b);
    printf("power  =  %d",c);
    return 0;
}