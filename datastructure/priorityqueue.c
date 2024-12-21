#include<stdio.h>
#include<stdbool.h>
#define max 5

struct priorityqueue
{
    int front;
    int rear;
    int pqarr[max];
    int count;
};

void insert(struct priorityqueue *pq)
{
    if (pq->rear==max-1)
    {
        printf("queue is full");
    }
    else
    {
        int elem;
        printf("enter the element to insert: ");
        scanf("%d",&elem);
        pq->rear++;
        pq->front++;
        pq->pqarr[pq->rear]=elem;
        pq->count++;
    }
    printf("\n");
}

void delete(struct priorityqueue *pq)
{
    int i,k;
    if ((pq->front==-1) && (pq->rear==-1))
    {
        printf("queue is empty");
    }
    else
    {
        int smallest=pq->pqarr[0];
        for (i = 0; i <= pq->count; i++)
        {
            if (smallest > pq->pqarr[i])
            {
                smallest = pq->pqarr[i];
                k=i;
            }
        }
        for (i = 0; i <= pq->rear; i++)
        {
            if (smallest == pq->pqarr[i])
            {
                for (; i < pq->rear; i++)
                {
                    pq->pqarr[i] = pq->pqarr[i + 1];
                }
                pq->pqarr[i] = -99;
                pq->rear--;
                if (pq->rear == -1) 
                    pq->front = -1;
            }
        }
        printf("%d is deleted",smallest);
        pq->front--;
    }
    printf("\n");
}

void display(struct priorityqueue *pq)
{
    for (int i = 0; i <= pq->rear; i++)
    {
        printf("%d ", pq->pqarr[i]);
    }
    printf("\n");
}

int main()
{
    struct priorityqueue pq;
    pq.front=pq.rear=-1;
    bool flag=true;
    int option;
    pq.count=-1;
    while (flag)
    {
        printf("enter 1 to insert element, 2 to delete element, 3 to view queue and 4 to exit: ");
        scanf("%d",&option);
        switch (option)
        {
        case 1:
            insert(&pq);
            break;
        case 2:
            delete(&pq);
            break;
        case 3:
            display(&pq);
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