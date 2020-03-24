#include <iostream>
#include <string>

using namespace std;

int M;

string dp[10001];

void sumString(int I, int J){
    int tmp = 0;
    for(int i = 0 ; i < dp[I].size() ; i++){
        int a = dp[I][i] - 48;
        int b = dp[J][i] - 48;
        int sum = a + b + tmp;
        if(sum >= 10){
            sum = sum - 10;
            tmp = 1;
        }
        else{
            tmp = 0;
        }
        dp[J+1].push_back(char(sum + 48));
        if(i == dp[I].size() - 1 && tmp == 1 && dp[I].size() == dp[J].size()){
            dp[J+1].push_back(char(49));
        }
    }
    if(dp[I].size() < dp[J].size()){
        int a = dp[J][dp[J].size() - 1] - 48;
        int sum = a + tmp;
        if(sum < 10){
            dp[J+1].push_back(char(sum + 48));
        }
        else{
            sum = sum - 10;
            dp[J+1].push_back(char(sum + 48));
        }
    }
}

int main(){
    cin >> M;

    dp[0].push_back('0');
    dp[1].push_back('1');

    // dp[4].push_back('4');
    // dp[4].push_back('5');
    // dp[4].push_back('9');

    // dp[5].push_back('3');
    // dp[5].push_back('9');
    // dp[5].push_back('9');
    // dp[5].push_back('1');

    // sumString(4,5);

    // for(int i = dp[6].size() - 1 ; i >= 0 ; i--){
    //     cout << dp[6][i];
    // }cout << endl;

    for(int i = 2 ; i <= M ; i++){
        sumString(i-2, i-1);
    }

    for(int i = dp[M].size() - 1 ; i >= 0 ; i--){
        cout << dp[M][i];
    }cout << endl;    

    return 0;
}
