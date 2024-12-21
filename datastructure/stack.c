#include<stdio.h>
#include<stdbool.h>
#include<stdlib.h>

struct stack
{
    int size;
    int top;
    int *s;
};

void push(struct stack *st);
void pop(struct stack *st);
void peep(struct stack st);
void display(struct stack *st);

int main()
{
    struct stack st;
    printf("enter size of stack: ");
    scanf("%d",&st.size);
    st.s=(int *)malloc(st.size*sizeof(int));
    st.top=-1;
    int option;
    bool flag=true;
    while(flag)
    {
        int a;
        printf("enter 1 to push, 2 to pop, 3 to view stack, 4 to view element at any position and 5 to exit: ");
        scanf("%d",&option);
        switch(option)
        {
        case 1:
            {
                push(&st);
                break;
            }
        case 2:
            {
                pop(&st);
                break;
            }
        case 3:
            {
                display(&st);
                break;
            }
        case 4:
            {
                peep(st);
                break;
            }
        case 5:
            {
                flag=false;
            }
        default:
            {
                break;
            }
        }
    }
    return 0;
}

void display(struct stack *st)
{
    for(int i=st->top;i>=0;i--)
    {
        printf("%d ",st->s[i]);
    }
    printf("\n");
}

void push(struct stack *st)
{
    int push_elem;
    printf("enter the element: ");
    scanf("%d",&push_elem);
    if(st->top==st->size-1)
    {
        printf("\nstack overflow\n");
    }
    else
    {
        st->top++;
        st->s[st->top]=push_elem;
    }
}

void pop(struct stack *st)
{
    if(st->top==-1)
    {
        printf("\nstack underflow\n");
    }
    else
    {
        st->top--;
    }
}

void peep(struct stack st)
{
    int pos;
    printf("enter the position: ");
    scanf("%d",&pos);
    if(st.top-pos+1<0)
    {
        printf("\ninvalid position\n");
    }
    else
    {
        printf("the element at %d index is %d\n",pos,st.s[st.top-pos+1]);
    }
}
