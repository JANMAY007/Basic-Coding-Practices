#include<stdio.h>
#define size 5
int arr[size];

void insertion_sort()
{
	int i, j, x;
	for(i = 0; i < size; i++)
	{
		j = i - 1;
		x = arr[i];
		while((j > -1) && (arr[j] > x))
		{
			arr[j + 1] = arr[j];
			j--;
		}
		arr[j + 1] = x;
	}
}

int main()
{
	int i;
	for(i = 0; i < size; i++)
	{
		printf("enter %d element: ", i + 1);
		scanf("%d", &arr[i]);
	}
	insertion_sort();
	for(i = 0; i < size; i++)
	{
		printf("%d ", arr[i]);
	}
	return 0;
}
