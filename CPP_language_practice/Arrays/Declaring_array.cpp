#include<iostream>
using namespace std;
int main()
{
    int marks[5],sum=0;
    float average;
    for(int i=0;i<5;i++)
    {
        cout<<"enter marks of "<<i+1<<" student: ";
        cin>>marks[i];
    }
    for(int i=0;i<5;i++)
    {
        sum=sum+marks[i];
    }
    average=sum/5;
    cout<<"average is: "<<average;
    return 0;
}