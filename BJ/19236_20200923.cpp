#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

typedef struct{
    int I, J, Dir;
    bool eaten = false; // 안 먹힘
} fish_info;
fish_info fish[17];

typedef struct{
    int moveI, moveJ;
}Dir;
Dir moveDir[9] = {{0,0}, {-1,0}, {-1,-1}, {0,-1}, {1,-1}, {1,0}, {1,1}, {0,1}, {-1,1}};

int ans, map[4][4];
bool moved;
vector<int> v;

void show_fish(){
    cout << "-----------------\n";
    for(int i = 0 ; i < 4 ; i++){
        for(int j = 0 ; j < 4 ; j++){
            cout << map[i][j] << " ";
        }cout << "\n";
    }
    cout << "-----------------\n";
}

void change_fish(int c, int n){
    // show_fish();
    // cout << c << " " << n << "\n";
    map[fish[c].I][fish[c].J] = n;
    map[fish[n].I][fish[n].J] = c;

    int tmp = fish[c].I;
    fish[c].I = fish[n].I;
    fish[n].I = tmp;

    tmp = fish[c].J;
    fish[c].J = fish[n].J;
    fish[n].J = tmp;
}

void move_fish(){
    for(int fish_num = 1 ; fish_num <= 16 ; fish_num++){
        if(fish[fish_num].eaten) continue; // 이미 먹혔으면 이동 ㄴㄴ
        bool moved = false;
        int cnt = 0;
        while(!moved){ // 물고기가 이동할 곳이 없을 때도 고려해야함
            if(cnt == 7) break;
            if(fish[fish_num].Dir == 9) fish[fish_num].Dir = 1;
            int nextI = fish[fish_num].I + moveDir[fish[fish_num].Dir].moveI;
            int nextJ = fish[fish_num].J + moveDir[fish[fish_num].Dir].moveJ;  
            if(nextI < 0 || nextJ < 0 || nextI > 3 || nextJ > 3){
                // nextI, nextJ가 공간 밖이면 방향을 돌리고 컨티뉴
                cnt++; fish[fish_num].Dir++; continue;
            }
            if(map[nextI][nextJ] == -1 || map[nextI][nextJ] == 0){
                // nextI, nextJ에 물고기가 없거나 상어가 있으면 방향을 돌리고 컨티뉴
                cnt++; fish[fish_num].Dir++; continue;
            }
            int next_fish_num = map[nextI][nextJ];
            change_fish(fish_num, next_fish_num);
            moved = true;
        }
    }
}

bool check_shark_can_eat(int num, int I, int J, int D){
    int cnt = 0;
    while(1){
        if(cnt == 3) break;
        int nextI = I + moveDir[D].moveI;
        int nextJ = J + moveDir[D].moveJ;
        if(nextI < 0 || nextJ < 0 || nextI > 3 || nextJ > 3) break;
        int next = map[nextI][nextJ];
        if(next == num) return true;
        I = nextI; J = nextJ;
        cnt++;
    }
    return false;
}

bool check_shark_can_move(int I, int J, int D){
    while(1){
        int nextI = I + moveDir[D].moveI;
        int nextJ = J + moveDir[D].moveJ;
        if(nextI < 0 || nextJ < 0 || nextI > 3 || nextJ > 3) break;
        int next = map[nextI][nextJ];
        I = nextI; J = nextJ;
        if(next != -1) return true;
    }
    return false;
}

void shark_eat(int I, int J, int D){
    
    if(!check_shark_can_move(I, J, D) && moved){
        int sum = 0;
        for(int i = 0 ; i < v.size() ; i++){
            sum += v[i];
        }
        ans = max(ans, sum);
        return;
    }

    move_fish(); moved = true;
    
    for(int i = 1 ; i < 17 ; i++){
        if(fish[i].eaten) continue;
        if(check_shark_can_eat(i, I, J, D)){
            v.push_back(i);
            fish[i].eaten = true;
        
            map[fish[i].I][fish[i].J] = 0;
            map[I][J] = -1;
        
            shark_eat(fish[i].I, fish[i].J, fish[i].Dir);

            map[fish[i].I][fish[i].J] = i;
            map[I][J] = 0;

            fish[i].eaten = false;
            v.pop_back();
        }
    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    for(int i = 0 ; i < 4 ; i++){
        for(int j = 0 ; j < 8 ; j += 2){
            int fish_num; cin >> fish_num;
            int fish_dir; cin >> fish_dir;

            map[i][j/2] = fish_num;
            fish[fish_num].I = i;
            fish[fish_num].J = j / 2;
            fish[fish_num].Dir = fish_dir;
        }
    }

    int a = map[0][0];
    v.push_back(map[0][0]);
    fish[map[0][0]].eaten = true;
    int D = fish[map[0][0]].Dir;
    map[0][0] = 0;

    shark_eat(0,0,D);
    cout << ans << "\n";
}