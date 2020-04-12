#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main(){
    bool check = false;
    int ans = 98765432; 
    int sum = 0;
    int M; cin >> M;
    int map[11][11] = {0};
    for(int i = 1 ; i <= M ; i++){
        for(int j = 1 ; j <= M ; j++){
            cin >> map[i][j];
        }
    }
    
    vector<int> v;
    for(int i = 1 ; i <= M ; i++){
        v.push_back(i);
    }

    sum = 0;
    v.push_back(v.front());
    for(int i = 0 ; i < v.size() - 1 ; i++){
        if(map[v[i]][v[i+1]] == 0){
            check = true;
            break;
        }
        sum += map[v[i]][v[i+1]];
    }
    if(!check) ans = sum;
    v.pop_back();

    while(next_permutation(v.begin(), v.end())){
        v.push_back(v.front());
        check = false;
        sum = 0;
        for(int i = 0 ; i < v.size() - 1 ; i++){
            if(map[v[i]][v[i+1]] == 0){
                check = true;
                break;
            }
            sum += map[v[i]][v[i+1]];
        }
        if(!check) ans = min(ans, sum);
        v.pop_back();
    }
    cout << ans << "\n";
    return 0;
}
// #include <iostream>
// #include <vector>
// #define MAX 98765432
// using namespace std;

// int M, ans = MAX;
// int startNode;
// int map[11][11];
// bool visited[11];

// vector<int> v;

// void func(int Node, int cost, int cnt){
//     if(cnt == M){
//         if(map[Node][startNode] != 0){
//             ans = min(ans, cost + map[Node][startNode]);
//             return;
//         }
//     }
//     for(int i = 1 ; i <= M ; i++){
//         if(!visited[i] && map[Node][i] != 0){
//             visited[i] = true;
//             func(i, cost + map[Node][i], cnt + 1);
//             visited[i] = false;
//         }
//     }
// }

// int main(){
//     ios_base::sync_with_stdio(0);
//     cin.tie(0);
//     cout.tie(0);

//     cin >> M;
//     for(int i = 1 ; i <= M ; i++){
//         for(int j = 1 ; j <= M ; j++){
//             cin >> map[i][j];
//         }
//     }

//     for(int i = 1 ; i <= M ; i++){
//         startNode = i;
//         visited[i] = true;
//         func(i, 0, 1);
//         visited[i] = false;    
//     }
    
//     cout << ans << "\n";
//     return 0;
// }

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