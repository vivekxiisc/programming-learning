#include<stdio.h>
int fibo(int n)
{
    if(n==0) return ;
    printf("%d",fibo(n-6));
    return fibo(n-6)+fibo(n-5);
   
}
int main()
{
    int n;
    printf("enter number");
    scanf("%d",&n);
    fibo(n);
   printf("%d ",fibo(n));
        return 0;
}