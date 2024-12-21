#include<stdlib.h>
#include<stdio.h>
#include<stdbool.h>
#define MAX 10

int arr[MAX];
int size = sizeof(arr)/sizeof(arr[0]);

void merge(int arr[], int left, int middle, int right)
{
    int i, j, k;
    int temp1 = middle - left + 1;
    int temp2 =  right - middle;
    int Left[temp1], Right[temp2];
    for (i = 0; i < temp1; i++)
    {
        Left[i] = arr[left + i];
    }
    for (j = 0; j < temp2; j++)
    {
        Right[j] = arr[middle + 1+ j];
    }
    i = 0;
    j = 0;
    k = left;
    while (i < temp1 && j < temp2)
    {
        if (Left[i] <= Right[j])
        {
            arr[k] = Left[i];
            i++;
        }
        else
        {
            arr[k] = Right[j];
            j++;
        }
        k++;
    }
    while (i < temp1)
    {
        arr[k] = Left[i];
        i++;
        k++;
    }
    while (j < temp2)
    {
        arr[k] = Right[j];
        j++;
        k++;
    }
}

void mergeSort(int arr[], int left, int right)
{
    if (left < right)
    {
        int middle = left + (right - left)/2;
        mergeSort(arr, left, middle);
        mergeSort(arr, middle+1, right);
        merge(arr, left, middle, right);
    }
}

void display()
{
    int i;
    for (i=0; i < size; i++)
    {
        printf("%d ", arr[i]);
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
        printf("enter 1 to insert array\n2 to merge sort sort\n3 to display\n4 to exit: ");
        scanf("%d",&option);
        switch (option)
        {
        case 1:
            insert();
            break;
        case 2:
            mergeSort(arr, 0, size-1);
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
