#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int N, H;
    cin >> N >> H;

    vector<int> bottom(N/2), top(N/2);
    for(int i = 0 ; i < N / 2 ; i++){
        cin >> bottom[i] >> top[i];
    }

    sort(bottom.begin(), bottom.end());
    sort(top.begin(), top.end());

    int result = 987654321;
    int cnt = 1;
    for(int i = 1 ; i <= H ; i++){
        int tmp = bottom.size() - (lower_bound(bottom.begin(), bottom.end(), i) - bottom.begin());
        tmp += top.size() - (upper_bound(top.begin(), top.end(), H - i) - top.begin());

        if(result == tmp){
            cnt++;
        }
        else if(result > tmp){
            result = tmp;
            cnt = 1;
        }
    }
    cout << result << " " << cnt << endl;
    return 0;
}