#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>

struct linkedlist
{
    int data;
    struct linkedlist *next;
}*first;

void insert()
{
    int elem;
    printf("enter the element:");
    scanf("%d",&elem);
    if (first==NULL)
    {
        first = (struct linkedlist *)malloc(sizeof(struct linkedlist));
        first->data = elem;
        first->next = NULL;
    }
    else
    {
        struct linkedlist *new_node = (struct linkedlist *)malloc(sizeof(struct linkedlist));
        struct linkedlist *temp = first;
        new_node->data = elem;
        new_node->next = NULL;
        while (temp->next!=NULL)
        {
            temp=temp->next;
        }
        temp->next = new_node;
    }
}

void display(struct linkedlist *dis)
{
    while (dis!=NULL)
    {
        printf("%d ",dis->data);
        dis=dis->next;
    }
    printf("\n");
}

void rdisplay(struct linkedlist *rev)
{
    if (rev==NULL)
    {
        return;
    }
    else
    {
        rdisplay(rev->next);
        printf("%d ",rev->data);
    }
    printf("\n");
}

int main()
{
    int option;
    bool flag=true;
    while (flag)
    {
        printf("enter 1 to insert element, 2 to display list, 3 to reverse list and 4 to exit: ");
        scanf("%d",&option);
        switch (option)
        {
        case 1:
            insert();
            break;
        case 2:
            display(first);
            break;
        case 3:
            rdisplay(first);
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