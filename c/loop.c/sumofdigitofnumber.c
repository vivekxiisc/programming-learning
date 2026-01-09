#include<stdio.h>
int main()
{
    int n, ld, sum=0;
    printf("enter the number");
    scanf("%d",&n);
    while(n>0)
    {
        ld=n%10;
        sum=sum+ld;
        n=n/10;
    }
    printf("sum of the digit =%d",sum);
    return 0;
}