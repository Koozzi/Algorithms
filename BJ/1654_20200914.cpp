#include <iostream>
#include <algorithm>
using namespace std;

int N, M;
long long ans, low, mid, high;
int arr[10000];

long long get_line(int n){
    long long sum = 0;
    for(int i = 0 ; i < N ; i++){
        sum += arr[i] / n;
    }
    return sum;
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    cin >> N >> M;
    for(int i = 0 ; i < N ; i++){
        cin >> arr[i];
    } sort(arr, arr+N);

    low = 1;
    high = arr[N-1];

    while(low <= high){
        mid = (low + high) / 2;
        if(get_line(mid) >= M){
            low = mid + 1;
            ans = max(ans, mid);
        }
        else{
            high = mid - 1;
        }
    }
    cout << ans << "\n";
    return 0;
}