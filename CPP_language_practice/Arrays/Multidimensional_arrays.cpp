#include<iostream>
using namespace std;
int main()
{
    float marks[5][3];
    int i,j;
    for(i=0;i<5;i++)
    {
        cout<<"enter marks of student "<<i+1<<": "<<endl;
        for(j=0;j<3;j++)
        {
            cout<<"subject "<<j+1<<": "<<endl;
            cin>>marks[i][j];
        }
    }
    for(i=0;i<5;i++)
    {
        cout<<"Marks of student "<<i+1<<": "<<endl;
        for(j=0;j<3;j++)
        {
            cout<<"subject "<<j+1<<": "<<marks[i][j]<<endl;
        }
    }
    return 0;
}