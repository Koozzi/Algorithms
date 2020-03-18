#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int N, S, ans = 0, sum = 0;;
int arr[40];
vector<int> v;

void solve(int maxCnt, int start){
    if(v.size() == maxCnt){
        if(sum == S){
            ans++;
        }
    }
    else{
        for(int i = start + 1 ; i < N ; i++){
            v.push_back(arr[i]);
            sum += arr[i];
            solve(maxCnt, i);
            v.pop_back();
            sum -= arr[i];
        }
    }
}

int main(){
    cin >> N >> S;
    for(int i = 0 ; i < N ; i++){
        cin >> arr[i];
    }
    sort(arr, arr + N);
    for(int i = 1 ; i <= N ; i++){
        for(int j = 0 ; j < N ; j++){
            v.push_back(arr[j]);
            sum += arr[j];
            solve(i, j);
            v.pop_back();
            sum -= arr[j];
        }
    }
    cout << ans << endl;
    return 0;
}