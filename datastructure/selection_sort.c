#include<stdio.h>
#define size 5
int arr[size];

void selectionsort()
{
	int i, j, k, temp;
 	for(i = 0; i < size - 1; i++)
 	{
 		for(j = k = i; j < size; j++)
 		{
 			if(arr[j] < arr[k])
 			{
 				k = j;
			}
 		}
		temp = arr[i];
		arr[i] = arr[k];
		arr[k] = temp;
	}
}

int main()
{
	int i;
	for(i = 0; i < size; i++)
	{
		printf("enter %d element: ", i+1);
		scanf("%d", &arr[i]);
	}
	selectionsort();
	for(i = 0; i< size; i++)
	{
		printf("%d ", arr[i]);
	}
	return 0;
}
