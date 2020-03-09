#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N, K;
int dp[101][10001];

vector<int> v;
void show(){
    cout << endl;
    for(int i = 1; i <= N ; i++){
        for(int j = 1 ; j <= K ; j++){
            cout << dp[i][j] << " ";
        }cout << endl;
    }
}
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
            dp[1][i] = i / v[1];
        }
        else{
            dp[1][i] = 100001;
        }
    }
    for(int i = 2 ; i <= N ; i++){
        for(int j = 1 ; j <= K ; j++){
            int div = j / v[i];
            if(j % v[i] == 0){
                dp[i][j] = div;
            }
            else{
                int minValue = 100002;
                int cnt = 0;
                for(int t = j ; t > 0 ; t -= v[i]){
                    minValue = min(minValue , dp[i-1][t]+ cnt) ;
                    cnt++;
                }
                dp[i][j] = minValue;
            }
        }
    }
    
    if(dp[N][K] == 100001){
        cout << -1 << endl;
    }
    else{
        cout << dp[N][K] << endl;
    }
    return 0;
}