#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int M;
long long sum, ans;
long long arr[4][4000];
vector<long long> v;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> M;
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < 4 ; j++){
            cin >> arr[j][i];
        }
    }
    
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < M ; j++){
            v.push_back(arr[2][i] + arr[3][j]);
        }
    }sort(v.begin(), v.end());

    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < M ; j++){
            long long half = arr[0][i] + arr[1][j];
            long long low = lower_bound(v.begin(), v.end(), - half) - v.begin();
            long long high = upper_bound(v.begin(), v.end(), -half) - v.begin();

            if(-half == v[low]){
                ans += (high - low);
            }
        }
    }

    cout << ans << "\n";
    return 0;
}