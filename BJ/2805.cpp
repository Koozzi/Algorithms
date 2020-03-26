#include <iostream>

using namespace std;

long long int M, N;
long long int tree[1000000];

long long int cutTree(long long int a){
    long long int sum = 0;
    for(int i = 0 ; i < M ; i++){
        if(tree[i] >= a){
            sum += (tree[i] - a);
        }
    }
    return sum;
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cin >> M >> N;
    long long int high = 0;
    long long int low = 1;
    for(int i = 0 ; i < M ; i++){
        cin >> tree[i];
        high = max(high, tree[i]);
    }

    long long int ans = 0;
    while(low <= high){
        long long int mid = (high + low) / 2;
        if(cutTree(mid) >= N){
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

