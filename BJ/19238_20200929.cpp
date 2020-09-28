#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

int N, M, K;
int texiI, texiJ;
int map[21][21];
int person_map[21][21];
bool visit[21][21];

struct person_info{
    int personI, personJ, destI, destJ, dist, texi_dist;
    bool used;
}; person_info person[401];

struct dir{
    int moveI, moveJ;
}; dir move_dir[4] = { {0,1}, {0,-1}, {1,0}, {-1,0} };

void init(){
    for(int i = 0 ; i <= N ; i++){
        for(int j = 0 ; j <= N ; j++){
            visit[i][j] = false;
        }
    }
}

int get_distance(int startI, int startJ, int endI, int endJ){
    init();
    int distance = -1;
    queue<pair<pair<int, int>, int>> q;
    q.push({ {startI, startJ}, 0});
    visit[startI][startJ] = true;
    while(!q.empty()){
        int currentI = q.front().first.first;
        int currentJ = q.front().first.second;
        int currentD = q.front().second;

        if(currentI == endI && currentJ == endJ){
            distance = currentD;
        }

        q.pop();
        for(int i = 0 ; i < 4 ; i++){
            int nextI = currentI + move_dir[i].moveI;
            int nextJ = currentJ + move_dir[i].moveJ;
            if(nextI <= 0 || nextJ <= 0 || nextI > N || nextJ > N) continue;
            if(map[nextI][nextJ] == 0 && !visit[nextI][nextJ]){
                q.push({ {nextI, nextJ}, currentD + 1 });
                visit[nextI][nextJ] = true;
            }
        }
    }
    return distance;
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    cin >> N >> M >> K;
    for(int i = 1 ; i <= N ; i++){
        for(int j = 1 ; j <= N ; j++){
            cin >> map[i][j];
        }
    }
    cin >> texiI >> texiJ;
    for(int i = 1 ; i <= M ; i++){
        cin >> person[i].personI >> person[i].personJ >> person[i].destI >> person[i].destJ;
        person_map[person[i].personI][person[i].personJ] = i;
        person[i].dist = get_distance(person[i].personI, person[i].personJ, person[i].destI, person[i].destJ);
        if(person[i].dist == -1){
            cout << -1 << "\n";
            return 0;
        }
    }

    int cnt = 0;
    while(1){
        int min_dist = 2e9;
        for(int i = 1 ; i <= M ; i++){
            if(person[i].used) continue;
            person[i].texi_dist = get_distance(texiI, texiJ, person[i].personI, person[i].personJ);
            if(person[i].texi_dist == -1){
                cout << -1 << "\n";
                return 0;
            }
            min_dist = min(min_dist, person[i].texi_dist);
        }

        if(min_dist > K){
            cout << -1 << "\n";
            return 0;
        }

        int next_person = 0;
        bool get_out_from_loop = false;
        for(int i = 1 ; i <= N ; i++){
            for(int j = 1 ; j <= N ; j++){
                int p = person_map[i][j];
                if(p == 0) continue;
                if(person[p].used) continue;
                if(person[p].texi_dist == min_dist){
                    person[p].used = true;
                    texiI = person[p].destI;
                    texiJ = person[p].destJ;
                    next_person = p;
                    get_out_from_loop = true;
                    cnt++;
                    break;
                }
            }
            if(get_out_from_loop) break;
        }

        int total_dist = person[next_person].dist + person[next_person].texi_dist; // 손님위치->손님목적지위치 + 택시위치->손님위치

        if(total_dist > K){
            cout << -1 << "\n";
            return 0;
        }
        
        K = K - total_dist + person[next_person].dist * 2;

        if(cnt == M) break;
    }

    cout << K << "\n";
    return 0;
}

/*
내 코드는 '택시 -> 다음 손님'을 찾을 때 BFS를 반복해서 돌리기때문에 시간이 너무 오래걸린다.
BFS를 한 번만 돌려서 택시 -> 손님1, 손님2 ... 거리를 다 파악하고 
그 뒤로 다음 손님을 선택하는 것이 가장 효율적인 방법인 거 같다. 
*/

/*
6 4 100

0 0 1 0 0 0

0 0 1 0 0 0

0 0 0 0 0 0

0 0 0 0 0 0

0 0 0 0 1 0

0 0 0 1 0 0

6 5

1 6 2 2

1 6 3 5

1 6 5 4

1 6 1 1
*/