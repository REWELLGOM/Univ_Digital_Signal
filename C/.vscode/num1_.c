#include <stdio.h>
#pragma warning (disable:4996)

int main()
{
    int N, b = 0;
    scanf("%d", &N);
    b |= N % 2 == 0 ? 1 : 0; 
    b |= N % 3 == 0 ? 2 : 0;
    b |= N % 5 == 0 ? 4 : 0;

    switch (b) {
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
    return 0; 
}



// |= 연산자를 이용한 비트 OR 연산