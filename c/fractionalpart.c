#include<stdio.h>
int main()
{
    float a;
    int b;
   float c;
    printf("enter a number");
    scanf("%f",&a);
    b=a;
    c=a-b;
    printf("fractional part is %f",c);

    return 0;
}