#include <iostream>
#include <algorithm>

using namespace std;

int N, arr[11][11], city[11];
int ans = 98765432;

int get_sum(){
    int sum = 0;
    for(int i = 1 ; i < N ; i++){
        if(arr[city[i]][city[i+1]] == 0){
            return 98765432;
        }
        sum += arr[city[i]][city[i+1]];
    }
    if(arr[city[N]][city[1]] != 0) return sum + arr[city[N]][city[1]];
    else return 98765432;
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> N;
    
    for(int i = 1 ; i <= N ; i++){
        city[i] = i;
        for(int j = 1 ; j <= N ; j++){
            cin >> arr[i][j];
        }
    }

    ans = min(ans, get_sum());
    while(next_permutation(city+1, city+1+N)){
        ans = min(ans, get_sum());
    }
    cout << ans << "\n";
    return 0;
}