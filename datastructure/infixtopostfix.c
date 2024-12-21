#include<stdio.h>
#include<stdlib.h>
#include<string.h>
struct Stack
{ 
    int top; 
    int size; 
    char* str;
};
struct Stack* create(int n) 
{ 
    struct Stack* s=(struct Stack*)malloc(sizeof(struct Stack)); 
    s->size=n; 
    s->top=-1;
    s->str=(char*)malloc(s->size*sizeof(char));
    return s; 
} 
 
int isfull(struct Stack* s) 
{ 
    return s->top==s->size-1;
} 

int isempty(struct Stack* s) 
{ 
    return s->top==-1; 
} 

void push(struct Stack* s,char x) 
{
    if(isfull(s)) 
        return;
    s->str[++s->top]=x;
}

char pop(struct Stack* s) 
{ 
    if(isempty(s))
    {
        printf("Stack is empty");
        return 0;
    }
    return s->str[s->top--];
}

int peek(struct Stack* s) 
{ 
    if(isempty(s))
    {
        printf("Stack is empty");
        return 0;
    }
    return s->str[s->top]; 
}

int f(char x)
{
    if((x<='Z'&&x>='A')||(x<='a'&&x>='z'))
        return 7;
    switch(x)
    {
    case '+':
    case '-':
        return 1;
    case '*':
    case '/':
        return 3;
    case '^':
        return 6;
    case '(':
        return 9;
    case ')':
        return 0;
    }
}
int g(char x)
{
    if((x<='Z'&&x>='A')||(x<='a'&&x>='z'))
        return 8;
    switch(x)
    {
    case '+':
    case '-':
        return 2;
    case '*':
    case '/':
        return 4;
    case '^':
        return 5;
    case '(':
        return 0;
    }
}
int r(char x)
{
    if((x<='Z'&&x>='A')||(x>='a'&&x<='z'))
        return 1;
    switch(x)
    {
    case '+':
    case '-':
    case '*':
    case '/':
    case '^':
        return -1;
    }
}

int infixtopost(char input[]) 
{ 
    int i,k=-1,rank=0,l=strlen(input);
    char pol[300],temp;
    struct Stack* s=create(strlen(input)); 
    push(s,'(');
    for(i=0;input[i];++i) 
    {
        if(isempty(s))
        return 0;
        while(f(input[i])<g(peek(s)))
        {
            temp=pop(s);
            pol[++k]=temp;
        }
        if(f(input[i])!=g(peek(s)))
            push(s,input[i]);
        else
            pop(s);
    }
    pol[++k]='\0';
    printf("%s",pol);
    return 1;
}

int main()
{
    char infix[300];
    printf("Enter the infix \n");
    scanf("%s",infix);
    int l=strlen(infix);
    infix[l]=')';
    if(!infixtopost(infix))
        printf("Invalid expression\n");
    return 0;
}