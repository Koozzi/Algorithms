#include <algorithm>
#include <iostream>
using namespace std;

int N, M, ans, low, mid, high;
int arr[10000];

long long check_budget(int n){
    int sum = 0;
    for(int i = 0 ; i < N ; i++){
        if(arr[i] <= n) sum += arr[i];
        else sum += n;
    }
    return sum;
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    cin >> N;
    int sum = 0;
    for(int i = 0 ; i < N ; i++){
        cin >> arr[i];
    } sort(arr, arr+N);
    cin >> M;

    low = 1;
    high = arr[N-1];

    while(low <= high){
        mid = (low + high) / 2;
        if(check_budget(mid) <= M){
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