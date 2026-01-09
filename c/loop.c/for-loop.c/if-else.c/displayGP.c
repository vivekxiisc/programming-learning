#include<stdio.h>
#include<math.h>
int main()
{
    int a,r,n,c;
    printf("enter first term\n");
    scanf("%d",&a);
    printf("enter common ratio");
    scanf("%d",&r);
    printf("enter number of terms");
    scanf("%d",&n);
    c=n-1;
    for(int i=a;i<=a*pow(r,n-1);i=i*r)
    printf("%d  ",i);
    return 0;

} 
//here a*pow(r,n-1) is the formula of nth term of GP




