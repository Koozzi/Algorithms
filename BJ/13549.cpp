#include <iostream>
#include <queue>

using namespace std;

int M, N;
int Time[100001];

void BFS(){
    queue<pair<int, int>> q;
    q.push({M, 0});
    Time[M] = 0;
    while(!q.empty()){
        int c = q.front().first; 
        int d = q.front().second;
        q.pop();

        if(c == N){
            cout << Time[c] << "\n";
            return;
        }

        if(c > 0 && c * 2 <= 100000){
            if(d < Time[c * 2]){
                q.push({c * 2, d});
                Time[c * 2] = d;
            }
        }

        if(c + 1 <= 100000){
            if(d + 1 < Time[c + 1]){
                q.push({c + 1, d + 1});
                Time[c + 1] = d + 1;
            }            
        }

        if(c - 1 >= 0){
            if(d + 1 < Time[c - 1]){
                q.push({c - 1, d + 1});
                Time[c - 1] = d + 1;
            }
        }
    }
}

int main(){
    cin >> M >> N;
    for(int i = 0 ; i <= 100000 ; i++){
        Time[i] = 98765432;
    }
    BFS();
    return 0;
}

// #include <iostream>
// #include <queue>
// #include <vector>
// #include <cstring>

// using namespace std;

// int M, N;
// int arr[100001];
// bool visited[100001];

// void BFS(int start){
//     queue<pair<int, int>> q;
//     q.push(make_pair(start, 0));
//     arr[start] = 0;

//     while(!q.empty()){
//         int loca = q.front().first;
//         int time = q.front().second;
//         q.pop();

//         if(loca == N){
//             cout << arr[loca] <<  "\n";
//             return;
//         }

//         if(loca > 0 && loca * 2 <= 100000){ // 순간이동
//             if(time < arr[loca * 2]){
//                 q.push(make_pair(loca * 2, time));
//                 arr[loca * 2] = time;
//             }
//         }

//         if(loca + 1 <= 100000){ // 오른쪽 걷기
//             if(time + 1 < arr[loca + 1]){
//                 q.push(make_pair(loca + 1, time + 1));
//                 arr[loca + 1] = time + 1;
//             }
//         }

//         if(loca - 1 >= 0){ // 왼쪽 걷기
//             if(time + 1 < arr[loca - 1]){
//                 q.push(make_pair(loca - 1, time + 1));
//                 arr[loca - 1] = time + 1; 
//             }
//         }
//     }
// }

// int main(){
//     cin >> M >> N;
//     memset(arr, 98765432, sizeof(arr));
//     BFS(M);
//     return 0;
// }

// /*
// 2 17
// -> 2

// 5 20
// -> 0

// 5 19
// -> 1

// 4 0
// -> 0

// 4 6
// -> 2


// */