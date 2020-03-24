#include <iostream>
#include <string>

using namespace std;

int M, N, ans = 0;
int dp[1000][1000];
string map[1000];

void show(){
    cout << endl;
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < N ; j++){
            cout << map[i][j] << " ";
        }cout << endl;
    }
    cout << endl;
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < N ; j++){
            cout << dp[i][j] << " ";
        }cout << endl;
    }
}

int main(){
    cin >> M >> N;
    for(int i = 0 ; i < M ; i++){
        cin >> map[i];
        for(int j = 0 ; j < map[i].size() ; j++){
            if(map[i][j] == '1'){
                dp[i][j] = 1;
            }
            ans = max(ans, dp[i][j]);
        }
    }
    
    for(int i = 1 ; i < M ; i++){
        for(int j = 1 ; j < N ; j++){
            int U = dp[i-1][j];
            int L = dp[i][j-1];
            int UL = dp[i-1][j-1];
            int minDP = min(U, L);
            minDP = min(minDP, UL);

            if(map[i][j] == '0'){
                dp[i][j] = 0;
                continue;
            }

            if(U == 0 || L == 0 || UL == 0){
                dp[i][j] = 1;
            }
            else{
                if(U == L && L == UL && UL == U){
                    dp[i][j] = U + 1;
                }
                else{
                    dp[i][j] = minDP + 1;
                }
            }
            ans = max(ans, dp[i][j]);
        }
    }
    
    cout << ans * ans << endl;
    return 0;
}