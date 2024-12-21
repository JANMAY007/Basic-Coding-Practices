#include<stdio.h>
#include<stdbool.h>
#include<stdlib.h>

struct Node
{
    int data;
    struct Node *next;
    struct Node *prev;
}*any;

void insertEnd(struct Node** start, int value)
{
    if (*start == NULL)
    {
        struct Node* new_node = (struct Node *)malloc(sizeof(struct Node));
        new_node->data = value;
        new_node->next = new_node->prev = new_node;
        *start = new_node;
        return;
    }
    struct Node *last = (*start)->prev;
    struct Node *new_node = (struct Node *)malloc(sizeof(struct Node));
    new_node->data = value;
    new_node->next = *start;
    (*start)->prev = new_node;
    new_node->prev = last;
    last->next = new_node;
    printf("\n");
}

void insertBegin(struct Node** start, int value)
{
    struct Node *last = (*start)->prev;
    struct Node *new_node = (struct Node *)malloc(sizeof(struct Node));
    new_node->data = value;
    new_node->next = *start;
    new_node->prev = last;
    last->next = (*start)->prev = new_node;
    *start = new_node;
    printf("\n");
}

void insertAfter(struct Node** start, int value1, int value2)
{
    struct Node *new_node = (struct Node *)malloc(sizeof(struct Node)); 
    new_node->data = value1;
    struct Node *temp = *start;
    while (temp->data != value2)
    {
        temp = temp->next;
    }
    struct Node *next = temp->next;
    temp->next = new_node;
    new_node->prev = temp;
    new_node->next = next;
    next->prev = new_node;
    printf("\n");
} 

void insertat(struct Node** start, int pos, int value)
{
    struct Node *new_node = (struct Node *)malloc(sizeof(struct Node));
    struct Node *temp;
    int count=0;
    temp=*start;
    while (temp->next!=*start)
    {
        temp=temp->next;
        count++;
    }
    if (temp==NULL || count<pos)
    {
        return;
    }
    else
    {
        new_node->data=value;
        for (int i = 0; i < pos-1; i++)
        {
            temp=temp->next;
        }
        new_node->next=temp->next;
        (temp->next)->prev=new_node;
        temp->next=new_node;
        new_node->prev=temp;
    }
}

void display(struct Node* start) 
{ 
    struct Node *temp = start;
    printf("original list\n");
    while (temp->next != start)
    {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("%d\n", temp->data);
    printf("reverse list\n");
    struct Node *last = start->prev;
    temp = last;
    while (temp->prev != last)
    { 
        printf("%d ", temp->data);
        temp = temp->prev;
    }
    printf("%d ", temp->data);
    printf("\n");
}

void anydisplay(struct Node* start, int value)
{
    any = start;
    printf("element at %d position is",value);
    for (int i = 0; i < value; i++)
    {
        any = any->next;
    }
    printf("%d",any->data);
    printf("\n");
}

void previous()
{
    any = any->prev;
    printf("%d",any->data);
    printf("\n");
}

void next()
{
    any = any->next;
    printf("%d",any->data);
    printf("\n");
}

int main()
{
    struct Node* start = NULL;
    int option;
    int begin,end,elem,ref,pos,any,atpos;
    bool flag=true;
    printf("enter first element: ");
    scanf("%d",&begin);
    insertEnd(&start,begin);
    while (flag)
    {
        printf("enter 1 to insert at begin\n2 to insert at end\n3 to insert after some element\n4 to insert at some position\n5 to display full list\n6 to print any one element\n7 to print previous\n8 to print next\n9 to print first\n10 to exit:\n");
        scanf("%d",&option);
        switch (option)
        {
        case 1:
            printf("enter element: ");
            scanf("%d",&begin);
            insertBegin(&start,begin);
            break;
        case 2:
            printf("enter element: ");
            scanf("%d",&end);
            insertEnd(&start,end);
            break;
        case 3:
            printf("enter element: ");
            scanf("%d",&elem);
            printf("enter reference element: ");
            scanf("%d",&ref);
            insertAfter(&start,elem,ref);
            break;
        case 4:
            printf("enter position: ");
            scanf("%d",&pos);
            printf("enter the element: ");
            scanf("%d",&atpos);
            insertat(&start,pos,atpos);
            break;
        case 5:
            display(start);
            break;
        case 6:
            printf("enter the position of the song: ");
            scanf("%d",&any);
            anydisplay(start,any);
            break;
        case 7:
            previous();
            break;
        case 8:
            next();
            break;
        case 9:
            printf("%d",start);
            break;
        case 10:
            flag=false;
            break;
        default:
            break;
        }
    }
    return 0;
} 