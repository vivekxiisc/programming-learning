#include<stdio.h>
int main()
{
    int r,c,a=1;
    printf("enter no of rows");
    scanf("%d",&r);
     printf("enter no of column");
    scanf("%d",&c);
    
    for(int i=1;i<=r;i++)
    {
        for(int j=1;j<=c;j++ )
        {
            printf("%d ",a);
            a++;

        }
        printf("\n");
        
        c++;
        
    }
        return 0;
}