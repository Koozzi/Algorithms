#include <iostream>
#include <algorithm>
using namespace std;

int N, M, ans, arr[200000];
int low = 1, mid, high;

bool is_possible(){
    int cnt = 1;
    int prev = arr[0];
    for(int i = 1 ; i < N ; i++){
        if(arr[i] - prev >= mid){
            cnt++;
            prev = arr[i];
        }
    }
    if(cnt >= M) return true;
    return false;
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    cin >> N >> M;
    for(int i = 0 ; i < N ; i++){
        cin >> arr[i];
    } sort(arr, arr+N);

    high = arr[N-1] - arr[0];

    while(low <= high){
        mid = (low + high) / 2;
        if(is_possible()){
            ans = max(ans, mid);
            low = mid + 1;
        }
        else{
            high = mid - 1;
        }
    }
    cout << ans << "\n";
    return 0;
}