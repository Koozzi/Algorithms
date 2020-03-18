#include <iostream>
#include <deque>

using namespace std;

int M, N;
bool used[32001];
deque<int> dq;

int main(){
    cin >> M >> N;
    for(int i = 0 ; i < N ; i++){
        int a, b;
        cin >> a >> b;
        if(!used[a] && !used[b]){
            dq.push_back(a);
            dq.push_back(b);
            used[a] = true;
            used[b] = true;
        }
        else if(!used[a] && used[b]){
            dq.push_front(a);
            used[a] = true;
        }
        else if(used[a] && !used[b]){
            dq.push_back(b);
            used[b] = true;
        }
    }
    for(int i = 1 ; i <= M ; i++){
        if(!used[i]){
            dq.push_back(i);
        }
    }
    for(int i = 0 ; i < dq.size() ; i++){
        cout << dq[i] << " ";
    }
    return 0;
}