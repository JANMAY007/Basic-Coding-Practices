#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>

void createheap(int arr[], int size, int i)
{
    int largest=i;
    int lchild=2*i+1;
    int rchild=2*i+2;
    if (lchild<size && arr[lchild]>arr[largest])
    {
        largest=lchild;
    }
    if (rchild<size && arr[rchild]>arr[largest])
    {
        largest=rchild;
    }
    if (largest!=i)
    {
        int temp;
        temp=arr[i];
        arr[i]=arr[largest];
        arr[largest]=temp;
        createheap(arr, size, largest);
    }
}

void heapsort(int arr[], int size)
{
	int i;
    for (i = size/2 - 1; i >= 0; i--)
    {
        createheap(arr,size,i);
    }
    for (i = size -1; i > 0; i--)
    {
        int temp;
        temp=arr[0];
        arr[0]=arr[i];
        arr[i]=temp;
        createheap(arr,i,0);
    }
}

void display(int arr[], int size)
{
	int i;
    for (i = 0; i < size; i++)
    {
        printf("%d ",arr[i]);
    }
    printf("\n");
}

int main()
{
    int option;
    bool flag=true;
    int arr[10];
    int i;
    int size = sizeof(arr)/sizeof(arr[0]);
    while (flag)
    {
        printf("enter 1 to insert new array\n2 to perform heap sort\n3 to display heap\n4 to exit: ");
        scanf("%d",&option);
        switch (option)
        {
        case 1:
            for (i = 0; i < size; i++)
            {
            	printf("enter %d element: ", i+1);
                scanf("%d",&arr[i]);
            }
            break;
        case 2:
            heapsort(arr,size);
            break;
        case 3:
            display(arr, size);
            break;
        case 4:
            flag=false;
            break;
        default:
            break;
        }
    }
    
}
