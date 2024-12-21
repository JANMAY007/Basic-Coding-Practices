#include<iostream>
#include<string>
using namespace std;
int main()
{
    char str[]="hello";
    cout<<str<<endl;
    for(int i=0;i<sizeof(str);i++)
    {
        std::cout<<str[i]<<endl;
    }
    return 0;
}
