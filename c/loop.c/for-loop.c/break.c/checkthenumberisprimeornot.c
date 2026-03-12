#include<stdio.h>
int main()
{
    int n;
    printf("enter a number");
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
    {
        if(n%i==0)
        {
            n=1;
            break;
        }
    }
    if(n==1)
    printf("not prime ");
    else if(n==0)
    printf("prime number");
    else
    printf("compsite");

    return 0;
}


//break statement is used to stop the loop....................