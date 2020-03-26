#include <iostream>
#include <algorithm>

using namespace std;

int M, N;
int a, ans;
int arr[100000];
int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    
    cin >> M;
    for(int i = 0 ; i < M ; i++){
        cin >> arr[i];
    }
    
    sort(arr, arr + M);
    
    cin >> N;
    for(int i = 0 ; i < N ; i++){
        ans = 0;
        cin >> a;

        int low = 0;
        int high = M - 1;

        while(low <= high){
            int mid = (low + high) / 2;
            if(arr[mid] == a){
                ans = 1;
                break;
            }
            if(a >= arr[mid]){
                low = mid + 1;
            }
            else{
                high = mid - 1;
            }
        }
        cout << ans << "\n";
    }
    return 0;
}