#include <stdio.h>

int main()
{
  int array[] = {5, 7, 123, 76, 23, 60, -3, 9};

  int isOk = 0;
  while (!isOk)
  {
    isOk = 1;

    for (int i = 0; i < sizeof(array) / sizeof(array[0]); i++)
    {
      if (array[i] > array[i + 1])
      {
        isOk = 0;
        int temp = array[i];
        array[i] = array[i + 1];
        array[i + 1] = temp;
        break;
      }
    }
  }

  for (int i = 0; i < sizeof(array) / sizeof(array[0]); i++)
  {
    printf("%d ", array[i]);
  }

  return 0;
}