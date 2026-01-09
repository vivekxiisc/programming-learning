#include<stdio.h>
int main()
{
    int n, fac=1;
    printf("enter a number");
    scanf("%d",&n);
    for(int i=1;i!=n+1;i++){
        fac=fac*i;
    
    printf("factorial of the given numbers are %d \n",fac);
    }
    return 0;
}