#include <iostream>
#include <vector>
#include <queue>

using namespace std;

vector<int> GIVE[26];
vector<int> GET[26];
vector<int> ORIGINAL;

int M, N, num, ans = 0;
bool visited[26];
bool check[26];

void BFS(int start){
    queue<int> q;
    q.push(start);
    visited[start] = true;
    while(!q.empty()){
        int current = q.front();
        q.pop();
        for(int i = 0 ; i < GIVE[current].size() ; i++){
            int next = GIVE[current][i];
            if(!visited[next] && !check[next]){
                q.push(next);
                visited[next] = true;
                ans++;
            }
        }
    }
}

int main(){
    cin >> M >> N;
    for(int i = 0 ; i <  N ; i++){
        char a, b;
        cin >> a >> b;
        GIVE[a - 65].push_back(b - 65); // a 가 b 에게 줌
        GET[b - 65].push_back(a - 65); // b 가 a 에게 받음
     }
    cin >> num;
    for(int i = 0 ; i < num ; i++){
        char a;
        cin >> a;
        GIVE[a - 65].clear(); // 검거 된 놈을 마약 제공을 못함.
        check[a - 65] = true; // 검거되었음을 체크
    }
    for(int i = 0 ; i < M ; i++){
        if(GET[i].size() == 0 && GIVE[i].size() != 0 ){
            ORIGINAL.push_back(i);
            //원산지 체크
        }
    }
    for(int i = 0 ; i < ORIGINAL.size() ; i++){
        BFS(ORIGINAL[i]);
    }
    cout << ans << endl;
    return 0;
}

/*
5 4
A B
A C
B D
E C
1 E
-> 3

11 11
A B
A C
A D
A E
B F
C F
D G
E H
F I
I J
J K
2 B C
-> 4
*/