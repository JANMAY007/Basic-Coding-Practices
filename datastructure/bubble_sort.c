#include<stdio.h>
#include<stdbool.h>
#define size 5
int arr[size];

void bubble_sort()
{
	int i, j, temp;
	bool flag;
	for(i = 0; i < size - 1; i++)
	{
		flag = false;
		for(j = 0; j< size - 1 - i; j++)
		{
			if(arr[j] > arr[j + 1])
			{
				temp = arr[j];
				arr[j] = arr[j + 1];
				arr[j + 1] = temp;
				flag = true;
			}
		}
		if(!flag)
		{
			break;
		}
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
	bubble_sort();
	for(i = 0; i < size; i++)
	{
		printf("%d ", arr[i]);
	}
	return 0;
}
