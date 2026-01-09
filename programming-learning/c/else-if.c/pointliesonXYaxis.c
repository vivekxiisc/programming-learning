#include<stdio.h>
int main()
    {
        int x,y;
        printf(" enter the value of x and y coordinates");
        scanf("%d%d",&x,&y);
        if(x==0&&y==0)
        printf("ORIGIN");
        else if(x!=0&&y!=0)
        printf("BOTH AXIS");
        else if(x==0)
        printf("Y-AXIS");
        else
        printf("X -AXIS");

        return 0;
    }
