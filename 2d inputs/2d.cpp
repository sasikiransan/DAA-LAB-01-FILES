#include<iostream>
#include<algorithm>
#include<vector>
#include<ctime>
using namespace std;
void custom_sort(vector<int>&arr){
    vector<int>neg,pos;
    bool hasZero=false;
    for(int x:arr){
        if(x<0)neg.push_back(x);
        else if(x>0)pos.push_back(x);
        else hasZero=true;
    }
    sort(neg.begin(),neg.end(),greater<int>());
    sort(pos.begin(),pos.end());
    arr.clear();
    for(int x:neg)arr.push_back(x);
    if(hasZero)arr.push_back(0);
    for(int x:pos)arr.push_back(x);
}
int main(){
    int n;
    cin>>n;
    vector<int>arr(n);
    for(int i=0;i<n;i++)cin>>arr[i];
    clock_t start=clock();
    custom_sort(arr);
    clock_t end=clock();
    cout<<"Time: "<<(double)(end-start)/CLOCKS_PER_SEC<<" seconds\n";
    return 0;
}
