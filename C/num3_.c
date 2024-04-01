#include <stdio.h>
#pragma warning (disable:4996)
int main(void)
{
   int num[10], check[10] = {0};
   int i, j, count;
   printf("10개의 정수를 입력\n");
   for (i = 0; i < 10; i++)
      scanf("%d", &num[i]);
   for (i = 0; i < 10; i++)
   {
      if (check[i])
         continue;
      count = 1;
      for (j = i + 1; j < 10; j++)
      {
         if (num[i] == num[j])
         {
            count++;
            check[j] = 1;
         }
      }
      printf("%d,%d\n",num[i],count);
   }

   return 0;
}