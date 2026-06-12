#include<stdio.h>
int main()
{
    int n,count=0;
    printf("enter the number");
    scanf("%d",&n);
    while(n>0)
    {
        n=n/10;
        count++;
    }
    printf("number of digit =%d",count);
    return 0;
}



//eg :: 546/10=54-------> count=1
//       56/10=5 -------> count=1+1
//        6/10=0--------> count=1+1+1=3