#include<iostream>
#include<string>
using namespace std;
int main()
{
    char m[]="hello";
    string str;
    int i;
    for(i=0;i<sizeof(m);i++)
    {
        str[i]=m[i];
        cout<<str[i];
    }
    return 0;
}
