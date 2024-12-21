#include<iostream>
using namespace std;
int count_pairs(int a[], int b[], int n, int m)
{
    int odd1=0,odd2=0;
    int even1=0,even2=0;
    for(int i=0;i<n;i++)
    {
        if(a[i]%2==0)
        {
            even1++;
        }
        else
        {
            odd1++;
        }
    }
    for(int i=0;i<m;i++)
    {
        if(b[i]%2==0)
        {
            even2++;
        }
        else
        {
            odd2++;
        }
    }
    int pairs=min(odd1,even2)+min(odd2,even1);
    return pairs;
}
int main()
{
    int a[]={9,14,6,2,11};
    int b[]={8,4,7,20};
    int n=sizeof(a)/sizeof(a[0]);
    int m=sizeof(b)/sizeof(b[0]);
    cout<<count_pairs(a,b,n,m);
    return 0;
}
