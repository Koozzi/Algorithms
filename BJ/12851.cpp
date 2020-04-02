#include <iostream>
#include <vector>
#include <queue>
#include <cstring>

using namespace std;

int M, N, ans, minTime = 100001;
int costtime[100001];
int arr[100001];

void BFS(int start, int end){
    queue<pair<int, int>> q;
    q.push(make_pair(start, 0));
    costtime[start] = 0;
    while(!q.empty()){
        int c = q.front().first;
        int d = q.front().second;
        q.pop();

        if(c == end){
            arr[d]++;
            minTime = min(minTime, d);
            continue;
        }

        int n;
        n = c * 2;
        if(c != 0 && n <= 100000){
            if(d + 1 <= costtime[n]){
                q.push(make_pair(n, d + 1));
                costtime[n] = d + 1;
            }
        }

        n = c + 1;
        if(n <= 100000){
            if(d + 1 <= costtime[n]){
                q.push(make_pair(n, d + 1));
                costtime[n] = d + 1;
            }
        }

        n = c - 1;
        if(n >= 0){
            if(d + 1 <= costtime[n]){
                q.push(make_pair(n, d + 1));
                costtime[n] = d + 1;
            }
        }
    }    
}

int main(){
    cin >> M >> N;

    memset(costtime, 98765432, sizeof(costtime));

    BFS(M, N);

    cout << minTime << "\n";
    cout << arr[minTime] << "\n";
    return 0;
}