#include <iostream>
#include <vector>
#include <queue>
#include <cstring>
#include <stack>

using namespace std;

int M, N, ans, minTime = 100001;
int costtime[100001];
int parent[100001];

stack<int> s;

void BFS(int start, int end){
    queue<pair<int, int>> q;
    q.push(make_pair(start, 0));
    costtime[start] = 0;
    while(!q.empty()){
        int c = q.front().first;
        int d = q.front().second;
        q.pop();

        if(c == end){
            cout << d << "\n";
            int idx = c;
            s.push(end);
            while(idx != start){
                s.push(parent[idx]);
                idx = parent[idx];
            }
            while(!s.empty()){
                cout << s.top() << " ";
                s.pop();
            }
            return;
        }

        int n;
        n = c * 2;
        if(c != 0 && n <= 100000){
            if(d + 1 <= costtime[n]){
                q.push(make_pair(n, d + 1));
                costtime[n] = d + 1;
                parent[n] = c;
            }
        }

        n = c + 1;
        if(n <= 100000){
            if(d + 1 <= costtime[n]){
                q.push(make_pair(n, d + 1));
                costtime[n] = d + 1;
                parent[n] = c;
            }
        }

        n = c - 1;
        if(n >= 0){
            if(d + 1 <= costtime[n]){
                q.push(make_pair(n, d + 1));
                costtime[n] = d + 1;
                parent[n] = c;
            }
        }
    }    
}

int main(){
    cin >> M >> N;

    memset(costtime, 98765432, sizeof(costtime));

    BFS(M, N);
    
    return 0;
}