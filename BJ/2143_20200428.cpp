#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

long long T, ans;
long long arr[2][1001];
long long Sum[2][1001];
vector<long long> v[2];

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie();
    cout.tie(0);

    cin >> T;
    for(int k = 0 ; k < 2 ; k++){
        int a; cin >> a;
        for(int i = 1 ; i <= a ; i++){
            cin >> arr[k][i];
            Sum[k][i] = Sum[k][i-1] + arr[k][i];
        }
        for(int i = a ; i > 0 ; i--){
            for(int j = 0 ; j < i ; j++){
                v[k].push_back(Sum[k][i] - Sum[k][j]);
            }
        }
    }

    sort(v[0].begin(), v[0].end());

    for(int i = 0 ; i < v[1].size() ; i++){
        int num = T - v[1][i];
        int low = lower_bound(v[0].begin(), v[0].end(), num) - v[0].begin();
        int high = upper_bound(v[0].begin(), v[0].end(), num) - v[0].begin();

        if(num == v[0][low]){
            ans += (high - low);
        }
    }

    cout << ans << "\n";
    return 0;
}