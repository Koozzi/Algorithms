#include <iostream>
#include <algorithm>
#define MAX_NUM 2e9
using namespace std;

int N, arr[13][13], ans = MAX_NUM;
bool visit[13];

void func(int prev, int sum, int length){
    if(length == N && arr[prev][1] != 0){
        ans = min(ans, sum + arr[prev][1]);
        return;
    }
    for(int i = 2 ; i <= N ; i++){
        if(visit[i] || arr[prev][i] == 0) continue;
        if(sum + arr[prev][i] > ans) continue;
        visit[i] = true;
        func(i, sum + arr[prev][i], length + 1);
        visit[i] = false;
    }
}

int main(){
    cin >> N;
    for(int i = 1 ; i <= N ; i++){
        for(int j = 1 ; j <= N ; j++){
            cin >> arr[i][j];
        }
    }
    func(1, 0, 1);
    cout << ans << "\n";
    return 0;
}