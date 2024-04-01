#include <stdio.h>
#pragma warning (disable:4996)
void main()
{
    int N;
    int b = 0;
    scanf("%d", &N);

    while (N >= 10)
    {
        b = 0;
        while (N)
        {
            b += N % 10;
            N /= 10;
        }
        N = b;
    }
    printf("%d", N);
}
