#include<stdio.h>
#include<stdbool.h>
#include<stdlib.h>
#include<string.h>
#define size 5

struct node
{ 
    int data;
    struct node* left;
    struct node* right;
};

void Inorder(struct node* node);
void Preorder(struct node* node);
void Postorder(struct node* node);
int search(int inorder[], int begin, int end, int data);
struct node* newnode(int data);
struct node* create(int inorder[], int preorder[], int begin, int end);

struct node* create(int inorder[], int preorder[], int begin, int end) 
{
    static int preindex = 0;
    int inindex;
    if (begin > end)
    {
        return NULL;
    }
    struct node* temp = newnode(preorder[preindex++]);
    if (begin == end)
    {
        return temp;
    }
    inindex = search(inorder, begin, end, temp->data);
    temp->left = create(inorder, preorder, begin, inindex-1);
    temp->right = create(inorder, preorder, inindex+1, end);
    return temp;
}

struct node* newnode(int data)
{
    struct node* node = (struct node*)malloc(sizeof(struct node));
    node->data = data;
    node->left = NULL;
    node->right = NULL;
    return (node);
}

int search(int inorder[], int begin, int end, int data)
{
	int i;
    for (i = begin; i <= end; i++)
    {
        if (inorder[i] == data)
            return i;
    }
}

void Inorder(struct node* temp)
{
    if (temp==NULL)
    {
        return;
    }
    Inorder(temp->left);
    printf("%d ",temp->data);
    Inorder(temp->right);
}

void Preorder(struct node* temp)
{
    if (temp==NULL)
    {
        return;
    }
    printf("%d ",temp->data);
    Inorder(temp->left);
    Inorder(temp->right);
}

void Postorder(struct node* temp)
{
    if (temp==NULL)
    {
        return;
    }
    Inorder(temp->left);
    Inorder(temp->right);
    printf("%d ",temp->data);
}

int main()
{
    int option;
    int inorder[size];
    int preorder[size];
    bool flag = true;
    int len;
    int i;
    struct node* root;
    while (flag)
    {
        printf("enter 1 to insert inorder and preorder and to create BST\n2 to print BST in postorder\n3 to print in preorder\n4 to print in inorder\n5 to exit: ");
        scanf("%d",&option);
        switch (option)
        {
        case 1:
            printf("enter inorder:");
            for (i = 0; i < size; i++)
            {
                printf("%d element: ",i+1);
                scanf("%d",&inorder[i]);
            }
            printf("enter preorder:");
            for (i = 0; i < size; i++)
            {
                printf("%d element: ",i+1);
                scanf("%d",&preorder[i]);
            }
            len = sizeof(inorder)/sizeof(inorder[0]);
            root = create(inorder, preorder, 0, len-1);
            break;
        case 2:
            Postorder(root);
            getchar();
            break;
        case 3:
            Preorder(root);
            getchar();
            break;
        case 4:
            Inorder(root);
            getchar();
            break;
        case 5:
            flag = false;
            break;
        default:
            break;
        }
    }
    return 0;
}
