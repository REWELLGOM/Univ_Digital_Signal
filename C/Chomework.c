#include <stdio.h>
#include <stdlib.h>

//use qsort
/*
int comp(const void* pv1,const void* pv2)
{
    int *p1, *p2;
    p1 = (int*) pv1;
    p2 = (int*) pv2;

    return *p1, *p2;
}

void main()
{
    int i, arr[10];
    for(i = 0; i<10;i++)
    {
        scanf("%d", arr+i);
    }
    printf(arr,10,sizeof(arr[0],comp));
    for(i = 0; i<10;i++)
    {
        printf("%d",*(arr+i));
    }
}
*/
/*
int main()
{

    int num = 0;
    int count = 0;
    int sum = 0;
    printf("입력: ");
    scanf("%d", &num);
    int num1 = num;

    while (num1)
    {
        num1 = num1 / 10; // 총 몇자리인지 구함
        count++;
    }
    printf("%d \n", count);
    for (int i = count; i < 0; count--) // 하나씩 자름
    {
        num = num / (10 ^ (count-1));        
        sum += num;
        num = num % (10 ^ (count-1)); 
    }
    printf("%d", num);
  
    int num = 0;
    int arr[10];
    for(int i = 0 ; i < 11; i++)
    {
        printf("입력: ");
        scanf("%d", num);
        arr[i] = num;
    }

    for(int j = 0; j < 11; j++)
    {
        printf("",arr[j]);
    }
}
*/