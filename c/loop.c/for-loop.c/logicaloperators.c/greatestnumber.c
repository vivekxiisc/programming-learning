#include<stdio.h>
int main()
{
    int a,b,c;
    printf("enter first number");
    scanf("%d",&a);
    printf("enter second number");
    scanf("%d",&b);
    printf("enter third number");         // here this program is based on nested if-else
    scanf("%d",&c);
    if(a>b&&b>c)
    printf("%d is greatest",a);
    if(b>a&&a>c)
    printf("%d is greatest",b);
    else
    printf("%d is greatest",c);
    return 0;
}