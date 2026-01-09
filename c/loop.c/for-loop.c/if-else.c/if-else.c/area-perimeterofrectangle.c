#include<stdio.h>
int main()
{
    int l,b,area=0,perimeter=0;
    printf("enter length of the rectangle");
    scanf("%d",&l);
    printf("enter the bredth of the rectangle");
    scanf("%d",&b);
    area=l*b;
    perimeter=2*(l+b);
    if(area>perimeter)
    printf("area is greater than perimeter");
    else
    printf("perimeter is greater than area ");
    return 0;
}