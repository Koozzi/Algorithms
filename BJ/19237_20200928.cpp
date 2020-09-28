#include <iostream>
#include <algorithm>

using namespace std;

struct Dir{
    int moveI, moveJ;
};
Dir move_dir[5] = { {0,0}, {-1,0}, {1,0}, {0,-1}, {0,1} };

struct Shark_info{
    int I, J, D;
    int arr[5][5];
    bool dead;
};
Shark_info Shark[401];



int N, M, K;
int death_cnt;
int map[20][20][3];

void show_map(){
    cout << "\n";
    for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < N ; j++){
            printf("%d,%d,%d\t\t", map[i][j][0], map[i][j][1], map[i][j][2]);
        }cout << "\n";
    }
    cout << "\n";
}

void fish_move(){
    for(int i = 1 ; i <= M ; i++){
        if(Shark[i].dead) continue;
        int I = Shark[i].I;
        int J = Shark[i].J;
        int D = Shark[i].D;
        bool moved = false;
        for(int j = 1 ; j <= 4 ; j++){ // 빈칸이 있으면 빈칸으로 움직이자.
            int dir = Shark[i].arr[D][j];
            int nextI = I + move_dir[dir].moveI;
            int nextJ = J + move_dir[dir].moveJ;
            if(nextI < 0 || nextJ < 0 || nextI >= N || nextJ >= N) continue;

            if(map[nextI][nextJ][2] == 0){
                Shark[i].I = nextI;
                Shark[i].J = nextJ;
                Shark[i].D = dir;
                moved = true;
                map[I][J][0] = 0;
                break;
            }
        }
            
        if(!moved){ // 빈칸으로 움직이지 못했으면 자기 냄새로 가야함.
            for(int j = 1 ; j <= 4 ; j++){
                int dir = Shark[i].arr[D][j];
                int nextI = I + move_dir[dir].moveI;
                int nextJ = J + move_dir[dir].moveJ;
                if(nextI < 0 || nextJ < 0 || nextI >= N || nextJ >= N) continue;
                if(map[nextI][nextJ][1] == i){
                    Shark[i].I = nextI;
                    Shark[i].J = nextJ;
                    Shark[i].D = dir;
                    map[I][J][0] = 0;
                    break;
                }
            }
        }        
    }
}

void check_same_position(){
    for(int i = 1 ; i <= M ; i++){
        if(Shark[i].dead) continue;
        int I = Shark[i].I;
        int J = Shark[i].J;
        if(map[I][J][0] == 0){
            map[I][J][0] = i;
            map[I][J][1] = i;
            map[I][J][2] = K+1;
        }
        else{
            if(map[I][J][0] < i){
                Shark[i].dead = true;
                death_cnt++;
            }
            else{
                Shark[map[I][J][0]].dead = true;
                death_cnt++;
                map[I][J][0] = i;
                map[I][J][1] = i;
                map[I][J][2] = K+1;
            }
        }
    }
}

void decrease_smell_cnt(){
    for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < N ; j++){
            if(map[i][j][2] != 0){
                map[i][j][2]--;
            }
            if(map[i][j][2] == 0){
                map[i][j][1] = 0;
            }
        }
    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    cin >> N >> M >> K;
    for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < N ; j++){
            int a; cin >> a;
            map[i][j][0] = a;
            if(a != 0){
                map[i][j][1] = a;
                map[i][j][2] = K;
                Shark[a].I = i;
                Shark[a].J = j;
            }
        }
    }
    for(int i = 1 ; i <= M ; i++){
        int a; cin >> a;
        Shark[i].D = a;
    }

    for(int i = 1 ; i <= M ; i++){
        for(int j = 1 ; j <= 4 ; j++){
            for(int k = 1 ; k <= 4 ; k++){
                int a; cin >> a;
                Shark[i].arr[j][k] = a;
            }
        }
    }

    int ans = 0;
    while(1){
        fish_move();
        check_same_position();
        decrease_smell_cnt();        
        // show_map();
        ans++;
        
        if(death_cnt == M-1 && ans <= 1000){
            cout << ans << "\n";
            return 0;
        }
        if(ans > 1000){
            cout << -1 << "\n";
            return 0;
        }
        
    }
}