#include<stdio.h>
int main()
{
    int n,nst=1;
    printf("enter a number");
    scanf("%d",&n);
   int  nsp=n-1;
    for(int i=1;i<=n;i++)
    {
        int a=i-1;
        for(int j=1;j<=nsp;j++)  // spaces
        {
            printf(" ");
        }
        for(int k=1;k<=nst;k++)     //number triangle
        {
            printf("%d",k);

        }
        for(int l=1;l<=i-1;l++)  // extra things
        {
            printf("%d",a);
            a--;
        }
        printf("\n");
        nsp--;
        nst+=1;
       
    }
    return 0;
}

//   1
//  121
// 12321
//1234321

