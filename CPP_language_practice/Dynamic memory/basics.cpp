#include<iostream>
using namespace std;
int main()
{
    int *ptr=new int;
    *ptr=4;
    cout<<*ptr<<endl;
    cout<<ptr<<endl;
    return 0;
}
