#include<stdio.h>
int main()
{
    int r;
    printf("enter no of rows");
    scanf("%d",&r);
    
    for(int i=1;i<=r;i++)
    {
        for(int j=1;j<=r;j++ )
        {
            if(i==1||i==r||j==1||j==r)
            printf("*");
            else 
            printf(" ");
          
            
        }
        printf("\n");
        
    }
        return 0;
}