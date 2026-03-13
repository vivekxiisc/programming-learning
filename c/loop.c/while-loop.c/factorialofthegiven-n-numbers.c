#include<stdio.h>
int main()
{
    int n,i=1,fac=1;
    printf("enter a number");
    scanf("%d",&n);

    while(i!=n+1){
        fac=fac*i;
    
    printf("factorial of the given numbers are %d \n",fac);
    i++;
    }
    return 0;
}