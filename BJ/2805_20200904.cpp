#include <iostream>
#include <algorithm>
using namespace std;

long long N, M, high, low;
long long ans;
long long arr[1000000];

long long get_wood(int n, int H, long long wood_arr[]){
    long long sum = 0;
    for(int i = 0 ; i < n ; i++){
        if(wood_arr[i] > H) sum += (wood_arr[i] - H);
    }
    return sum;
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    cin >> N; cin >> M;
    for(int i = 0 ; i < N ; i++){
        cin >> arr[i];
        high = max(high, arr[i]);
    }
    while(low <= high){
        long long mid = (high + low) / 2;
        if(get_wood(N, mid, arr) >= M){
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