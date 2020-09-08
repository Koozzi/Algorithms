#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

vector<int> increase;
vector<int> decrease;
int N, arr[1000], ans;

int get_lis(int idx){
    increase.clear();
    increase.push_back(arr[0]);
    for(int i = 1 ; i <= idx ; i++){
        if(increase.back() < arr[i]){
            increase.push_back(arr[i]);
        }
        else{
            auto iter = lower_bound(increase.begin(), increase.end(), arr[i]);
            increase[iter - increase.begin()] = arr[i];
        }
    }
    return increase.size();
}

int get_lds(int idx){
    decrease.clear();
    decrease.push_back(arr[N-1]);
    for(int i = N-2 ; i >= idx ; i--){
        if(decrease.back() < arr[i]){
            decrease.push_back(arr[i]);
        }
        else{
            auto iter = lower_bound(decrease.begin(), decrease.end(), arr[i]);
            decrease[iter - decrease.begin()] = arr[i];
        }
    }
    return decrease.size();
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    cin >> N;
    for(int i = 0 ; i < N ; i++){
        cin >> arr[i];
    }
    for(int i = 0 ; i < N ; i++){
        ans = max(ans, get_lis(i) + get_lds(i) - 1);
    }
    cout << ans << "\n";
    return 0;
}