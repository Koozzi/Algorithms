#include <iostream>
#include <algorithm>
using namespace std;

long long S, N, ans;

bool is_possible(long long num){
    
}

int main(){
    cin >> S;

    long long low = 1;
    long long high = S;

    while(low <= high){
        long long mid = (low + high) / 2;
        if(is_possible(mid)){
            ans = max(ans, mid);
            low = mid + 1;
        }
        else high = mid - 1;
    }
    cout << ans << "\n";
    return 0;
}