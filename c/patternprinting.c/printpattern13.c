#include<stdio.h>
int main()
{
    int r,c,a=1;
    printf("enter no of rows");
    scanf("%d",&r);
    
    for(int i=1;i<=r;i++)
    {
     
        for(int j=1;j<=i;j++ )
        {
            if((i+j)%2==0)
          printf("");
          else
          printf("0");
        
          
          }
        printf("\n");
        }
        return 0;
}