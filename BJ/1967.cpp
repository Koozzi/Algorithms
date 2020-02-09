#include <iostream>
#include <queue>
#include <vector>
#include <memory.h>

using namespace std;

int N;
int longest = 0;

bool visited[10001];

vector<int> v[10001];
vector<pair<int ,int>> node[10001];

int BFS(int startI){
    int longA = 0;
    int depth[10001] = {0};
    queue<int> q;
    q.push(startI);
    visited[startI] = true;
    while(!q.empty()){
        int current = q.front();
        q.pop();
        for(int i = 0 ; i < node[current].size() ; i++){
            int next = node[current][i].first;
            if(!visited[next]){
                visited[next] = true;
                q.push(next);
                depth[next] = depth[current] + node[current][i].second;
                if(depth[next] >= longA){
                    longA = depth[next];
                }
            }
        }
    }
    return longA;
}

int main(){
    cin >> N;
    for(int i = 1 ; i < N ; i++){
        int a, b, c;
        cin >> a >> b >> c;
        node[a].push_back({b,c});
        node[b].push_back({a,c});
    }

    for(int i = 1 ; i <= N ; i++){
        memset(visited, false , sizeof(visited));
        int tmp = BFS(i);
        if(tmp >= longest){
            longest = tmp;
        }
    }
    cout << longest << "\n";
    return 0;
}

/*
메모리초과
두 노드 사이의 가중치를 위해 10001 x 10001 배열을 선언했더니 메모리 초과가 남
=> vector<pair<int ,int>> node[10001]; 선언을 함
=> 메모리 초과 해결

시간초과
2차원 배열 때문에 메인 함수에서 2중 for문을 돌렸었었음
1중 for문으로 바꾼 후 이에 맞게 코드를 조금 수정하니 시간 초과도 통과 됨
*/