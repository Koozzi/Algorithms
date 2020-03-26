#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

long long int M, N;
long long int low = 1, high, mid, ans;
vector<long long int> v;

long long int check(long long int mid){
    long long int sum = 0;
    for(int i = 0 ; i < M ; i++){
        if(mid >= v[i]){
            sum += v[i];
        }
        else{
            sum += mid;
        }
    }
    return sum;
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    cin >> M;
    long long int A = 0; 
    for(int i = 0 ; i < M ; i++){
        long long int a; cin >> a;
        A += a;
        v.push_back(a);
        high = max(high, a);
    }
    sort(v.begin(), v.end());
    cin >> N;

    if(A <= N){ // 요청대로 모든 지방에 예산을 나누어 줄 수 있는 경우
        cout << high << "\n";
        return 0;
    }

    while(low <= high){
        mid = (low + high) / 2;
        if(N >= check(mid)){
            low = mid + 1;
            ans = max(ans , mid);
        }
        else{
            high = mid - 1;
        }
    }
    cout << ans << endl;
    return 0;
}