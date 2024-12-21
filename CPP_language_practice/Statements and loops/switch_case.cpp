#include<iostream>
using namespace std;
int main()
{
    char o;
    cout<<"enter any operator(+,-,*,/): ";
    cin>>o;
    float num1,num2;
    cout<<"enter two operands: ";
    cin>>num1>>num2;
    switch (o)
    {
    case '+':
        cout<<num1<<"+"<<num2<<"="<<num1+num2;
        break;
    case '-':
        cout<<num1<<"-"<<num2<<"="<<num1-num2;
        break;
    case '*':
        cout<<num1<<"*"<<num2<<"="<<num1*num2;
        break;
    case '/':
        cout<<num1<<"/"<<num2<<"="<<num1/num2;
        break;
    default:
        break;
    }
    return 0;
}