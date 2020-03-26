#include <iostream>
#include <queue>
#include <vector>
#include <cstring>

using namespace std;

int M, N;
int arr[100001];
bool visited[100001];
void BFS(int start){
    queue<pair<int, int>> q;
    q.push(make_pair(start, 0));
    arr[start] = 0;
    visited[start] = true;
    while(!q.empty()){
        int loca = q.front().first;
        int time = q.front().second;
        q.pop();

        if(loca == N){
            cout << arr[loca] <<  "\n";
            return;
        }

        if(loca > 0 && loca * 2 <= 100000){ // 순간이동
            if(time < arr[loca * 2]){
            // if(!visited[loca * 2]){
                q.push(make_pair(loca * 2, time));
                arr[loca * 2] = time;
                // visited[loca * 2] = true;
            }
        }

        if(loca + 1 <= 100000){ // 걷기
            if(time + 1 < arr[loca + 1]){
            // if(!visited[loca + 1]){
                q.push(make_pair(loca + 1, time + 1));
                arr[loca + 1] = time + 1;
                // visited[loca + 1] = true;
            }
        }

        if(loca - 1 >= 0){
            if(time + 1 < arr[loca - 1]){
            // if(!visited[loca - 1]){
                q.push(make_pair(loca - 1, time + 1));
                arr[loca - 1] = time + 1; 
                // visited[loca - 1] = true;
            }
        }
    }
}

int main(){
    cin >> M >> N;
    memset(arr, 98765432, sizeof(arr));
    BFS(M);
    return 0;
}

/*
2 17
-> 2

5 20
-> 0

5 19
-> 1

4 0
-> 0

4 6
-> 2


*/