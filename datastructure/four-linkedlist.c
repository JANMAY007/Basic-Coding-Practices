/*
This code is completely user friendly
You can print the list with any gap of nodes
Not only 4 but any number you can apply for gap of nodes 
*/
#include<stdio.h>
#include<stdbool.h>
#include<stdlib.h>

struct Node
{
    int data;
    struct Node *next;
};

struct Node *head = NULL;
struct Node *arr[15];
int arrIndex = 0;

void insert(int data)
{
    if(head==NULL)
    {
        head = (struct Node *)malloc(sizeof(struct Node));
        head->data = data;
        head->next = NULL;
        arr[0] = head;
        arrIndex++;
    }
    else
    {
        struct Node *newNode = (struct Node *)malloc(sizeof(struct Node));
        struct Node *temp = head;
        while(temp->next!=NULL)
        {
            temp = temp->next;
        }
        newNode->data = data;
        newNode->next = NULL;
        temp->next = newNode;
        arr[arrIndex] = newNode;
        arrIndex++;
    }
}

void displayLinkedList()
{
    struct Node *temp = head;
    while(temp!=NULL)
    {
        printf("%d ",temp->data);
        temp = temp->next;
    }
    printf("\n");
}

void multilists(int gap)
{
    for(int i = 0;i<gap;i++)
    {
        for(int j = i; j<arrIndex;j+=gap)
        {
            printf("%d ",arr[j]->data);
        }
        printf("\n");
    }
}

int main()
{
    int option;
    int elem,gap;
    bool flag=true;
    while (flag)
    {
        printf("enter 1 to insert element, 2 to view list, 3 to view list with any gap of nodes and 4 to exit: ");
        scanf("%d",&option);
        switch (option)
        {
        case 1:
            printf("enter the element: ");
            scanf("%d",&elem);
            insert(elem);
            break;
        case 2:
            displayLinkedList();
            break;
        case 3:
            printf("enter the gap of printing: ");
            scanf("%d",&gap);
            multilists(gap);
            break;
        case 4:
            flag=false;
            break;
        default:
            break;
        }
    }
    return 0;
}
