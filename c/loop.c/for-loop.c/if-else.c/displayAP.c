#include<stdio.h>
int main()
{
    int a,d,n;
    printf("enter first term\n");
    scanf("%d",&a);
    printf("enter common difference");
    scanf("%d",&d);
    printf("enter number of terms");
    scanf("%d",&n);
    for(int i=a;i<=a+(n-1)*d;i=i+d)
    printf("%d  ",i);
    return 0;

}