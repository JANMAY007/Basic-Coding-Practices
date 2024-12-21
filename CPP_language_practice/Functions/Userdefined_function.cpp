#include<iostream>
using namespace std;
int max(int num1,int num2);
int main()
{
    int a,b;
    cout<<"enter two numbers: ";
    cin>>a>>b;
    int res;
    res=max(a,b);
    cout<<"maximum of both is "<<res;
    return 0;
}
int max(int num1,int num2)
{
    int result;
    if (num1>num2)
    {
        result=num1;
    }
    else
    {
        result=num2;
    }
    return result;
}