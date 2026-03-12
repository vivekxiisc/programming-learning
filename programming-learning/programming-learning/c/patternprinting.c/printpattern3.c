#include<stdio.h>
int main()
{
    int r,c;
    printf("enter no of rows");
    scanf("%d",&r);
    printf("enter the last term of  one row");
    scanf("%d",&c);
    for(int i=1;i<=r;i++)
    {
        for(int j=1;j<=c;j++ )
        {
            if(j%2!=0)
            printf("%d",j);
        }
        printf("\n");
        c=c+2;
    }
        return 0;
}