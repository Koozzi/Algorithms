#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int N, original = 0, red_green = 0;
char map[101][101];
vector<char> copy_map[101];
bool visited1[101][101];
bool visited2[101][101];

typedef struct{
    int move_i, move_j;
}Dir;
Dir moveDir[4] = {{-1,0}, {1,0}, {0, 1}, {0,-1}};

void BFS1(int I, int J){
    queue<pair<int ,int>> q;
    visited1[I][J] = true;
    q.push({I,J});
    while(!q.empty()){
        int current_I = q.front().first;
        int current_J = q.front().second;
        q.pop();
        for(int i = 0 ; i < 4 ; i++){
            int next_I = current_I + moveDir[i].move_i;
            int next_J = current_J + moveDir[i].move_j;
            if(next_I >= 0 && next_I < N
            && next_J >= 0 && next_J < N
            && !visited1[next_I][next_J]
            && copy_map[next_I][next_J] == copy_map[current_I][current_J]){
                q.push({next_I, next_J});
                visited1[next_I][next_J] = true;
            }
        }
    }
}

void BFS2(int I, int J){
    queue<pair<int ,int>> q;
    visited2[I][J] = true;
    q.push({I,J});
    while(!q.empty()){
        int current_I = q.front().first;
        int current_J = q.front().second;
        q.pop();
        for(int i = 0 ; i < 4 ; i++){
            int next_I = current_I + moveDir[i].move_i;
            int next_J = current_J + moveDir[i].move_j;
            if(copy_map[current_I][current_J] == 'R'
            || copy_map[current_I][current_J] == 'G'){
                if(next_I >= 0 && next_I < N
                && next_J >= 0 && next_J < N
                && !visited2[next_I][next_J]
                && (copy_map[next_I][next_J] == 'R' 
                || copy_map[next_I][next_J] == 'G')){
                    q.push({next_I, next_J});
                    visited2[next_I][next_J] = true;
                }                
            }
            else{
                if(next_I >= 0 && next_I < N
                && next_J >= 0 && next_J < N
                && !visited2[next_I][next_J]
                && copy_map[next_I][next_J] == copy_map[current_I][current_J]){
                    q.push({next_I, next_J});
                    visited2[next_I][next_J] = true;
                }
            }

        }
    }
}

int main(){
    cin >> N;
    for(int i = 0 ; i < N ; i++){
        cin  >> map[i];
        for(int j = 0  ; j < N ; j++){
            copy_map[i].push_back(map[i][j]);
        }
    }
    for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < N ; j++){
            if(!visited1[i][j]){
                BFS1(i, j);
                original++;
            }
                
        }
    }
    for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < N ; j++){
            if(!visited2[i][j]){
                BFS2(i, j);
                red_green++;
            }
        }
    }
    cout << original << " " << red_green << "\n";
    return 0;    
}