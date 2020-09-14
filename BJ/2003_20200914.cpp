#include <iostream>
#include <algorithm>
using namespace std;

int N, M;
int arr[10000];

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    cin >> N >> M;
    for(int i = 0 ; i < N ; i++){
        cin >> arr[i];
    }

    int left = 0;
    int right = 0;
    int sum = 0;
    int ans = 0;

    while(1){
        if(sum == M){
            ans++;
            sum -= arr[left++];
        }
        else if(sum > M) sum -= arr[left++];
        else if(right == N) break;
        else sum += arr[right++];
    }
    cout << ans << "\n";
    return 0;
}