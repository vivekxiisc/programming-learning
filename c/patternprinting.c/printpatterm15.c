#include<stdio.h>
int main()
{
    int r;
    printf("enter no of rows");
    scanf("%d",&r);
    
    for(int i=1;i<=r;i++)
    {
      
        for(int j=1;j<=r-i;j++ )
        {
          
          printf(" ");
          
          }
          for(int k=1;k<=i;k++)
          {
            printf("*");
          }
        
        for(int l=1;l<=r-i;l++ )
        {
          
          printf("*");
          
          }
          for(int m=2;m<=i;m++)
          {
            printf(" ");
          }
        printf("\n");
        }
        return 0;
}