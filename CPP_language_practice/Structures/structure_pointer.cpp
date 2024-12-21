#include<iostream>
using namespace std;
struct Distance
{
    int feet;
    float inch;
};
int main()
{
    Distance *ptr,d;
    ptr=&d;
    cout<<"enter feet"<<endl;
    cin>>(*ptr).feet;
    cout<<"enter inch"<<endl;
    cin>>(*ptr).inch;
    cout<<"distance = "<<(*ptr).feet<<"feet "<<(*ptr).inch<<"inch";
}
