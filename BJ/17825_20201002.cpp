#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int arr[10];
int score[33];
bool map_used[33];
bool arrive[4];
int horse[4];
int ans;
vector<int> v;

int map[33][6] = {
    {0, 1, 2, 3, 4, 5}, // 0
    {1, 2, 3, 4, 5, 6}, // 1
    {2, 3, 4, 5, 6, 7}, // 2
    {3, 4, 5, 6, 7, 8}, // 3
    {4, 5, 6, 7, 8, 9}, // 4
    {5, 21, 22, 23, 24, 30}, // 5
    {6, 7, 8, 9, 10, 11}, // 6
    {7, 8, 9, 10, 11, 12}, // 7
    {8, 9, 10, 11, 12, 13}, // 8
    {9, 10, 11, 12, 13, 14},
    {10, 26, 25, 24, 30, 31},
    {11, 12, 13, 14, 15, 16},
    {12, 13, 14, 15, 16, 17},
    {13, 14, 15, 16, 17, 18},
    {14, 15, 16, 17, 18, 19},
    {15, 29, 28, 27, 24, 30},
    {16, 17, 18, 19, 20, 32},
    {17, 18, 19, 20, 32, 32},
    {18, 19, 20, 32, 32, 32},
    {19, 20, 32, 32, 32, 32},
    {20, 32, 32, 32, 32, 32},
    {21, 22, 23, 24, 30, 31},
    {22, 23, 24, 30, 31, 20},
    {23, 24, 30, 31, 20, 32},
    {24, 30, 31, 20, 32, 32},
    {25, 24, 30, 31, 20, 32},
    {26, 25, 24, 30, 31, 20},
    {27, 24, 30, 31, 20, 32},
    {28, 27, 24, 30, 31, 20},
    {29, 28, 27, 24, 30, 31},
    {30, 31, 20, 32, 32, 32},
    {31, 20, 32, 32, 32, 32},
    {32, 32, 32, 32, 32, 32}
};

void set_score(){
    for(int i = 0 ; i < 21 ; i++){
        score[i] = i * 2;
    }
    score[21]=13; score[22]=16; score[23]=19;
    score[26]=22; score[25]=24;
    score[29]=28; score[28]=27; score[27]=26;
    score[24]=25; score[30]=30; score[31]=35;
}

void solve(){
    int sum = 0;
    for(int i = 0 ; i < v.size() ; i++){
        int move = arr[i]; // 얼만큼 움직일래? 
        int horse_num = v[i]; // 어떤 말이 움직이니?
        int horse_loc = horse[horse_num]; // 움직일 말의 현재 위치
        int new_horse_loc = map[horse_loc][move]; // 움직일 말의 미래 위치
        
        if(arrive[horse_num]) continue; // 움직일 말이 이미 도착한 놈이면 무시
        if(map_used[new_horse_loc]) return; // 움직일 말의 미래 위치에 다른 말이 존재하면 바로 Return
        
        map_used[horse_loc] = false; // 움직일 말의 현재 위치에서 벗어날 것이기때문에 현재 위치에 아무도 존재하지 않는다.
        if(new_horse_loc != 32){
            sum += score[new_horse_loc];
            horse[horse_num] = new_horse_loc;
            map_used[new_horse_loc] = true;
        }

    }
    ans = max(ans, sum);
}

void init(){
    for(int i = 0 ; i < 4 ; i++){
        horse[i] = 0;
        arrive[i] = false;
    }
    for(int i = 0 ; i < 33 ; i++){
        map_used[i] = false;
    }
}

void DFS(){
    if(v.size() == 10){
        init();
        solve();
        return;
    }
    for(int i = 0 ; i < 4 ; i++){
        v.push_back(i);
        DFS();
        v.pop_back();
    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    for(int i = 0 ; i < 10 ; i++){
        cin >> arr[i];
    }
    set_score();
    DFS();
    cout << ans << "\n";
}