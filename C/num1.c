
/*
int main(void)
{
	int a = 0;
	int a1 = 0;
	int a2 = 0;
	int num = 0;
	scanf("%d", &num);
	if (num % 2 == 0)
	{
		a = 1;
	}
	else if (num % 3 == 0)
	{
		a1 = 1;
	}
	else
	{
		a2 = 1;
	}

	if (a == 1 && a1 == 1 && a2 == 1)
	{
		printf("A");
	}
	else if (a == 1 && a1 == 1)
	{
		printf("B");
	}
	else if (a == 1 && a2 == 1)
	{
		printf("C");
	}
	else if (a1 == 1 && a2 == 1)
	{
		printf("D");
	}
	else if (a1 == 0 && a2 == 0 && a == 0)
	{
		printf("F");
	}
	else
	{
		printf("E");
	}
}
*/
#include <stdio.h>
#pragma warning (disable:4996)
void main()
{
    int N, b = 0;
    scanf("%d", &N);
    b |= N%2 == 0 ? 1:0; // |= or 역할  '?'앞의 조건이 참이면 1 아니면 0
    b |= N%3 == 0 ? 2:0;
    b |= N%5 == 0 ? 4:0;
    switch(b)
    {
        case 7:
            printf("A");
            break;
        case 3:
            printf("B");
            break;
        case 5:
            printf("C");
            break;
        case 6:
            printf("D");
            break;
        case 1:
        case 2:
        case 4:
            printf("E");
            break;
        default:
            printf("N");
            break;
    }
}
