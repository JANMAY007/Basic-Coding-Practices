#include<stdio.h>
#include<stdbool.h>
#define MAX 10

int arr[MAX];
int size = sizeof(arr)/sizeof(arr[0]);

void swap(int* a, int* b)
{
    int t = *a;
    *a = *b;
    *b = t;
}

int partition(int low, int high)
{
    int pivot = arr[high];
    int i = low - 1;
    int j;
    for (j = low; j <= high; j++)
    {
        if (arr[j] < pivot)
        {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i+1], &arr[high]);
    return(i+1);
}

void quicksort(int low, int high)
{
    if (low < high)
    {
        int temp = partition(low, high);
        quicksort(low, temp-1);
        quicksort(temp + 1, high);
    }

}

void display()
{
	int i;
    for (i = 0; i < size; i++)
    {
        printf("%d ",arr[i]);
    }
}

void insert()
{
	int i;
    for (i = 0; i < size; i++)
    {
        printf("enter %d element: ",i+1);
        scanf("%d",&arr[i]);
    }
}

int main()
{
    int option;
    bool flag = true;
    while (flag)
    {
        printf("enter 1 to insert array\n2 to quick sort\n3 to display\n4 to exit: ");
        scanf("%d",&option);
        switch (option)
        {
        case 1:
            insert();
            break;
        case 2:
            quicksort(0, size-1);
            break;
        case 3:
            display();
            break;
        case 4:
            flag = false;
            break;
        default:
            break;
        }
    }
    return 0;
}
