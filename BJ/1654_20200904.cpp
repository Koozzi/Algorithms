#include <iostream>
#include <algorithm>
using namespace std;

long long N, K, arr[10000];
long long ans, low = 1, mid, high;

long long get_length(){
    long long sum = 0;
    for(int i = 0 ; i < K ; i++){
        sum += (arr[i] / mid);
    }
    return sum;
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    cin >> K; cin >> N;
    for(int i = 0 ; i < K ; i++){
        cin >> arr[i];
        high = max(high, arr[i]);
    }

    while(low <= high){
        mid = (low + high) / 2;
        if(get_length() >= N){
            ans = max(ans, mid);
            low = mid + 1;
        }
        else high = mid - 1;
    }
    cout << ans << "\n";
    return 0;
}