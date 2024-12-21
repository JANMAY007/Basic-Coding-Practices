#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>

struct polynomials
{
    int coeff;
    int pow;
    struct polynomials *next;
};

void create_polynomials(int x, int y, struct polynomials **temp)
{
    struct polynomials *r, *z;
    z = *temp;
    if(z == NULL)
    {
        r =(struct polynomials*)malloc(sizeof(struct polynomials));
        r->coeff = x;
        r->pow = y;
        *temp = r;
        r->next = (struct polynomials*)malloc(sizeof(struct polynomials));
        r = r->next;
        r->next = NULL;
    }
    else
    {
        r->coeff = x;
        r->pow = y;
        r->next = (struct polynomials*)malloc(sizeof(struct polynomials));
        r = r->next;
        r->next = NULL;
    }
}

void polyadd(struct polynomials *poly1, struct polynomials *poly2, struct polynomials *poly)
{
    while(poly1->next && poly2->next)
    {
        if(poly1->pow > poly2->pow)
        {
            poly->pow = poly1->pow;
            poly->coeff = poly1->coeff;
            poly1 = poly1->next;
        }
        else if(poly1->pow < poly2->pow)
        {
            poly->pow = poly2->pow;
            poly->coeff = poly2->coeff;
            poly2 = poly2->next;
        }
        else
        {
            poly->pow = poly1->pow;
            poly->coeff = poly1->coeff+poly2->coeff;
            poly1 = poly1->next;
            poly2 = poly2->next;
        }
        poly->next = (struct polynomials *)malloc(sizeof(struct polynomials));
        poly = poly->next;
        poly->next = NULL;
    }
    while(poly1->next || poly2->next)
    {
        if(poly1->next)
        {
            poly->pow = poly1->pow;
            poly->coeff = poly1->coeff;
            poly1 = poly1->next;
        }
        if(poly2->next)
        {
            poly->pow = poly2->pow;
            poly->coeff = poly2->coeff;
            poly2 = poly2->next;
        }
        poly->next = (struct polynomials *)malloc(sizeof(struct polynomials));
        poly = poly->next;
        poly->next = NULL;
    }
}

void show(struct polynomials *polynomials)
{
    while(polynomials->next != NULL)
    {
        printf("%dx^%d", polynomials->coeff, polynomials->pow);
        polynomials = polynomials->next;
        if(polynomials->next != NULL)
        {
            printf(" + ");
        }
    }
    printf("\n");
}

int main()
{
    struct polynomials *poly1 = NULL, *poly2 = NULL, *poly = NULL;
    poly = (struct polynomials *)malloc(sizeof(struct polynomials));
    /*int coefficient,exponent,option;
    bool flag = true;
    while (flag)
    {
        printf("1 to enter term for first polynomial, 2 to enter term for second polynomial, 3 to view polynomial, 4 to add polynomial and 5 to exit: ");
        scanf("%d",&option);
        switch (option)
        {
        case 1:
            printf("enter the coefficient: ");
            scanf("%d",&coefficient);
            printf("enter the exponent: ");
            scanf("%d",&exponent);
            create_polynomials(coefficient,exponent,&poly1);
            break;
        case 2:
            printf("enter the coefficient: ");
            scanf("%d",&coefficient);
            printf("enter the exponent: ");
            scanf("%d",&exponent);
            create_polynomials(coefficient,exponent,&poly2);
            break;
        case 3:
            show(poly1);
            show(poly2);
            break;
        case 4:
            polyadd(poly1,poly2,poly);
            printf("Final polynomial is:\n");
            show(poly);
            break;
        case 5:
            flag=false;
            break;
        default:
            break;
        }    
    }*/
    create_polynomials(5,2,&poly1);
    create_polynomials(-1,1,&poly1);
    create_polynomials(6,0,&poly1);
    create_polynomials(5,2,&poly2);
    create_polynomials(-1,1,&poly2);
    create_polynomials(6,0,&poly2);
    show(poly1);
    show(poly2);
    polyadd(poly1,poly2,poly);
    show(poly);
    return 0; 
} 