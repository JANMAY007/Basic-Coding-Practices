#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
#include<string.h>
# define size 25

struct phone_book
{
    struct phone_book *lchild;
    int phone;
    char name[size];
    struct phone_book *rchild;
}*root=NULL;

void Insert(int key)
{
    struct phone_book *t=root;
    struct phone_book *r=NULL,*p;
    if(root==NULL)
    {
        p=(struct phone_book *)malloc(sizeof(struct phone_book));
        p->phone=key;
        p->lchild=p->rchild=NULL;
        root=p;
        return;
    }
    while(t!=NULL)
    {
        r=t;
        if(key<t->phone)
        {
            t=t->lchild;
        }
        else if(key>t->phone)
        {
            t=t->rchild;
        }
        else
        {
            return;
        }
    }
    p=(struct phone_book *)malloc(sizeof(struct phone_book));
    p->phone=key;
    p->lchild=p->rchild=NULL;
    if(key<r->phone) 
    {
        r->lchild=p;
    }
    else 
    {
        r->rchild=p;
    }
}

void ascending(struct phone_book *p)
{
    if(p)
    {
        ascending(p->lchild);
        printf("%s %d",p->name,p->phone);
        printf("\n");
        ascending(p->rchild);
    }
}

void descending(struct phone_book *p)
{
    if(p)
    {
        descending(p->rchild);
        printf("%s %d",p->name,p->phone);
        printf("\n");
        descending(p->lchild);
    }
}

struct phone_book * Searchnumber(int key)
{
    struct phone_book *t=root;
    while(t!=NULL)
    {
        if(key==t->phone)
        {
            return t;
        }
        else if(key<t->phone)
        {
            t=t->lchild;
        }
        else
        {
            t=t->rchild;
        }
    }
    return NULL;
}

struct phone_book * Searchname(char *sername)
{
    struct phone_book *t=root;
    while(t!=NULL)
    {
        if(strcmp(sername,t->name)==0)
        {
            return t;
        }
        else if(strcmp(sername,t->name)<0)
        {
            t=t->lchild;
        }
        else
        {
            t=t->rchild;
        }
    }
    return NULL;
}

struct phone_book *RInsert(struct phone_book *p,int key, char *names)
{
    struct phone_book *t=NULL;
    if(p==NULL)
    {
        t=(struct phone_book *)malloc(sizeof(struct phone_book));
        t->phone=key;
        strcpy(t->name,names);
        t->lchild=t->rchild=NULL;
        return t;
    }
    if(key < p->phone)
    {
        p->lchild=RInsert(p->lchild,key,names);
    }
    else if(key > p->phone)
    {
        p->rchild=RInsert(p->rchild,key,names);
    }
    return p;
}

int Height(struct phone_book *p)
{
    int x,y;
    if(p==NULL)
    {
        return 0;
    }
    x=Height(p->lchild);
    y=Height(p->rchild);
    return x>y?x+1:y+1;
}

struct phone_book *InPre(struct phone_book *p)
{
    while(p && p->rchild!=NULL)
    {
        p=p->rchild;
    }
    return p;
}

struct phone_book *InSucc(struct phone_book *p)
{
    while(p && p->lchild!=NULL)
    {
        p=p->lchild;
    }
    return p;
}

struct phone_book *Deletenumber(struct phone_book *p,int key,char *delname)
{
    struct phone_book *q;
    if(p==NULL)
    {
        return NULL;
    }
    if(p->lchild==NULL && p->rchild==NULL)
    {
        if(p==root)
        {
            root=NULL;
        }
        free(p);
        return NULL;
    }
    if(key < p->phone)
    {
        p->lchild=Deletenumber(p->lchild,key,delname);
    }
    else if(key > p->phone)
    {
        p->rchild=Deletenumber(p->rchild,key,delname);
    }
    else
    {
        if(Height(p->lchild)>Height(p->rchild))
        {
            q=InPre(p->lchild);
            p->phone=q->phone;
            strcpy(p->name,q->name);
            p->lchild=Deletenumber(p->lchild,q->phone,q->name);
        }
        else
        {
            q=InSucc(p->rchild);
            p->phone=q->phone;
            strcpy(p->name,q->name);
            p->rchild=Deletenumber(p->rchild,q->phone,q->name);
        }
    }
    return p;
}

struct phone_book *Deletename(struct phone_book *p,int key,char *delname)
{
    struct phone_book *q;
    if(p==NULL)
    {
        return NULL;
    }
    if(p->lchild==NULL && p->rchild==NULL)
    {
        if(p==root)
        {
            root=NULL;
        }
        free(p);
        return NULL;
    }
    if(strcmp(delname,q->name)<0)
    {
        p->lchild=Deletename(p->lchild,key,delname);
    }
    else if(strcmp(delname,q->name)>0)
    {
        p->rchild=Deletename(p->rchild,key,delname);
    }
    else
    {
        if(Height(p->lchild)>Height(p->rchild))
        {
            q=InPre(p->lchild);
            p->phone=q->phone;
            strcpy(p->name,q->name);
            p->lchild=Deletename(p->lchild,q->phone,q->name);
        }
        else
        {
            q=InSucc(p->rchild);
            p->phone=q->phone;
            strcpy(p->name,q->name);
            p->rchild=Deletename(p->rchild,q->phone,q->name);
        }
    }
    return p;
}

int main()
{
    struct phone_book *temp,*searchname,*searchnumber;
    long long int num;
    long long int elem,del,ser;
    char name[size], elemname[size], delname[size], sername[size];
    int option;
    bool flag = true;
    printf("enter phone number: ");
    scanf("%lld",&num);
    printf("enter their name: ");
    scanf("%s", &name);
    root=RInsert(root,num,name);
    while (flag)
    {
        printf("enter 1 to insert, 2 to delete by number, 3 to delete by name, 4 to search by nummber, 5 to search by name, 6 to print in ascending order, 7 to print in descending orde and 8 to exit: ");
        scanf("%d",&option);
        switch (option)
        {
        case 1:
            printf("enter the number: ");
            scanf("%d",&elem);
            printf("enter their name: ");
            scanf("%s", &elemname);
            RInsert(root,elem,elemname);
            break;
        case 2:
            printf("enter the element to delete: ");
            scanf("%d",&del);
            searchnumber=Searchnumber(del);
            Deletenumber(root,del,searchnumber->name);
            break;
        case 3:
            printf("enter the element to delete: ");
            scanf("%s", &delname);
            searchname=Searchname(delname);
            Deletenumber(root,searchname->phone,searchname->name);
            break;
        case 4:
            printf("enter the element: ");
            scanf("%d",&ser);
            temp = Searchnumber(ser);
            if(temp!=NULL)
            {
                printf("element %d is found\n",temp->phone);
            }
            else
            {
                printf("element is not found\n");
            }
            break;
        case 5:
            printf("enter the name: ");
            scanf("%s", &sername);
            temp = Searchname(sername);
            if (temp!=NULL)
            {
                printf("element %d is found\n",temp->name);
            }
            else
            {
                printf("element is not found\n");
            }
            break;
        case 6:
            ascending(root);
            break;
        case 7:
            descending(root);
            break;
        case 8:
            flag = false;
            break;
        default:
            break;
        }
    }
    return 0;
}