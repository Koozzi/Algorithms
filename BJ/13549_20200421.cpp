#include <iostream>
#include <queue>
#define INIT_NUM 98765432
#define MAX_NUM 100001
using namespace std;

int M, N;
int Time[MAX_NUM];

void init(){
    for(int i = 0 ; i < MAX_NUM ; i++){
        Time[i] = INIT_NUM;
    }
}

int BFS(){
    queue<pair<int, int>> q;
    q.push({M, 0});
    Time[M] = 0;
    while(!q.empty()){
        int c = q.front().first;
        int t = q.front().second;
        int n = 0;
        q.pop();

        if(c == N){
            return Time[c];
            // retrun t; 를 하면 왜 틀릴까?
        }

        if(c > 0 && c * 2 < MAX_NUM){
            if(Time[c * 2] > t){
                q.push({c * 2, t});
                Time[c * 2] = t;
            }
        }

        if(c + 1 < MAX_NUM){
            if(Time[c + 1] > t + 1){
                q.push({c + 1 , t + 1});
                Time[c + 1] = t + 1;
            } 
        }

        if(c - 1 >= 0){
            if(Time[c - 1] > t + 1){
                q.push({c - 1 , t + 1});
                Time[c - 1] = t + 1;
            }
        }
    }
}

int main(){
    init();
    cin >> M >> N;
    cout << BFS() << "\n";
    return 0;
}