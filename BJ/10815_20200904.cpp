#include <iostream>
#include <algorithm>
using namespace std;

int N, M;
int arr[500000];

void solve_with_library(){
    cin >> M;
    for(int i = 0 ; i < M ; i++){
        int a; cin >> a;
        if(binary_search(arr, arr + N, a)) cout << 1 << " ";
        else cout << 0 << " ";
    }cout << "\n";
}

void solve_with_no_library(){
    cin >> M;
    for(int i = 0 ; i < M ; i++){
        int a; cin >> a;
        int low = 0; int high = N - 1;
        int ans = 0;

        if(a > arr[N-1] || a < arr[0]){
            cout << ans << " ";
            continue;
        }

        while(low <= high){
            int mid = (high + low) / 2;
            if(arr[mid] == a){
                ans = 1;
                break;
            }
            else if(arr[mid] > a){
                high = mid - 1;
            }
            else{
                low = mid + 1;
            }
        }
        cout << ans << " ";
    }cout << "\n";
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    cin >> N;
    for(int i = 0 ; i < N ; i++){
        cin >> arr[i];
    } sort(arr, arr + N);
    // solve_with_library();
    solve_with_no_library();
    return 0;
}