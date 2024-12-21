#include<iostream>
using namespace std;
int main()
{
    int number;
    cout<<"enter a number: ";
    cin>>number;
    if(number>0)
    {
        cout<<"you entere a positive number."<<endl;
    }
    else if(number<0)
    {
        cout<<"you entered a negative number."<<endl;
    }
    else
    {
        cout<<"you entered 0(zero)."<<endl;
    }
    return 0;
}