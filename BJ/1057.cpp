#include <iostream>
#include <deque>

using namespace std;

int N, A, B;

deque<int> dq;
deque<int> newdq;

bool meet(){
    for(int i = 1 ; i < dq.size() ; i++){
        if(dq[i] == A || dq[i] == B){
            if(i % 2 == 0){
                if(dq[i-1] == A || dq[i-1] == B){
                    return true;
                }
                else{
                    return false;
                }
            }
            else{
                if(dq[i+1] == A || dq[i+1] == B){
                    return true;
                }
                else{
                    return false;
                }
            }
        }
    }
}

void tournament(){
    for(int i = 1 ; i <= dq.size() - 1 ; i+=2){
        if(dq[i+1] != A && dq[i+1] != B){
            newdq.push_back(dq[i]);
        }
        else{
            newdq.push_back(dq[i+1]);
        }
    }
    dq.clear();
    dq.push_back(0);
    for(int i = 0 ; i < newdq.size() ; i++){
        dq.push_back(newdq[i]);
    }
    newdq.clear();
}

int main(){
    cin >> N >> A >> B;
    dq.push_back(0);
    for(int i = 1 ; i <= N ; i++){
        dq.push_back(i);
    }
    if(N % 2 != 0){
        dq.push_back(0);
    }
    int cnt = 1;
    while(N > 1){
        if(meet()){
            cout << cnt << "\n";
            return 0;
        }
        tournament();
        cnt++;
        if(N % 2 != 0){
            N = N / 2 + 1;
        }
        else{
            N = N / 2;
        }
    }
    cout << -1 << "\n";
    return 0;
}