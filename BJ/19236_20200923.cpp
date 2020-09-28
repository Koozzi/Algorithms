#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

struct fish_info{
    int I, J, D;
    bool Eaten;
}; fish_info Fish[17];

struct coppied_fish_info{
    int I, J, D;
    bool Eaten;
}; coppied_fish_info Coppied_Fish[17];

struct Dir{
    int moveI, moveJ;
}; 
//                           북      서북      서      서남     남     동남     동      동북 
Dir move_dir[9] = { {0,0}, {-1,0}, {-1,-1}, {0,-1}, {1,-1}, {1,0}, {1,1}, {0,1}, {-1,1}};

int ans, map[4][4];
int SharkI, SharkJ, SharkD;

vector<int> Eat;

void show_map(){
    cout << "\n";
    for(int i = 0 ; i < 4 ; i++){
        for(int j = 0 ; j < 4 ; j++){
            int n = map[i][j];
            if(n == 0 || n == -1){
                cout << n << "\t";
                continue;
            }
            int d = Fish[n].D;
            cout << map[i][j];
             // ↖, ←, ↙, ↓, ↘, →, ↗ 
            if(d == 1) cout << "↑";
            else if(d == 2) cout << "↖";
            else if(d == 3) cout << "←";
            else if(d == 4) cout << "↙";
            else if(d == 5) cout << "↓";
            else if(d == 6) cout << "↘";
            else if(d == 7) cout << "→";
            else cout << "↗";
            cout << "\t";
        }cout << "\n";
    }
    cout << "\n";
}
void move_fish(){
    for(int i = 1 ; i <= 16 ; i++){
        if(Fish[i].Eaten) continue;
        int change_dir_cnt = 0;
        int I = Fish[i].I;
        int J = Fish[i].J;
        int D = Fish[i].D;
        while(change_dir_cnt < 8){
            if(Fish[i].D > 8) Fish[i].D = 1;
            int nextI = Fish[i].I + move_dir[Fish[i].D].moveI;
            int nextJ = Fish[i].J + move_dir[Fish[i].D].moveJ;
        
            if(nextI < 0 || nextJ < 0 || nextI > 3 || nextJ > 3){
                change_dir_cnt++;
                Fish[i].D++;
                continue;
            }

            if(nextI == SharkI && nextJ == SharkJ){ // 먹혔거나 상어가 있을 때 
                change_dir_cnt++;
                Fish[i].D++;
                continue;
            }
            
            int nextF = map[nextI][nextJ];
            int nextD = Fish[nextF].D;

            if(nextF == 0){
                map[I][J] = 0;
                map[nextI][nextJ] = i;
                Fish[i].I = nextI;
                Fish[i].J = nextJ;
                break;
            }

            Fish[i].I = nextI;
            Fish[i].J = nextJ;

            Fish[nextF].I = I;
            Fish[nextF].J = J;

            map[I][J] = nextF;
            map[nextI][nextJ] = i;
            break;
        }
    }
}
vector<int> check_shark_can_eat(int I, int J, int D){
    vector<int> v;
    while(1){
        int nextI = I + move_dir[D].moveI;
        int nextJ = J + move_dir[D].moveJ;

        I = nextI;
        J = nextJ;

        if(nextI <  0 || nextJ < 0 || nextI > 3 || nextJ > 3) break;
        if(map[nextI][nextJ] == 0 || map[nextI][nextJ] == -1) continue;
        
        v.push_back(map[nextI][nextJ]);
    }
    return v;
}

void show_dir(int d){
            if(d == 1) cout << "↑";
            else if(d == 2) cout << "↖";
            else if(d == 3) cout << "←";
            else if(d == 4) cout << "↙";
            else if(d == 5) cout << "↓";
            else if(d == 6) cout << "↘";
            else if(d == 7) cout << "→";
            else cout << "↗";
}

void solve(int num, int sum){
    sum += num;
    ans = max(ans, sum);

    int I = Fish[num].I;
    int J = Fish[num].J;
    int D = Fish[num].D;
    Fish[num].Eaten = true;

    map[I][J] = 0;

    // printf("%d을 먹고 현재 위치는 (%d, %d) 방향은 ", num, I, J);
    // show_dir(D);
    // cout << "\n";
    // show_map();

    // for(int i = 1 ; i < 17; i++){
    //     if(!Fish[i].Eaten){
    //         printf("%d의 위치 : (%d, %d)\n", i, Fish[i].I, Fish[i].J);
    //     }
    // }

    SharkI = I;
    SharkJ = J;
    SharkD = D;

    move_fish();
    // printf("상어가 %d번 물고기를 먹고 다른 물고기들이 움직인 후\n", num);
    // show_map();

    vector<int> v = check_shark_can_eat(I, J, D);
    if(v.size() == 0){
        // printf("상어가 움직일 수 있는 곳 없음\n");
        // for(int i = 0 ; i < Eat.size() ; i++){
        //     cout << Eat[i] << " ";
        // }cout << "\n";
        // cout << ans << "\n";
        return;
    }
    // else{
    //     cout << "상어가 갈 수 있는 곳 ->  ";
    //     for(int i = 0 ;  i < v.size() ; i++){
    //         cout << v[i] << " ";
    //     }cout << "\n";
    //     cout << "\n";
    // }

    // printf("상어의 위치 : (%d, %d)\n", SharkI, SharkJ);
    // printf("%d의 위치 : (%d, %d)\n", num, I, J);
    // printf("Ans : %d\n", ans);

    int coppied_map[4][4];
    for(int i = 0 ; i < 4; i++){
        for(int j = 0 ; j < 4 ; j++){
            coppied_map[i][j] = map[i][j];
        }
    }

    vector<pair<pair<int, int>, pair<int, bool>>> copied(17);
    for(int i = 1 ; i < 17 ; i++){
        copied[i].first.first = Fish[i].I;
        copied[i].first.second = Fish[i].J;
        copied[i].second.first = Fish[i].D;
        copied[i].second.second = Fish[i].Eaten;
    }

    
    // for(int i = 0 ; i < v.size() ; i++){
    //     cout << v[i] << " ";
    // }cout << "\n";

    for(int i = 0 ; i < v.size() ; i++){
        int nextF = v[i];
        Eat.push_back(nextF);
        solve(nextF, sum);
        Eat.pop_back();
        SharkI = I;
        SharkJ = J;
        SharkD = D;

        for(int j = 0 ; j < 4 ; j++){
            for(int k = 0 ; k < 4 ; k++){
                map[j][k] = coppied_map[j][k];
            }
        }

        for(int j = 1 ; j < 17 ; j++){
            Fish[j].I = copied[j].first.first;
            Fish[j].J = copied[j].first.second;
            Fish[j].D = copied[j].second.first;
            Fish[j].Eaten = copied[j].second.second;
        }
    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    for(int i = 0 ; i < 4 ; i ++){
        for(int j = 0 ; j < 4 ; j++){
            int a, b; cin >> a >> b;
            map[i][j] = a;
            Fish[a].I = i;
            Fish[a].J = j;
            Fish[a].D = b;
        }
    }
    // show_map();
    Eat.push_back(map[0][0]);
    solve(map[0][0], 0);
    cout << ans << "\n";
}