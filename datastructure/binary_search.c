#include<stdio.h>
#define MAX 10

int binarySearch(int bsarr[], int first, int last, int search) {
  	int middle;
  	if (first > last)
    {
    	return -1;
	}
  	middle = (first + last)/2;
  	if (bsarr[middle] == search)
    {
    	return middle;
	}
  	else if (search > bsarr[middle])  
   	{
   		return binarySearch(bsarr, middle+1, last, search);
	}
  	else
  	{
  	   	return binarySearch(bsarr, first, middle-1, search);
	}
}

int main()
{
	int count, first, last, search, array[MAX], index;
  	for (count = 0; count < MAX; count++)
    {
    	printf("enter %d element: ", count+1);
   		scanf("%d", &array[count]);
	}
  	printf("Enter value to find\n");
  	scanf("%d", &search);
  	first = 0;
  	last = MAX - 1;
  	index = binarySearch(array, first, last, search);
  	if (index == -1)
	{
		printf("%d not found\n", search);
	}
  	else
    {
    	printf("%d is present at location %d.\n", search, index + 1);
	}
  	return 0;
}
