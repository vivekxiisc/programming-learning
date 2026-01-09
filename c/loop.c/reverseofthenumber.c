#include<stdio.h>
int main()
{
    int n,ld=0,rev=0;
    printf("enter the number");
    scanf("%d",&n);
    while(n>0){
    ld=n%10;
    rev=rev+ld;
    rev=rev*10;
    n=n/10;
    }
    rev=rev/10;
    printf("reverse of the number %d",rev);

    return 0;
}