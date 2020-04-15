#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <cstring>

using namespace std;

int T, M, N;
int check[200001];
bool visited[200001]; 

vector<int> v[200001];

void BFS(){
    memset(visited, false, sizeof(visited));
    memset(check, 0, sizeof(check));
    queue<int> q;
    q.push(1);
    visited[1] = true;
    check[1] = 1;
    while(!q.empty()){
        int c = q.front();
        q.pop();
        for(int i = 0 ; i < v[c].size() ; i++){
            int n = v[c][i];
            if(visited[n]){
                if(check[n] == check[c]){
                    cout << "NO" << "\n";
                    return;
                }
            }
            else{
                q.push(n);
                visited[n] = true;
                check[n] = check[c] * -1;
            }
        } 
    }
    cout << "YES" << "\n";
}

int main(){
    cin >> T;
    while(T--){
        cin >> M >> N;
        for(int i = 0 ; i < N ; i++){
            int a, b; cin >> a >> b;
            v[a].push_back(b);
            v[b].push_back(a);
        }
        BFS();
    }
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