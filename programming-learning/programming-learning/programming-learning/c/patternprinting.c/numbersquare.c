#include<stdio.h>
int main()
{
    int r,c;
    printf("enter no of rows");
    scanf("%d",&r);
    printf("enter no of things in one row");
    scanf("%d",&c);
    for(int i=1;i<=r;i++)
    {
        for(int j=1;j<=c;j++)
        {
            printf("%d ",j);
        }
        printf("\n");
    }
    return 0;
}