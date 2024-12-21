#include<iostream>
using namespace std;
int main()
{
    int a;
    double b=2.55;
    a=b;//implicite type cast for compiler
    cout<<a<<endl;
    a=(int)b;//explicite type cast for the compiler
    cout<<a<<endl;
    a=int(b);//explicite type cast for the compiler
    cout<<a<<endl;
    return 0;
}