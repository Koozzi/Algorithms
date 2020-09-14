#include <iostream>
#include <algorithm>
using namespace std;

long long N, M, ans;
long long low, mid, high;
long long arr[1000000];

long long cut_tree(int height){
    long long sum = 0;
    for(int i = 0 ; i < N ; i++){
        if(arr[i] > height) sum += (arr[i] - height);
    }
    return sum;
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    cin >> N >> M;
    
    for(int i = 0 ; i < N ; i++){
        cin >> arr[i];
        high = max(high, arr[i]);
    } 

    while(low <= high){
        mid = (high + low) / 2;
        if(cut_tree(mid) >= M){
            ans = max(ans, mid);
            low = mid + 1;
        }
        else{
            high = mid - 1;
        }
    }
    cout << ans << "\n";
}