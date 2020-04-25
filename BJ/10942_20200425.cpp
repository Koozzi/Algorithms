#include <iostream>
using namespace std;

int M, N;
int arr[2001];
bool dp[2001][2001];

void palindrome(){
    for(int i = 1 ; i <= M ; i++){
        dp[i][i] = true;
    }
    for(int i = 1 ; i < M ; i++){
        if(arr[i] == arr[i+1]){
            dp[i][i+1] = true;
        }
    }
    for(int l = 3 ; l <= M ; l++){
        for(int i = 1 ; i+l-1 <= M ; i++){
            if(arr[i] == arr[i+l-1] && dp[i+1][i+l-2]){
                dp[i][i+l-1] =true;
            }
        }
    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> M;
    for(int i = 1 ; i <= M ; i++){
        cin >> arr[i];
    }
    palindrome();
    cin >> N;
    for(int i = 0 ; i < N ; i++){
        int a, b; cin >> a >> b;
        cout << dp[a][b] << "\n";
    }
    return 0;
}