#include<iostream>
using namespace std;
int main()
{
    int num;
    cout<<"enter a number: ";
    cin>>num;
    if(num%2==0)
    {
        goto print;
    }
    else
    {
        cout<<"you entered a odd number";
    }
    print:
        cout<<"you entered a even number";
        return 0;
}