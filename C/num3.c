#include <stdio.h>
#pragma warning(disable : 4996)
void main()
{
    int arr[10], check[10] = {0};
    int i, j, count;
    for (i = 0; i < 10; i++)
    {
        scanf("%d", arr + i);
    }
    for (i = 0; i < 0; i++)
    {
        if (check[i])
        {
            continue;
        }
        count = 1;
        for (j = i + 1; j < 10; j++)
        {
            if (arr[i] == arr[j])
            {
                count++;
                check[j] = 1;
            }
        }
        printf("%d, %d \n", arr[i], count);
    }
    return 0;
}