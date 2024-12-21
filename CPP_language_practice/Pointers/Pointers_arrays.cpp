#include<iostream>
using namespace std;
const int MAX=3;
int main()
{
    int var[MAX]={100,200,300};
    int *ptr;
    ptr=var;
    for(int i=0;i<MAX;i++)
    {
        cout<<"address of variable "<<i<<" is"<<endl;
        cout<<ptr<<endl;
        cout<<"value of variable "<<i<<" is"<<endl;
        cout<<*ptr<<endl;
        ptr++;
    }
    return 0;
}
