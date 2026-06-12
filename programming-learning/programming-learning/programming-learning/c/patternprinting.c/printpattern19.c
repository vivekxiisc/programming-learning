#include<stdio.h>
int main()
{
    int n,nst=1;
    printf("enter a number");
    scanf("%d",&n);
   int  nsp=n-1;
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=nsp;j++)
        {
            printf(" ");
        }
        for(int k=1;k<=nst;k++)
        {
            printf("%c",64+k);

        }
        printf("\n");
        nsp--;
        nst+=2;
    }
    return 0;
}



//   A
//  ABC
// ABCDE
//ABCDEFG




