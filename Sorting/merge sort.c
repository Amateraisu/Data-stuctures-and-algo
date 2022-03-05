#include <stdio.h>
#include <stdlib.h>



void merges(int* num, int left, int middle, int right)
{
  //find the number of elements in left and right temp arrays 
  int leftnum = middle - left +1;
  int rightnum = right - middle;

  //create temp arrays with the leftnum and rightnum

  int leftarr[leftnum];
  int rightarr[rightnum];

  //copy the data of num into my left and right arrays

  for (int i = 0; i<leftnum ; i++)
    {
      leftarr[i] = num[left + i];
    }
  for (int j = 0 ; j<rightnum;j++)
    {
      rightarr[j] = num[middle+1+j];
    }

  //now to copy the sorted elements of left and right into num;
  int i,j,k;
  i = j = 0;
  k = left;
  while (i<leftnum && j<rightnum)
    {
      if (leftarr[i] <= rightarr[j])
      {
        num[k] = leftarr[i];
        i++;
        k++;
      }
      else 
      {
        num[k] = rightarr[j];
        k++;
        j++;
      }
    }
  //if either left or right still remaining,

  while(i<leftnum)
    {
      num[k] = leftarr[i];
      k++;
      i++;
    }

  while (j<rightnum)
    {
      num[k] = rightarr[j];
      k++;
      j++;
    }
}

void mergeSort(int* num, int left, int right)
{
  if (left<right)
  {
    int middle = (left+right)/2;
    mergeSort(num, left, middle);
    mergeSort(num,middle+1, right);
    merges(num, left, middle, right);
    
  }
}


/* UTILITY FUNCTIONS */
/* Function to print an array */
void printArray(int A[], int size)
{
    int i;
    for (i = 0; i < size; i++)
        printf("%d ", A[i]);
    printf("\n");
}
  
/* Driver code */
int main()
{
    int arr[] = { 12, 11, 13, 5, 6, 7 };
    int arr_size = sizeof(arr) / sizeof(arr[0]);
  
    printf("Given array is \n");
    printArray(arr, arr_size);
  
    mergeSort(arr, 0, arr_size - 1);
  
    printf("\nSorted array is \n");
    printArray(arr, arr_size);
    return 0;
}