#include <iostream>
#include <algorithm>
using namespace std;

int N, M, arr[100000];

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    cin >> N >> M;
    for(int i = 0 ; i < N ; i++){
        cin >> arr[i];
    }

    int sum = 0;
    for(int i = 0 ; i < M ; i++){
        sum += arr[i];
    }
    int ans = sum;
    int left = 0;
    int right = M;

    while(right != N){
        sum -= arr[left++];
        sum += arr[right++];
        ans = max(ans, sum);
    }
    cout << ans << "\n";
    return 0;
}