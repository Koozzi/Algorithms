#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int M;
int arr[500000];
int ans[500000];

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin>> M;
    for(int i = 0 ; i < M ; i++){
        cin >> arr[i];
    }
    bool flag = false;
    for(int i = M - 1 ; i >= 0 ; i--){
        for(int j = i ; j >= 0 ; j--){
            if(arr[j] > arr[i]){
                ans[i] = j + 1;
                flag = true;
                break;
            }
        }
        if(!flag){
            ans[i] = 0;
        }
    }
    for(int i = 0 ; i < M ; i++){
        cout << ans[i] << " ";
    }
    return 0;
}