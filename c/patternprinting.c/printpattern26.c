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
            printf("%d",m);
           
       }
       printf("\n");
    for(int i=1;i<=n-1;i++){
      int a=1;
        for(int k=1;k<=nst;k++)     //number triangle
        {
            printf("%d",a);
            a++;

        }
        for(int j=1;j<=nsp;j++)  // spaces
        {
            printf(" ");
            a++; 
        }
      for(int l=nst;l>=1;l--)     //opposite number  triangle
        {
            printf("%d",l);
           
        }
        printf("\n");
        nsp+=2;
        nst--; 
    }
    return 0;
}
     //1234567
     //123 321
     //12   21   
     //1     1
