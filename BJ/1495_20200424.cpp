#include <iostream>
#include <algorithm>
using namespace std;

int M, startVolume, maxVolume;
bool dp[101][1001];

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> M >> startVolume >> maxVolume;

    dp[0][startVolume] = true;

    for(int i = 1 ; i <= M ; i++){
        int a; cin >> a;
        for(int j = 0 ; j <= maxVolume ; j++){
            if(!dp[i-1][j]){
                continue;
            }
            if(j - a >= 0){
                dp[i][j-a] = true;
            }
            if(j + a <= maxVolume){
                dp[i][j+a] = true;
            }
        }
    }

    int ans = -1;

    for(int i = 0 ; i <= maxVolume ; i++){
        if(dp[M][i]){
            ans = max(ans, i);
        }
    }

    cout << ans << "\n";
    return 0;
}

/*
4 50 60
6 7 2 6
-> 59

3 5 10
5 3 7
-> 10


*/