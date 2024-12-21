#include<stdio.h>
#include<stdbool.h>
#include<stdlib.h>

struct node
{
    int data;
    struct node* next;
}*head;

void create()
{
    int elem;
    printf("enter the element:");
    scanf("%d",&elem);
    if (head==NULL)
    {
        head = (struct node *)malloc(sizeof(struct node));
        head->data = elem;
        head->next = NULL;
    }
    else
    {
        struct node *new_node = (struct node *)malloc(sizeof(struct node));
        struct node *temp = head;
        new_node->data = elem;
        new_node->next = NULL;
        while (temp->next!=NULL)
        {
            temp=temp->next;
        }
        temp->next = new_node;
    }
}

void display()
{
    struct node *temp;
    static int flag=0;
    while (temp!=head || flag==0)
    {
        flag=1;
        printf("%d",temp->data);
        temp=temp->next;
        display();
    }
    flag=0;
}

int length()
{
    int count=0;
    struct node *temp;
    temp=head;
    do
    {
        temp=temp->next;
        count++;
    } while (temp!=head);
    return count;
}

void insert()
{
    struct node *temp,*p;
    int i;
    int elem,pos;
    p=head;
    printf("enter the position of insertion: ");
    scanf("%d",&pos);
    if (pos==0 || pos>length())
    {
        printf("invalid position!!");
        return;
    }
    if (pos==0)
    {
        temp=(struct node *)malloc(sizeof(struct node));
        printf("enter the element: ");
        scanf("%d",&elem);
        if (head==NULL)
        {
            head=temp;
            head->next=head;
        }
        else
        {
            while (p->next!=head)
            {
                p=p->next;
            }
            p->next=temp;
            temp->next=head;
            head=temp;
        }
    }
    else
    {
        for (int i = 0; i < pos-1; i++)
        {
            p=p->next;
        }
        temp=(struct node *)malloc(sizeof(struct node));
        printf("enter the element: ");
        scanf("%d",&elem);
        temp->data=elem;
        temp->next=p->next;
        p->next=temp;
    }
}