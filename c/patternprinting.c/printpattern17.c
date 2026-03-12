#include<stdio.h>
int main()
{
    int n,nst=1,nsp=3;  // nst= no of star in first row  &  nsp= no of spaces in first row
    printf("enter no of rows");
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
    {
      for(int j=1;j<=nsp;j++)   // for spaces
      {
        printf(" ");
      }
      for(int k=1;k<=nst;k++)  //   for star
      {
        printf("*");
      }
      printf("\n");
      nsp--;
      nst=nst+2;
    }
    return 0;
}
    //   *
    //  ***
    // *****
    //*******