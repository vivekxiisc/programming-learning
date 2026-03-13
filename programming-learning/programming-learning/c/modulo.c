#include<stdio.h>
int main()
{
    int a,b,c;
    printf("enter a number");
    scanf("%d",&a);
    printf("enter second number");
    scanf("%d",&b);
    c=a%b;
    printf("remainder=%d",c);
    return 0;

}