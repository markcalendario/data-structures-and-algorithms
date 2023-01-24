#include <stdio.h>

int main()
{
  int array[] = {5, 8, 1, 43, -4, 87, 2};
  int isOk = 0;
  while (!isOk)
  {
    isOk = 1;
    for (int i = 0; i < sizeof(array) / sizeof(array[0]) - 1; i++)
    {
      if (array[i] > array[i + 1])
      {
        isOk = 0;
        int temp = array[i];
        array[i] = array[i + 1];
        array[i + 1] = temp;
      }
    }
  }

  for (int i = 0; i < sizeof(array) / sizeof(array[0]); i++)
  {
    printf("%d ", array[i]);
  }

  return 0;
}