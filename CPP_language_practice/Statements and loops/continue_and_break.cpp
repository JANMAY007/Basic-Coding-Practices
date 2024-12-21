#include<iostream>
using namespace std;
int main()
{
    for(int num=0;num<=6;num++)
    {
        if(num==3)
            continue;
        else if (num==5)
            break;
        cout<<num<<endl;
    }
    return 0;
}