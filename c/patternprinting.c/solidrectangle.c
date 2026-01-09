#include<stdio.h>
int main()
{
    int r,c;
    printf("enter the number of row");
    scanf("%d",&r);
    printf("enter the number of columns");
    scanf("%d",&c);
    for(int i=1;i<=r;i++)
    {
        for(int j=1;j<=c;j++)
        {
            printf("*");
        }
        printf("\n");
    }
    return 0;
}