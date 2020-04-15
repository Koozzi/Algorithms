#include <iostream>
#include <vector>

using namespace std;

int M, N;
bool visited[2001];

vector<int> v[2001];
vector<int> ans;

void func(int node){
    if(ans.size() == 5){
        cout << 1 << "\n";
        exit(0);
    }
    for(int i = 0 ; i < v[node].size() ; i++){
        if(!visited[v[node][i]]){
            ans.push_back(v[node][i]);
            visited[v[node][i]] = true;
            func(v[node][i]);
            ans.pop_back();
            visited[v[node][i]] = false;
        }
    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cin >> M >> N;
    for(int i = 0 ; i < N ; i++){
        int a, b; cin >> a >> b;
        v[a].push_back(b);
        v[b].push_back(a);
    }

    for(int i = 0 ; i < M ; i++){
        ans.push_back(i);
        visited[i] = true;
        func(i);
        ans.pop_back();
        visited[i] = false;
    }
    cout << 0 << "\n";
    return 0;
}

// #include <iostream>
// #include <vector>

// using namespace std;

// int M, N;
// bool visited[2001];

// vector<int> v[2001];
// vector<int> ans;

// void DFS(int startNode){
//     if(ans.size() == 5){
//         cout << 1 << "\n";
//         exit(0);
//     }
//     for(int i = 0 ; i < v[startNode].size() ; i++){
//         if(!visited[v[startNode][i]]){
//             ans.push_back(v[startNode][i]);
//             visited[v[startNode][i]] = true;
//             DFS(v[startNode][i]);
//             ans.pop_back();
//             visited[v[startNode][i]] = false;
//         }
//     }
// }

// int main(){
//     cin >> M >> N;
//     for(int i = 0 ; i < N ; i++){
//         int a, b; cin >> a >> b;
//         v[a].push_back(b);
//         v[b].push_back(a);
//     }
//     for(int i = 1 ; i <= M ; i++){
//         ans.push_back(i);
//         visited[i] = true;
//         DFS(i);
//         ans.pop_back();
//         visited[i] = false;
//     }
//     cout << 0 << "\n";
//     return 0;
// }