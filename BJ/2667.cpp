#include <algorithm>
#include <vector>
#include <iostream>
#include <queue>
#define MAX_SIZE 26
using namespace std;

int count_house[MAX_SIZE * MAX_SIZE];
int map[MAX_SIZE][MAX_SIZE];
bool visited[MAX_SIZE][MAX_SIZE];
char input_data[MAX_SIZE][MAX_SIZE];

int map_size;
int cnt = 0;
typedef struct{
    int map_i, map_j;
}Dir;
Dir moveDir[4] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

void BFS(int I, int J){
    queue<pair<int, int>> q;
    cnt++;
    q.push({I,J});
    visited[I][J] = true;
    count_house[cnt]++;
    while(!q.empty()){
        int MAP_I = q.front().first;
        int MAP_J = q.front().second;
        q.pop();
        for(int i = 0 ; i < 4 ; i++){
            int NEXT_I = MAP_I + moveDir[i].map_i;
            int NEXT_J = MAP_J + moveDir[i].map_j;
            if(NEXT_I >= 0 && NEXT_I < map_size
            && NEXT_J >= 0 && NEXT_J < map_size
            && (!visited[NEXT_I][NEXT_J])
            && map[NEXT_I][NEXT_J] == 1){
                q.push({NEXT_I, NEXT_J});
                visited[NEXT_I][NEXT_J] = true;
                count_house[cnt]++;
            }
        }
    }
}

int main(){
    cin >> map_size;
    for(int i = 0 ; i < map_size ; i++){
        cin >> input_data[i];
        for(int j = 0 ; j < map_size ; j++){
            map[i][j] = int(input_data[i][j]) - 48;
            visited[i][j] = false;
        }
    }

    for(int i = 0 ; i < map_size ; i++){
        for(int j = 0 ; j < map_size ; j++){
            if(!visited[i][j] && map[i][j] == 1){
                BFS(i, j);
            }
        }
    }
    cout << cnt << "\n";
    sort(count_house+1, count_house+cnt+1);
    for(int i = 1 ; i < cnt+1 ; i++){
        cout << count_house[i] << "\n";
    }
}

/* 처음에 count_house 의 크기를 26으로 설정했다. 
당연히 틀렸습니다. 라는 결과가 나왔고
count_house 의 크기를 26 * 26 으로 설정했더니 통과하였다.
배열 크기 설정을 매우 잘 해야 할 듯.
아니면 vector 를 사용하든가.
 */