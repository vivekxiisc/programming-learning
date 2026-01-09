#include<stdio.h>
int main()
{
    int n ;
    printf("enter a number");
    scanf("%d",&n);
    if(n<0){
    n =n*(-1);
    printf("absolute value is %d",n);
    }
    else 
    printf("absolute value is %d",n);
    
    return 0;
}