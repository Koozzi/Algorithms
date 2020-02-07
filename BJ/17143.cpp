#include <iostream>
#include <vector>
#include <vector>

using namespace std;

int R,C,M;
int map[101][101] = {0};
vector <int> v[101][101];

typedef struct{
    int loc_i, loc_j, speed, dir, size;
    bool live;
}shark;
shark sk[10001];

void moveUp(int shark_num){
    sk[shark_num].loc_i -= 1;
    if(sk[shark_num].loc_i == 1){
        sk[shark_num].dir = 2;
    }
}

void moveDown(int shark_num){
    sk[shark_num].loc_i += 1;
    if(sk[shark_num].loc_i == R){
        sk[shark_num].dir = 1;
    }    
}

void moveRight(int shark_num){
    sk[shark_num].loc_j += 1;
    if(sk[shark_num].loc_j == C){
        sk[shark_num].dir = 4;
    }
}

void moveLeft(int shark_num){
    sk[shark_num].loc_j -= 1;
    if(sk[shark_num].loc_j == 1){
        sk[shark_num].dir = 3;
    }
}

void moveShark(){
    for(int i = 1 ; i <= M ; i++){
        map[sk[i].loc_i][sk[i].loc_j] = 0;
    }
    for(int i = 1 ; i <= M ; i++){
        int speed_tmp = sk[i].speed;
        if(sk[i].live){
            if(sk[i].dir == 1){
                if(sk[i].loc_i == 1){
                    sk[i].dir = 2;
                }
                while(speed_tmp--){
                    if(sk[i].dir == 1){
                        moveUp(i);
                    }
                    else{
                        moveDown(i);
                    }
                }
                if(map[sk[i].loc_i][sk[i].loc_j] != 0){
                    if(sk[map[sk[i].loc_i][sk[i].loc_j]].size > sk[i].size){
                        sk[i].live = false;
                    }
                    else{
                        sk[map[sk[i].loc_i][sk[i].loc_j]].live = false;
                        map[sk[i].loc_i][sk[i].loc_j] = i;
                    }
                }
                else{
                    map[sk[i].loc_i][sk[i].loc_j] = i;
                }
            }
            else if(sk[i].dir == 2){
                if(sk[i].loc_i == R){
                    sk[i].dir = 1;
                }
                while(speed_tmp--){
                    if(sk[i].dir == 1){
                        moveUp(i);
                    }
                    else{
                        moveDown(i);
                    }
                }       
                if(map[sk[i].loc_i][sk[i].loc_j] != 0){
                    if(sk[map[sk[i].loc_i][sk[i].loc_j]].size > sk[i].size){
                        sk[i].live = false;
                    }
                    else{
                        sk[map[sk[i].loc_i][sk[i].loc_j]].live = false;
                        map[sk[i].loc_i][sk[i].loc_j] = i;
                    }
                }
                else{
                    map[sk[i].loc_i][sk[i].loc_j] = i;
                }  
            }
            else if(sk[i].dir == 3){
                if(sk[i].loc_j == C){
                    sk[i].dir = 4;
                }
                while(speed_tmp--){
                    if(sk[i].dir == 3){
                        moveRight(i);
                    }
                    else{
                        moveLeft(i);
                    }
                }
                if(map[sk[i].loc_i][sk[i].loc_j] != 0){
                    if(sk[map[sk[i].loc_i][sk[i].loc_j]].size > sk[i].size){
                        sk[i].live = false;
                    }
                    else{
                        sk[map[sk[i].loc_i][sk[i].loc_j]].live = false;
                        map[sk[i].loc_i][sk[i].loc_j] = i;
                    }
                }
                else{
                    map[sk[i].loc_i][sk[i].loc_j] = i;
                }
            }
            else if(sk[i].dir == 4){
                if(sk[i].loc_j == 1){
                    sk[i].dir = 3;
                }
                while(speed_tmp--){
                    if(sk[i].dir == 3){
                        moveRight(i);
                    }
                    else{
                        moveLeft(i);
                    }
                }
                if(map[sk[i].loc_i][sk[i].loc_j] != 0){
                    if(sk[map[sk[i].loc_i][sk[i].loc_j]].size > sk[i].size){
                        sk[i].live = false;
                    }
                    else{
                        sk[map[sk[i].loc_i][sk[i].loc_j]].live = false;
                        map[sk[i].loc_i][sk[i].loc_j] = i;
                    }
                }
                else{
                    map[sk[i].loc_i][sk[i].loc_j] = i;
                }
            }            
        }
    }
}

int main(){
    cin >> R >> C >> M;
    int ans = 0;
    for(int i = 1 ; i <= M ; i++){
        int r, c, s, d, z;
        cin >> r >> c >> s >> d >> z;
        map[r][c] = i;
        sk[i].loc_i = r;
        sk[i].loc_j = c;
        sk[i].speed = s;
        sk[i].dir = d;
        sk[i].size = z;
        sk[i].live = true;
    }
    vector <int> v;
    for(int j = 1 ; j <= C ; j++){
        for(int i = 1 ; i <= R ; i++){
            if(map[i][j] != 0){
                ans += sk[map[i][j]].size;
                sk[map[i][j]].live = false;
                break;
            }
        }
        moveShark();
    }
    cout << ans << "\n";
    return 0;
}

/*
1. 낚시왕 오른쪽으로 한 칸 이동
2. 가장 가까운 상어 잡기
3. 상어 움직임 
    3-1. 한 자리에는 한 마리의 상어밖에 오지 못함
    3-2. 크기가 가장 큰 상어가 그 자리에 남고 나머지 상어는 다 죽여야 함

문제를 푸는데 오래 걸리 이유
1. 문제를 제대로 안 읽음
    1-1. 낚시를 한 후에 상어가 움직임 (상어가 움직인 후에 낚시를 하는 것이 아님
    1-2. 한 자리에는 한 마리의 상어만 있을 수 있음. 크기가 가장 큰 상어만 남기고 나머지는 다 죽여야 함
2. 상어를 움직일때마다 좌표를 +- 1 를 했는데 행과 열을 헷갈렸음.
3. 상어를 죽일 때 애매하게 죽임
    3-1. 죽인 상어의 좌표를 0,0 으로 하고 스피드도 0으로 했을 때는 예제는 다 맞았지만 통과하지는 못함
    3-2. shark struct 에서 live 라는 bool 변수를 추가하고 살아있는 상어를 true, 죽은 상어를 false 로 명확하게 지정해줌 -> 통과됨
*/