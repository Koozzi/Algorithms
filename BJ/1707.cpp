#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <cstring>

using namespace std;

int T, M, N;
bool flag;
int visited[20001]; 

vector<int> v[20001];

void BFS(int start){
    queue<int> q;
    q.push(start);
    visited[start] = 1;
    while(!q.empty()){
        int c = q.front();
        q.pop();
        for(int i = 0 ; i < v[c].size() ; i++){
            int n = v[c][i];
            if(visited[n] != 0){
                if(visited[n] == visited[c]){
                    cout << "NO" << "\n";
                    flag = false;
                    return;
                }
            }
            else{
                q.push(n);
                visited[n] = visited[c] * -1;
            }
        } 
    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cin >> T;
    while(T--){
        memset(visited, 0, sizeof(visited));
        cin >> M >> N;
        flag = true;
        for(int i = 0 ; i < N ; i++){
            int a, b; cin >> a >> b;
            v[a].push_back(b);
            v[b].push_back(a);
        }
        for(int i = 1 ; i <= M ; i++){
            if(visited[i] == 0 && flag){
                BFS(i);
            }
        }

        if(flag) cout << "YES" << "\n";

        for(int i = 1 ; i <= M ; i++){
            v[i].clear();
        }
    }
    return 0;
}

// #include <iostream>
// #include <queue>
// #include <vector>
// #include <cstring>

// using namespace std;

// int T, M, N, A, B;
// bool flag = false;
// vector<int> v[20001];

// int visited[20001];
// int bipartite[20001];

// void show(){
//     cout << "Bipartite" << endl;
//     for(int i = 1 ; i <= M ; i ++){
//         cout << bipartite[i] << " ";
//     }cout << endl;
// }

// void BFS(int start){
//     queue<int> q;
//     q.push(start);
//     visited[start] = 1;
//     while(!q.empty()){
//         int c = q.front();
//         q.pop();
//         for(int i = 0 ; i < v[c].size() ; i++){
//             int n = v[c][i];
//             if(visited[n] == visited[c]){
//                 cout << "NO" << endl;
//                 flag = true;
//                 return;
//             }
//             else{
//                 if(visited[n] == 0){
//                     q.push(n);
//                     visited[n] = visited[c] * -1;
//                 }
//             }
//         }
//     }
// }


// int main(){
//     ios_base::sync_with_stdio(0);
//     cin.tie(0);
//     cin >> T;
//     while(T--){
//         memset(visited, false, sizeof(visited));
//         flag = false;
//         cin >> M >> N;
//         for(int i = 0 ; i < N ; i++){
//             cin >> A >> B;
//             v[A].push_back(B);
//             v[B].push_back(A);
//         }
//         for(int i = 1 ; i <= M ; i++){
//             if(!flag && visited[i] == 0){
//                 BFS(i);
//             }
//         }
//         if(!flag){
//             cout << "YES" << endl;
//         }
//         for(int i = 0 ; i <= M ; i++){
//             v[i].clear();
//         }
//     }
//     return 0;
// }