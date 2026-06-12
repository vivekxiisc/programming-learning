#include<stdio.h>
int main()
{
    int n;
    printf("enter a number ");
    scanf("%d",&n);
    if(n%5==0&&n%3==0)
    {
        if(n%15!=0)
        printf("%d is diviible by 5 and 3 but not by 15",n);
        else
        printf("%d is  diviible by 5 and 3 as wll as by   15",n);
    }
    else
    printf("%d is not diviible by 5 and 3 as well as by   15",n);
        return 0;
}