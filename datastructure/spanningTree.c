#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>

#define MAX 10
#define temp 0
#define perm 1
#define infinity 9999
#define nil -1

struct Graph
{
    int edge;
    int vertices;
};

int n;
int adj[MAX][MAX];
int pre[MAX];
int status[MAX];
int length[MAX];

int minimum()
{
    int i;
    int min = infinity;
    int k = -1;
    for(i=0; i<n; i++)
    {
        if(status[i] == temp && length[i] < min)
        {
            min = length[i];
            k = i;
        }
    }
    return k;
}

void generatetree(int var, struct Graph tree[MAX])
{
    int current,i;
    int count = 0;
    for(i=0; i<n; i++)
    {
        pre[i] = nil;
        length[i] = infinity;
        status[i] = temp;
    }
    length[var] = 0;
    while(1)
    {
        current = minimum();
        if(current == nil)
        {
            if(count == n-1)
            {
                return;
            }
            else
            {
                printf("Not possible");
                printf("\n");
                exit(1);
            }
        }
        status[current] = perm;
        if(current != var)
        {
            count++;
            tree[count].edge = pre[current];
            tree[count].vertices = current;
        }
        for(i=0; i<n; i++)
        {
            if(adj[current][i] > 0 && status[i] == temp)
            {
                if(adj[current][i] < length[i])
                {
                    pre[i] = current;
                    length[i] = adj[current][i];
                }
            }
        }
    }
}

void makegraph()
{
    int i,max_edges,origin,destin,weight;
    printf("Enter number of vertices : ");
    scanf("%d",&n);
    max_edges = n*(n-1)/2;
    printf("enter 0 in both edge to exit");
    printf("\n");
    for(i=1; i<=max_edges; i++)
    {
        printf("Enter edge %d: ",i);
        scanf("%d %d",&origin,&destin);
        if((origin == 0) && (destin == 0))
        {
            break;
        }
        printf("Enter weight for this edge : ");
        scanf("%d",&weight);
        if( origin >= n || destin >= n || origin < 0 || destin < 0)
        {
            printf("Invalid edge!");
            i--;
        }
        else
        {
            adj[origin][destin] = weight;
            adj[destin][origin] = weight;
        }
    }
}

int main()
{
    int weight_tree = 0;
    int i, root;
    struct Graph tree[MAX];
    int option;
    bool flag = true;
    while (flag)
    {
        printf("enter 1 to create graph\n2 to generate tree\n3 to exit: ");
        scanf("%d",&option);
        switch (option)
        {
        case 1:
            makegraph();
            break;
        case 2:
            printf("Enter root vertex : ");
            scanf("%d",&root);
            generatetree(root, tree);
            printf("Edges to be included in spanning tree are : \n");
            for(i=1; i<=n-1; i++)
            {
                printf("%d->%d\n",tree[i].edge,tree[i].vertices);
                weight_tree += adj[tree[i].edge][tree[i].vertices];
            }
            printf("Weight of spanning tree is : %d", weight_tree);
            printf("\n");
            break;
        case 3:
            flag = false;
            break;
        default:
            break;
        }
    }
    return 0;
}

/*#define NIL -1
#define MAX 100

struct edge
{
    int x;
    int y;
    int weight;
    struct edge *next;
}*front = NULL;

void generatetree(struct edge tree[]);
void insert_queue(int i, int j, int weight);
struct edge *delete_queue();
int isEmpty();
void graph();

int vertices;

int main()
{
    int count;
    struct edge tree[MAX];
    int tree_weight = 0;
    graph();
    generatetree(tree);
    printf("Edges in MST:\n");
    for(count = 1; count <= vertices - 1; count++)
    {
        printf("%d->", tree[count].x);
        printf("%d\n", tree[count].y);
        tree_weight = tree_weight + tree[count].weight;
    }
    printf("Total Weight of this Minimum Spanning Tree:\t%d\n", tree_weight);
    return 0;
}

void generatetree(struct edge tree[])
{
    struct edge *temp;
    int y1, y2, root_y1, root_y2;
    int parent[MAX];
    int i, count = 0;
    for(i = 0; i < vertices; i++)
    {
        parent[i] = NIL;
    }
    while(!isEmpty( ) && count < vertices - 1)
    {
        temp = delete_queue();
        y1 = temp->x;
        y2 = temp->y;
        while(y1 != NIL)
        {
            root_y1 = y1;
            y1 = parent[y1];
        }
        while(y2 != NIL)
        {
            root_y2 = y2;
            y2 = parent[y2];
        }
        if(root_y1 != root_y2)
        {
            count++;
            tree[count].x = temp->x;
            tree[count].y = temp->y;
            tree[count].weight = temp->weight;
            parent[root_y2] = root_y1;
        }
    }
    if(count < vertices - 1)
    {
        printf("graph is not possible\n");
        exit(1);
    }
}

void insert_queue(int i, int j, int weight)
{
    struct edge *temp, *q;
    temp = (struct edge *)malloc(sizeof(struct edge));
    temp->x = i;
    temp->y = j;
    temp->weight = weight;
    if(front == NULL || temp->weight < front->weight)
    {
        temp->next = front;
        front = temp;
    }
    else
    {
        q = front;
        while(q->next != NULL && q->next->weight <= temp->weight)
        {
            q = q->next;
        }
        temp->next = q->next;
        q->next = temp;
        if(q->next == NULL)
        {
            temp->next = NULL;
        }
    }
}

struct edge *delete_queue()
{
    struct edge *temp;
    temp = front;
    front = front->next;
    return temp;
}

int isEmpty()
{
    if(front == NULL)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

void graph()
{
    int count, weight, maximum_edges, origin_vertex, destination_vertex;
    printf("Enter Total Number of Vertices:");
    scanf("%d", &vertices);
    printf("enter edge -1 -1 to exit\n");
    maximum_edges = vertices * (vertices - 1)/2;
    for(count = 0; count < maximum_edges; count++)
    {
        printf("Enter Edge [%d] Co-ordinates\n", count + 1);
        printf("Enter Origin Point:\t");
        scanf("%d", &origin_vertex);
        printf("Enter Destination Point:\t");
        scanf("%d", &destination_vertex);
        if((origin_vertex == -1) && (destination_vertex == -1))
        {
            break;
        }
        printf("Enter Weight for this Edge:\n");
        scanf("%d", &weight);
        if(origin_vertex >= vertices || destination_vertex >= vertices || origin_vertex < 0 || destination_vertex < 0)
        {
            printf("Entered Edge Co - ordinates is Invalid\n");
            count--;
        }
        else
        {
            insert_queue(origin_vertex, destination_vertex, weight);
        }
    }
}
*/