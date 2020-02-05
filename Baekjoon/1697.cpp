#include <algorithm>
#include <iostream>
#include <vector>
#include <queue>

using namespace std;
int N, K;

bool visited[100001];
int depth[100001] = {0};
int nextIdx[3] = {-1, 1, 2};

int BFS(int start){
    queue<int> q;
    q.push(start);
    visited[start] = true;
    while(!q.empty()){
        int current = q.front();
        if(current == K){
            break;
        }
        q.pop();
        for(int i = 0 ; i < 3 ; i++){
            if(i != 2){
                int next = current + nextIdx[i];
                if(next > -1 && next < 100001 && current < 100001 && current > -1){
                    if(!visited[next]){
                        q.push(next);
                        visited[next] = true;
                        depth[next] = depth[current] + 1;
                    }
                }
            }
            else{
                int next = current * nextIdx[i];
                if(next > -1 && next < 100001 && current < 100001 && current > -1){
                    if(!visited[next]){
                        q.push(next);
                        visited[next] = true;
                        depth[next] = depth[current] + 1;
                    }
                }

            }
        }
    }
    return depth[K];
}

int main(){
    cin >> N >> K;
    if(N == 0 && K != 0){
        int ans = BFS(1);
        cout << ans + 1 << "\n";
    }
    else if(N == 0 && K == 0){
        cout << 0 << "\n";
    }
    else{
        int ans = BFS(N);
        cout << ans << "\n"; 
    }
    return 0;
}

/*
런타임에러 이유

current 와 next 의 범위를 고려 안 함
만약에 current 가 52345 가 되면 next 는 100000이 넘어가서 
visted 배열과 depth 배열을 참조할 수 없음.
마찬가지로 current 가 0 일 때 next 가 -1 도 될 수 있는데 
if 문을 통해 범위 설정을 해주니 통과됨.
*/