#include<stdio.h>
#include<stdbool.h>

struct simplequeue
{    
    int sarr[10],rear,count;   
};

void enqueue(struct simplequeue *sq)
{
    int elem;
    if (sq->rear==-1)
    {
        sq->rear=0;
    }
    else
    {
        ++sq->rear;
    }
    if (sq->rear==10)
    {
        printf("queue overflow\n");
    }
    else
    {
        printf("enter the element: ");
        scanf("%d",&elem);
        printf("\n");
        sq->sarr[sq->rear]=elem;
        sq->count++;
    }
}

void dequeue(struct simplequeue *sq)
{
    printf("%d is deleted\n",sq->sarr[0]);
    for (int i = 0; i < sq->count; i++)
    {
        sq->sarr[i]=sq->sarr[i+1];
    }
    sq->count--;
}

void display(struct simplequeue *sq)
{
    printf("the queue is\n");
    for (int i = 0; i < sq->count; i++)
    {
        printf("%d ",sq->sarr[i]);
    }
    printf("\n");
}

void peep(struct simplequeue *sq)
{
    int view;
    printf("enter the position of element in queue: ");
    scanf("%d",&view);
    if (view>=0 && view<sq->count)
    {
        printf("%d\n",sq->sarr[view-1]);
    }
    else
    {
        printf("no element");
    }
}

int main()
{
    struct simplequeue sq;
    int option;
    bool flag=true;
    sq.count=0;
    sq.rear=-1;
    while (flag)
    {
        printf("1 to enqueue, 2 to delete, 3 to view queue, 4 to see element of queue and 5 to exit.");
        scanf("%d",&option);
        printf("\n");
        switch (option)
        {
        case 1:
        {
            enqueue(&sq);
            break;
        }
        case 2:
        {
            dequeue(&sq);
            break;
        }
        case 3:
        {
            display(&sq);
            break;
        }
        case 4:
        {
            peep(&sq);
            break;
        }
        case 5:
        {
            flag=false;
        }
        default:
            break;
        }
    }
    return 0;
}