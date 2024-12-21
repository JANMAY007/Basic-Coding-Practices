#include<iostream>
using namespace std;
void swap(int& a,int& b) // through reference variable
{
    int temp;
    temp=a;
    a=b;
    b=temp;
    return;
}
int main()
{
    int num1,num2;
    cout<<"enter two numbers: ";
    cin>>num1>>num2;
    swap(num1,num2);
    cout<<"after swaping: "<<num1<<" "<<num2;
    return 0;
}