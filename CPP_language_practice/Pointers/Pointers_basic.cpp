#include<iostream>
using namespace std;
int main()
{
    int var=20;
    int *ip;
    ip=&var;
    cout<<var<<endl;
    cout<<ip<<endl;
    cout<<*ip;
    return 0;
}