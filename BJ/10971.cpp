#include <iostream>
#include <vector>
#define MAX 98765432
using namespace std;

int M, ans = MAX;
int startNode;
int map[11][11];
bool visited[11];

vector<int> v;

void func(int Node, int cost, int cnt){
    if(cnt == M){
        if(map[Node][startNode] != 0){
            ans = min(ans, cost + map[Node][startNode]);
            return;
        }
    }
    for(int i = 1 ; i <= M ; i++){
        if(!visited[i] && map[Node][i] != 0){
            visited[i] = true;
            func(i, cost + map[Node][i], cnt + 1);
            visited[i] = false;
        }
    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> M;
    for(int i = 1 ; i <= M ; i++){
        for(int j = 1 ; j <= M ; j++){
            cin >> map[i][j];
        }
    }

    for(int i = 1 ; i <= M ; i++){
        startNode = i;
        visited[i] = true;
        func(i, 0, 1);
        visited[i] = false;    
    }
    
    cout << ans << "\n";
    return 0;
}

/*
10
0 1000000 1000000 1000000 1000000 1000000 1000000 1000000 1000000 1000000 
1000000 0 1000000 1000000 1000000 1000000 1000000 1000000 1000000 1000000 
1000000 1000000 0 1000000 1000000 1000000 1000000 1000000 1000000 1000000 
1000000 1000000 1000000 0 1000000 1000000 1000000 1000000 1000000 1000000 
1000000 1000000 1000000 1000000 0 1000000 1000000 1000000 1000000 1000000 
1000000 1000000 1000000 1000000 1000000 0 1000000 1000000 1000000 1000000 
1000000 1000000 1000000 1000000 1000000 1000000 0 1000000 1000000 1000000 
1000000 1000000 1000000 1000000 1000000 1000000 1000000 0 1000000 1000000 
1000000 1000000 1000000 1000000 1000000 1000000 1000000 1000000 0 1000000 
1000000 1000000 1000000 1000000 1000000 1000000 1000000 1000000 1000000 0 
-> 10000000


*/