#include <iostream>
#include <algorithm>
#include <vector>
#define MAX_NUM 100001
using namespace std;

int M, K, ans;
int dp[101][MAX_NUM];
vector<pair<int, int>> v;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> M >> K;
    v.push_back({0,0});
    for(int i = 0 ; i < M ; i++){
        int a, b;
        cin >> a >> b;
        v.push_back({a,b});
    }
    
    for(int i = 1 ; i <= K ; i++){
        if(i >= v[1].first){
            dp[1][i] = v[1].second;
        }
    }

    for(int i = 2 ; i <= M ; i++){
        for(int j = 1 ; j <= K ; j++){
            dp[i][j] = dp[i-1][j];
            int weight = v[i].first;
            int value = v[i].second;
            if(j >= weight){
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value);
                ans = max(ans, dp[i][j]);
            }
        }
    }

    cout << ans << "\n";
    return 0;
}