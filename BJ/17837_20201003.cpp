#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int N, M;
vector<int> v[13][13];
int map[13][13];
int moveI[5] = { 0, 0, 0, -1, 1};
int moveJ[5] = { 0, 1, -1, 0, 0};

struct  horse{
    int I, J, D;
};
horse h[11];

void show_map(){
    cout << "\n";
    for(int i = 1 ; i <= N ; i++){
        for(int j = 1 ; j <= N ; j++){
            if(v[i][j].size() == 0){
                cout << 0 << "\t\t";
            }
            else{
                for(int k = 0 ; k < v[i][j].size() ; k++){
                    cout << v[i][j][k] << " ";
                }cout << "\t\t";
            }
        } cout << "\n";
    }
    cout << "\n";
}
void change_dir(int d, int n){
    if(d == 1){
        h[n].D = 2;
    }
    else if(d == 2){
        h[n].D = 1;
    }
    else if(d == 3){
        h[n].D = 4;
    }
    else{
        h[n].D = 3;
    }
}
bool four_horses(){
    for(int i = 1 ; i <= N ; i++){
        for(int j = 1 ; j <= N ; j++){
            if(v[i][j].size() >= 4){
                return true;
            }
        }
    }
    return false;
}

void next_move_white(int n, int I, int J, int nextI, int nextJ){
    vector<int> new_vec;
    for(int i = v[I][J].size() - 1 ; i >= 0 ; i--){
        int A = v[I][J][i];
        v[I][J].pop_back();
        new_vec.push_back(A);
        if(A == n) break;
    }

    for(int i = new_vec.size() - 1 ; i >= 0 ; i--){
        v[nextI][nextJ].push_back(new_vec[i]);
        h[new_vec[i]].I = nextI;
        h[new_vec[i]].J = nextJ;
    }
}
void next_move_red(int n, int I, int J, int nextI, int nextJ){
    vector<int> new_vec;
    for(int i = v[I][J].size() - 1 ; i >= 0 ; i--){
        int A = v[I][J][i];
        v[I][J].pop_back();
        new_vec.push_back(A);
        if(A == n) break;
    }

    for(int i = 0 ; i < new_vec.size() ; i++){
        v[nextI][nextJ].push_back(new_vec[i]);
        h[new_vec[i]].I = nextI;
        h[new_vec[i]].J = nextJ;
    }
}

void move_horses(int n){
    int I = h[n].I;
    int J = h[n].J;
    int D = h[n].D;

    int nextI = I + moveI[D];
    int nextJ = J + moveJ[D];

    if(nextI < 1 || nextJ < 1 || nextI > N || nextJ > N){ // 체스판을 나가는 경우 -> 방향만 바꿔줌
        change_dir(D, n);
        nextI = I + moveI[h[n].D];
        nextJ = J + moveJ[h[n].D];
        if(map[nextI][nextJ] == 0){
            next_move_white(n, I, J, nextI, nextJ);
        }
        else if(map[nextI][nextJ] == 1){
            next_move_red(n, I, J, nextI, nextJ);
        }
        return;
    }

    if(map[nextI][nextJ] == 2){ // 이동할 칸이 파란 칸일 경우 -> 방향만 바꿔줌
        change_dir(D, n);
        nextI = I + moveI[h[n].D];
        nextJ = J + moveJ[h[n].D];

        if(nextI >= 1 && nextJ >= 1 && nextI <= N && nextJ <= N){
            if(map[nextI][nextJ] == 0){
                next_move_white(n, I, J, nextI, nextJ);
            }
            else if(map[nextI][nextJ] == 1){
                next_move_red(n, I, J, nextI, nextJ);
            } 
        }
    } 

    else if(map[nextI][nextJ] == 0){ // 이동할 칸이 하얀 칸일 경
        next_move_white(n, I, J, nextI, nextJ);
    }

    else if(map[nextI][nextJ] == 1){ // 이동할 칸이 빨간 칸일 경우
        next_move_red(n, I, J, nextI, nextJ);
    }
}


int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    cin >> N >> M;

    for(int i = 1 ; i <= N ; i++){
        for(int j = 1 ; j <= N ; j++){
            cin >> map[i][j];
        }
    }

    for(int i = 1 ; i <= M ; i++){
        cin >> h[i].I >> h[i].J >> h[i].D;
        v[h[i].I][h[i].J].push_back(i);
    }

    if(four_horses()){
        cout << 0 << "\n";
        return 0;
    }

    int ans = 1;
    while(1){
        if(ans == 1001){
            cout << -1 << "\n";
            return 0;
        }
        for(int i = 1 ; i <= M ; i++){
            move_horses(i);   
            if(four_horses()){
                cout << ans << "\n";
                return 0;
            }
        }
        ans++;
    }
}