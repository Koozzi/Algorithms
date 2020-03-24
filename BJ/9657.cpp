#include <iostream>

using namespace std;

int main(){
    bool dp[1001];
    dp[1] = true;
    dp[2] = false;
    dp[3] = true;
    dp[4] = true;

    int M;
    cin >> M;

    for(int i = 5 ; i <= M ; i++){
        if(!dp[i-1] || !dp[i-3] || !dp[i-4]){
            dp[i] = true;
        }
        else{
            dp[i] = false;
        }
    }
    if(dp[M]){
        cout << "SK" << endl;
    }
    else{
        cout << "CY" << endl;
    }
    return 0;
}