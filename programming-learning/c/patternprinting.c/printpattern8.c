#include<stdio.h>
int main()
{
    int r,c,a,n;
    printf("enter no of rows");
    scanf("%d",&r);
    //printf("enter the no of things in one row");
    //scanf("%d",&c);
    for(int i=1;i<=r;i++)
    {
        for(int j=1;j<=r;j++ )
        {
            a=r/2+1;
            if(i==a||j==a)
            printf("*");
            else
            printf(" ");
            
        }
        printf("\n");
        
    }
        return 0;
}