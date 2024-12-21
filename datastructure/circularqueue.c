#include<stdio.h>
#include<stdbool.h>

#define maxsize 3

struct circularqueue
{
    int front;
    int rear;
    int carr[maxsize];
};

void enqueue(struct circularqueue *cq)
{
    int elem;
    if ((cq->rear+1)%maxsize==cq->front)
    {
        printf("queue is full");
    }
    else
    {
        printf("enter the element: ");
        scanf("%d",&elem);
        cq->rear=(cq->rear+1)%maxsize;
        cq->carr[cq->rear]=elem;
    }
    printf("\n");
}

void dequeue(struct circularqueue *cq)
{
    int index=-1;
    if (cq->front==cq->rear)
    {
        printf("queue is empty");
    }
    else
    {
        cq->front=(cq->front+1)%maxsize;
        printf("%d is deleted",cq->carr[cq->front]);
        index=cq->carr[cq->front];
    }
    printf("\n");
}

void display(struct circularqueue *cq)
{
    int i=cq->front+1;
    while (i!=(cq->rear+1)%maxsize)
    {
        printf("%d ",cq->carr[i]);
        i=(i+1)%maxsize;
    }
    printf("\n");
}

int main()
{
    struct circularqueue cq;
    cq.front=0;
    cq.rear=0;
    int option;
    bool flag=true;
    while (flag)
    {
        printf("enter 1 to enqueue, 2 to dequeue, 3 to view and 4 to exit: ");
        scanf("%d",&option);
        switch (option)
        {
        case 1:
        {
            enqueue(&cq);
            break;
        }
        case 2:
        {
            dequeue(&cq);
            break;
        }
        case 3:
        {
            display(&cq);
            break;
        }
        case 4:
        {
            flag=false;
        }
        default:
            break;
        }
    }
    return 0;
}