#include<stdio.h>
int main()
{
    int n,nst,nsp;
    printf("enter a number");
    scanf("%d",&n);
   nsp=1;
   nst=n-1;
   
    for(int m=1;m<=2*n-1;m++)
       {
            printf("%c",m+64);
           
       }
       printf("\n");
    for(int i=1;i<=n-1;i++){
        int a=65;
        for(int k=1;k<=nst;k++)     //star triangle
        {
            printf("%C",a);
            a++;

        }
        for(int j=1;j<=nsp;j++)  // spaces
        {
            printf(" ");
            a++;
        }
        
      for(int l=1;l<=nst;l++)     //star triangle
        {
            printf("%C",a);
            a++;   
        }
        printf("\n");
        nsp+=2;
        nst--;
       
       
    }
    return 0;
}

//ABCDEFG
//ABC EFG
//AB   FG     
//A     G