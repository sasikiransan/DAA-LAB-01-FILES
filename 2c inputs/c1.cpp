#include<iostream>
#include<vector>
#include<ctime>
using namespace std;
int letter_to_value(char ch){
    if(ch>='A'&&ch<='Z')return ch-'A'+1;
    return ch-'a'+27;
}
char value_to_letter(int v){
    if(v>=1&&v<=26)return 'A'+v-1;
    return 'a'+v-27;
}
void insertion_sort(vector<int>&arr){
    for(int i=1;i<arr.size();i++){
        int key=arr[i];
        int j=i-1;
        while(j>=0&&arr[j]>key){
            arr[j+1]=arr[j];
            j--;
        }
        arr[j+1]=key;
    }
}
int main(){
    int n;
    cin>>n;
    vector<int>arr(n);
    for(int i=0;i<n;i++){
        char ch;
        cin>>ch;
        arr[i]=letter_to_value(ch);
    }
    clock_t start=clock();
    insertion_sort(arr);
    clock_t end=clock();
    cout<<"Time:"<<((double)(end-start)/CLOCKS_PER_SEC)<<"seconds\n";
    return 0;
}
