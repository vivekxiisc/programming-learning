#include<stdio.h>
int main()
{
    int r,c,d;
    printf("enter number of rows");
    scanf("%d",&r);
    printf("enter number things in one  row");
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