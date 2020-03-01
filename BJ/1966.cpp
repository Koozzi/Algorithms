#include <iostream>
#include <algorithm>
#include <deque>

using namespace std;

bool isBiggest(deque<pair<int, int>> d){
    bool check = true;
    for(int i = 0 ; i < d.size() ; i++){
        if(d.front().second < d[i].second){
            check = false;
            break;
        }
    }
    return check;
}

void show(deque<pair<int, int>> d){
    for(int i = 0 ; i < d.size() ; i++){
        cout << d[i].second << " ";
    }
    cout << "\n";
}

int main(){
    int T;
    cin >> T;
    deque<pair<int, int>> dq;
    while(T--){
        dq.clear();
        int M, N, cnt = 0;
        cin >> M >> N;
        for(int i = 0 ; i < M ; i++){
            int a;
            cin >> a;
            dq.push_back(make_pair(i,a));
        }
        while(1){
            for(int i = 0 ; i < dq.size() ; i++){
                if(dq.front().second < dq[i].second){
                    int docNum = dq.front().first;
                    int docVal = dq.front().second;
                    dq.pop_front();
                    dq.push_back(make_pair(docNum, docVal));
                    break;
                }
            }
            if(isBiggest(dq)){
                if(dq.front().first == N){
                    cout << cnt + 1 << "\n";
                    break;
                }
                cnt++;
                dq.pop_front();
            }
        }
    }
    return 0;
}