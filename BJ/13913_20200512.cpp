#include <iostream>
#include <queue>
#include <stack>
#define MAX_NUM 100001
#define INIT_NUM 98765432
using namespace std;

int M, N;

stack<int> s;

typedef struct{
    int t;
    int prev;
}loca;
loca info[MAX_NUM];

void init(){
    for(int i = 0 ; i < MAX_NUM ; i++){
        info[i].t = INIT_NUM;
    }
}

int BFS(){
    queue<int> q;
    q.push(M);
    info[M].t = 0;
    while(!q.empty()){
        int c = q.front();
        int n;
        q.pop();

        if(c == N){
            return info[c].t;
        }
        // 순간이동
        n = c * 2;
        if(c != 0 && n < MAX_NUM){
            if(info[c].t + 1 < info[n].t){
                info[n].t = info[c].t + 1;
                info[n].prev = c;
                q.push(n);
            }
        }

        // 오른쪽
        n = c + 1;
        if(n < MAX_NUM){
            if(info[c].t + 1 < info[n].t){
                info[n].t = info[c].t + 1;
                info[n].prev = c;
                q.push(n);
            }
        }
        
        // 왼쪽
        n = c - 1;
        if(n >= 0){
            if(info[c].t + 1 < info[n].t){
                info[n].t = info[c].t + 1;
                info[n].prev = c;
                q.push(n);
            }            
        }
    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    init();

    cin >> M >> N;
    int ans = BFS();
    cout << ans << "\n";
    
    for(int i = 0 ; i <= ans ; i++){
        s.push(N);
        N = info[N].prev;
    }

    while(!s.empty()){
        cout << s.top() << " ";
        s.pop();
    }
}