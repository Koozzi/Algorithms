#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int dp[1001][1001];

int main(){
    string str1, str2;

    cin >> str1 >> str2;
    int i, j;
    for(i = 1 ; i <= str1.size() ; i++){
        for(j = 1 ; j <= str2.size() ; j++){
            if(str1[i-1] == str2[j-1]){
                dp[i][j] = dp[i-1][j-1] + 1;
            }
            else{
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
            }
        }
    }
    cout << i << j << endl;
    cout << str1.size() << str2.size() << endl;
    cout << dp[str1.size() - 1][str2.size() - 1] << endl;

    return 0;
}