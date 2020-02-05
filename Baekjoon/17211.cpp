#include <iostream>
#include <math.h>

using namespace std;

int main(){
    int N, M; 
    float a, b, c, d;
    float dp[101][2] = {0};
    cin >> N >> M >> a >> b >> c >> d;
    if(N != 1){
        if(M == 1){
            dp[1][0] = d;
            dp[1][1] = c;
            for(int i = 2 ; i < N+1 ; i++){
                dp[i][0] = dp[i-1][0] * d + dp[i-1][1] * b;
                dp[i][1] = dp[i-1][0] * c + dp[i-1][1] * a;
            }
        }
        else{
            dp[1][0] = b;
            dp[1][1] = a;
            for(int i = 2 ; i < N+1 ; i++){
                dp[i][0] = dp[i-1][0] * d + dp[i-1][1] * b;
                dp[i][1] = dp[i-1][0] * c + dp[i-1][1] * a;
            }
        }
        cout << round(dp[N][1] * 1000) << "\n" << round(dp[N][0] * 1000) << "\n";
    }
    else{
        if(M == 0){
            cout << round(a * 1000) << "\n" << round(b * 1000) << "\n";
        }
        else{
            cout << round(c * 1000) << "\n" << round(d * 1000) << "\n";
        }
    }
    return 0;
}