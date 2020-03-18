#include <iostream>
#include <vector>
#include <deque>

using namespace std;

int N, idx = 10;

vector<int> v[1000001];
deque<int> q;

void showAns(){
    if(v[idx].size() != 0){
        for(int i = 0 ; i < v[idx].size() ; i++){
            cout << v[idx][i];
        }
        cout << endl;
    }
    else{
        cout << -1 << endl;
    }
}
void decNum(int numSize){
    if(q.size() == numSize){
        for(int i = 0 ; i < q.size() ; i++){
            v[idx].push_back(q[i]);
        }
        if(idx == N){
            showAns();
            exit(0);
        }
        idx++;
        return;
    }
    else{
        for(int i = 0 ; i < 10 ; i++){
            if(i < q.back()){
                q.push_back(i);
                decNum(numSize);
                q.pop_back();
            }
        }
    }
}

int main(){
    cin >> N;
    if(N < 10){
        cout << N << endl;
        return 0;
    }
    for(int i = 0 ; i < 10 ; i++){
        v[i].push_back(i);
    }
    for(int i = 2 ; i <= 10 ; i++){
        for(int j = i - 1 ; j < 10 ; j++){
            q.push_back(j);
            decNum(i);
            q.pop_back();
        }
    }
    cout << -1 << endl;
    return 0;
}