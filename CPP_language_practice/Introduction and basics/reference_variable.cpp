#include<iostream>
using namespace std;
int main()
{
    int x=10;
    int& ref=x;
    ref=20;
    cout<<"x="<<x<<endl;
    x=30;
    cout<<"Reference="<<ref;
    return 0;
}