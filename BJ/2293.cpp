#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N, K;
int dp[2][10001];

vector<int> v;

int main(){
    cin >> N >> K;
    v.push_back(0);
    for(int i = 0 ; i < N ; i++){
        int a;
        cin >> a;
        v.push_back(a);
    }
    sort(v.begin(), v.end());
    for(int i = 1 ; i <= K ; i++){
        if(i % v[1] == 0){
            dp[1][i] = 1;
        }
    }
    for(int i = 2 ; i <= N ; i++){
        for(int j = 1 ; j <= K ; j++){
            if(i % 2 == 0){
                dp[0][j] = 0;
                if(j % v[i] == 0){
                    dp[0][j] += 1;
                }
                for(int k = j ; k >= 0 ; k -= v[i]){
                    dp[0][j] += dp[1][k];
                }
            }
            else{
                dp[1][j] = 0;
                if(j % v[i] == 0){
                    dp[1][j] += 1;
                }
                for(int k = j ; k >= 0 ; k -= v[i]){
                    dp[1][j] += dp[0][k];
                }
            }
        }
    }
    if(N % 2 == 0){
        cout << dp[0][K] << endl;
    }
    else{
        cout << dp[1][K] << endl;
    }

    return 0;    
}