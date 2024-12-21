#include<iostream>
#include<string>
using namespace std;
int main()
{
    char name[20];
    char *p;
    p=name;
    cout<<"enter your name: ";
    cin>>name;
    while(*p!='\0')
    {
        cout<<*p;
        p++;
    }
    return 0;
}
