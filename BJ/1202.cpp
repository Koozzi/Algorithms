#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>

using namespace std;

const int MAX = 300000;

int M, N;
int bag[MAX];
pair<int, int> jew[MAX];
priority_queue<int> pq;

int main(){
    cin >> M >> N;
    for(int i = 0 ; i < M ; i++){
        cin >> jew[i].first >> jew[i].second;
    }
    for(int i = 0 ; i < N ; i++){
        cin >> bag[i];
    }

    sort(jew, jew + M);
    sort(bag, bag + N);

    long long ans = 0;
    int idx = 0;

    for(int i = 0 ; i < N ; i++){
        while(idx < M && jew[idx].first <= bag[i]){
            pq.push(jew[idx++].second);
        }
        if(!pq.empty()){
            ans += pq.top();
            pq.pop();
        }
    }
    cout << ans << "\n";
    return 0;
}