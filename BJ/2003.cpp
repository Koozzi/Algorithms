#include <iostream>

using namespace std;

int M, N;
int arr[100000];

int main(){
    cin >> M >> N;
    for(int i = 0 ; i < M ; i++){
        cin >> arr[i];
    }
    int ans = 100001;
    int sum = 0;
    int lo = 0;
    int hi = 0;

    while(1){
        if(sum > N) sum -= arr[lo++];
        else if(hi == M) break;
        else sum += arr[hi++];
        if(sum >= N) ans = min(ans, hi - lo);
    }
    if(ans == 100001){
        cout << 0 << endl;
    }
    else{
        cout << ans << endl;        
    }
    return 0;
}