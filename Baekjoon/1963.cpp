#include <iostream>
#include <queue>

using namespace std;

int start_num, end_num, found_num;
int isPrime[10000] = {0};
int depth[10000] = {0};
int num_arr[4] = {0};
bool visited[10000];

void eratos(){
    for(int i = 2 ; i * i < 10000 ; i++){
        for(int j = i * i ; j < 10000 ; j += i){
            isPrime[j] = 1;
        }
    }
}

void divide(int num){
    num_arr[0] = num / 1000;
    num_arr[1] = (num - 1000 * num_arr[0]) / 100;
    num_arr[2] = (num - 1000 * num_arr[0] - 100 * num_arr[1]) / 10;
    num_arr[3] = num - 1000 * num_arr[0] - 100 * num_arr[1] - 10 * num_arr[2];
}

int combine(){
    return 1000 * num_arr[0] + 100 * num_arr[1] + 10 * num_arr[2] + num_arr[3];
}

void BFS(int start){
    found_num = 0;
    for(int i = 0 ; i < 10000 ; i++){
        depth[i] = 0;
        visited[i] = false;
    }
    queue<int> q;
    visited[start] = true;
    q.push(start);
    while(!q.empty()){
        int current = q.front();
        q.pop();
        for(int i = 0 ; i < 4 ; i++){
            num_arr[0] = current / 1000;
            num_arr[1] = (current - 1000 * num_arr[0]) / 100;
            num_arr[2] = (current - 1000 * num_arr[0] - 100 * num_arr[1]) / 10;
            num_arr[3] = current - 1000 * num_arr[0] - 100 * num_arr[1] - 10 * num_arr[2];
            for(int j = 0 ; j < 10 ; j++){
                num_arr[i] = j;
                int next = 1000 * num_arr[0] + 100 * num_arr[1] + 10 * num_arr[2] + num_arr[3];
                if(next >= 1000 && !visited[next] && isPrime[next] != 1){
                    depth[next] += depth[current] + 1;
                    q.push(next);
                    visited[next] = true;
                    if(next == end_num){
                        found_num = 1;
                    }
                }
            }
        }
    }
}

int main(){
    eratos();
    int T;
    cin >> T;
    while(T--){
        cin >> start_num >> end_num;
        BFS(start_num);
        cout << depth[end_num] << "\n";
    }
    return 0;
}