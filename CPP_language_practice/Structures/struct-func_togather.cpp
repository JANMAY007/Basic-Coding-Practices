#include<iostream>
using namespace std;
struct Person
{
    char name[50];
    int age;
    float salary;
};
void Display(Person);
int main()
{
    Person p;
    cout<<"enter name:"<<endl;
    cin.get(p.name,50);
    cout<<"enter age:"<<endl;
    cin>>p.age;
    cout<<"enter salary:"<<endl;
    cin>>p.salary;
    Display(p);
    return 0;
}
void Display(Person p)
{
    cout<<"name is "<<p.name<<endl;
    cout<<"age is "<<p.age<<endl;
    cout<<"salary is "<<p.salary<<endl;
}
