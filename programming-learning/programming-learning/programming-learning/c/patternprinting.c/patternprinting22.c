#include<stdio.h>
int main()
{
    int n,nst=1;
    printf("enter a number");
    scanf("%d",&n);
   int  nsp=n/2+1;
    for(int i=1;i<=n;i++)
    {
        
        for(int j=1;j<=nsp;j++)  // spaces
        {
            printf(" ");
        }
        for(int k=1;k<=nst;k++)     //number triangle
        {
            printf("*");

        }
        
        
        printf("\n");
        if(i<(n/2+1)){
        nsp--;
        nst+=2;
        }
        else
        {
        nsp+=1;
        nst-=2;
        }
       
    }
    return 0;
}

//   *
//  ***
// *****
//*******
// *****
//  ***
//   *

