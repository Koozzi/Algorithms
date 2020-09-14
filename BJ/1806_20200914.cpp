#include <iostream>
#include <algorithm>
using namespace std;

int N, M, arr[100000];

int main(){
    cin >> N >> M;
    for(int i = 0 ; i < N ; i++){
        cin >> arr[i];
    }

    int left = 0;
    int right = 0;
    int sum = 0;
    int ans = 100001;

    while(1){
        if(sum >= M){
            ans = min(ans, right - left);
            sum -= arr[left++];
        }
        else if(right == N) break;
        else sum += arr[right++];
    }
    if(ans == 100001) cout << 0 << "\n";
    else cout << ans << "\n";
    return 0;
}