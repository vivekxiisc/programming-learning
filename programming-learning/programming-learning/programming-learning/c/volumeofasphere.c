#include<stdio.h>
#include<math.h>
int main()
{
    int r;
    float v;
    //float pi=3.14;
    printf("enter radius of the sphere");
    scanf("%d",&r);
    v=(4*r*r*r*3.14)/3;
    printf("volume of the sphere= %f",v);
    return 0;
}
