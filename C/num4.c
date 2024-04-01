#include <stdio.h>
int is_prime(int x)
{
    int i;
    if(x==1) return 0;
    for(i = 2; i < x; i++)
    {
        if(x % i == 0)
        {
            return 0;
        }
        return 1;
    }
}
int next_prime(int x)
{
    while(!is_prime(++x));
    return x;
    //int i;
    //i = x + 1;
    //while (!is_prime(i))
    //{
     //   i++;
    //}
    //return i;
}

void main(void)
{
    int N,i,M;
    printf("입력: ");
    scanf("%d %d", &N,&M);
    for(i = 0; i < M; i++)
    {
        N = next_prime(N);
        printf("%d ", N);
    }
}