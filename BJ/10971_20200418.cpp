#include <iostream>
#include <algorithm>
using namespace std;

int M, arr[8], w[11][11], sum, ans = 98765432;

int main(){
    cin >> M;
    for(int i = 1 ; i <= M ; i++){
        for(int j = 1 ; j <= M ; j++){
            cin >> w[i][j];
        }
    }

    for(int i = 0 ; i < M ; i++){
        arr[i] = i + 1;
    }

    for(int i = 0 ; i < M - 1 ; i++){
        if(w[arr[i]][arr[i+1]] == 0){
            ans = 98765432;
            break;
        }
        ans += w[arr[i]][arr[i+1]];    
    }
    if(ans != 98765432) ans += w[arr[M-1]][arr[0]];

    while(next_permutation(arr, arr+M)){
        bool check = false;
        sum = 0;
        for(int i = 0 ; i < M - 1 ; i++){
            if(w[arr[i]][arr[i+1]] == 0){
                check = true;
                break;
            }
            sum += w[arr[i]][arr[i+1]];    
        }
        if(check) continue;
        if(w[arr[M-1]][arr[0]] == 0) continue;
        sum += w[arr[M-1]][arr[0]];
        ans = min(ans, sum);
    }
    cout << ans << "\n";
    return 0;
}