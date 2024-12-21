#include<iostream>
using namespace std;
struct person
{
    char name[50];
    int age;
    float salary;
};
int main()
{
    person p;
    cout<<"enter name:";
    cin.get(p.name,50);
    cout<<"enter salary:";
    cin>>p.salary;
    cout<<"enter age:";
    cin>>p.age;
    cout<<"the information is\n";
    cout<<p.name;
    cout<<p.age;
    cout<<p.salary;
    return 0;
}
