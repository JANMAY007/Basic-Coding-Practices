#include<stdio.h>
#include<stdbool.h>
#define max 5

struct Dequeue
{
    int rear,front;
    int dearr[max];
};

void insertf(struct Dequeue *deq)
{
    int elem;
    if (deq->rear==-1)
    {
        deq->front=deq->rear=0;
        printf("enter the element: ");
        scanf("%d",&elem);
        deq->dearr[deq->rear]=elem;
    }
    else
    {
        printf("enter the element: ");
        scanf("%d",&elem);
        deq->front=(deq->front-1+max)%max;
        deq->dearr[deq->front]=elem;
    }
}

void insertr(struct Dequeue *deq)
{
    int elem;
    if (deq->rear==-1)
    {
        deq->front=deq->rear=0;
        printf("enter the element: ");
        scanf("%d",&elem);
        deq->dearr[deq->rear]=elem;
    }
    else
    {
        printf("enter the element: ");
        scanf("%d",&elem);
        deq->rear=(deq->rear-1+max)%max;
        deq->dearr[deq->rear]=elem;
    }
}

void dequeuef(struct Dequeue *deq)
{
    int x;
	x=deq->dearr[deq->front];
	if(deq->rear==deq->front)
    {
        deq->front=deq->rear=-1;
    }
	else
	{
        deq->front=(deq->front+1)%max;
    }
}

void dequeuer(struct Dequeue *deq)
{
    int x;
	x=deq->dearr[deq->rear];
	if(deq->rear==deq->front)
    {
        deq->front=deq->rear=-1;
    }
	else
	{
        deq->rear=(deq->rear+1)%max;
    }
}

void display(struct Dequeue *deq)
{
    if(deq->rear==-1)
	{
		printf("queue is empty");
	}
	int i;
	i=deq->front;
	while(i!=deq->rear)
	{
		printf("%d ",deq->dearr[i]);
		i=(i+1)%max;
	}
	printf("\n%d ",deq->dearr[deq->rear]);
    printf("\n");
}

int main()
{
    struct Dequeue deq;
    int option;
    bool flag=true;
    deq.front=deq.rear=-1;
    while (flag)
    {
        printf("1 to insert at front, 2 to insert at rear, 3 to delete from front, 4 to delete from rear, 5 to view queue and 6 to exit: ");
        scanf("%d",&option);
        switch (option)
        {
        case 1:
            insertf(&deq);
            break;
        case 2:
            insertr(&deq);
            break;
        case 3:
            dequeuef(&deq);
            break;
        case 4:
            dequeuer(&deq);
            break;
        case 5:
            display(&deq);
            break;
        case 6:
            flag=false;
            break;
        default:
            printf("enter valid option\n");
            break;
        }
    }
    return 0;
}