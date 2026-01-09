#include<stdio.h>
int main()
{
    int n;
    printf("enter a number");
    scanf("%d",&n);
    if(n>99 && n<1000 )
    printf("three digit number");
    else
    printf("not a three digit number");    
    return 0;

}