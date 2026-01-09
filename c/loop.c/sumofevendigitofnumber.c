#include<stdio.h>
int main()
{
    int n,ld,sum=0;
    printf("enter a number");
    scanf("%d",&n);
    while(n>0)
    {
        ld=n%10;
        if(ld%2==0){
        sum=sum+ld;
        }
        n=n/10;  
    }
    printf("sum=%d",sum);
    return 0;
}