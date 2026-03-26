#include <stdio.h>
#define Pi 3.14
int main()
{
    double a, area;
    scanf("%lf", &a);
    area = Pi * a * a;
    printf("%.2lf\n", area);
    return 0;
}