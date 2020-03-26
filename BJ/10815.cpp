#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

vector<int> v;

int M, N, a;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> M;
    for(int i = 0 ; i < M ; i++){
        int vec;
        cin >> vec;
        v.push_back(vec);
    }

    sort(v.begin(), v.end());

    cin >> N;
    for(int i = 0 ; i < N ; i++){
        cin >> a;

        int ans = 0;
        int low = 0;
        int high = v.size() - 1;

        if(a < v[0] || a > v[v.size() - 1]){
            cout << 0 << " ";
            continue;
        }

        while(high >= low){
            int mid = (low + high) / 2;
            if(v[mid] == a){
                ans = 1;
                break;
            }
            if(v[mid] <= a){
                low = mid + 1;
            }
            else{
                high = mid - 1;
            }
        }
        cout << ans << " ";
    }
    return 0;
}
