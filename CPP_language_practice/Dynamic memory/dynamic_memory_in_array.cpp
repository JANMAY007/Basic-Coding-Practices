#include<iostream>
using namespace std;
int main()
{
    int length,sum=0;
    cout<<"enter total students in group: "<<endl;
    cin>>length;
    int *marks=new int[length];
    cout<<"enter the marks of students: "<<endl;
    for(int i=0;i<length;i++)
    {
        cin>>*(marks+i);
    }
    for(int i=0;i<length;i++)
    {
        sum+=*(marks+i);
    }
    cout<<"the sum is "<<sum<<endl;
    return 0;
}
