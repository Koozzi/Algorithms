#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int N, ans_cnt = -98765432;
int arr[12][12];
int qwe[13];

int num;

vector<pair<int, int>> core;
void show_arr(){
    cout << "--------------" << "\n";
    cout << num << "\n";
    for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < N ; j++){
            cout << arr[i][j] << " ";
        }cout << "\n";
    }
}
void set_line(int dir, int I, int J){
    if(dir == 0){ // 동
        for(int j = J + 1 ; j < N ; j++){
            arr[I][j] = -1;
            num++;
        }
    }
    else if(dir == 1){ // 남
        for(int i = I + 1 ; i < N ; i++){
            arr[i][J] = -1;
            num++;
        }
    }
    else if(dir == 2){ // 서
        for(int j = J - 1 ; j >= 0 ; j--){
            arr[I][j] = -1;
            num++;
        }
    }
    else{ // 북
        for(int i = I - 1 ; i >= 0 ; i--){
            arr[i][J] = -1;
            num++;
        }
    }
}
void delete_line(int dir, int I, int J){
    if(dir == 0){ // 동
        for(int j = J + 1 ; j < N ; j++){
            arr[I][j] = 0;
            num--;
        }
    }
    else if(dir == 1){ // 남
        for(int i = I + 1 ; i < N ; i++){
            arr[i][J] = 0;
            num--;
        }
    }
    else if(dir == 2){ // 서
        for(int j = J - 1 ; j >= 0 ; j--){
            arr[I][j] = 0;
            num--;
        }
    }
    else{ // 북
        for(int i = I - 1 ; i >= 0 ; i--){
            arr[i][J] = 0;
            num--;
        }
    }
}
bool is_dir_fine(int dir, int I, int J){
    if(dir == 0){ // 동
        for(int j = J + 1 ; j < N ; j++){
            if(arr[I][j] != 0) return false;
        }
    }
    else if(dir == 1){ // 남
        for(int i = I + 1 ; i < N ; i++){
            if(arr[i][J] != 0) return false;
        }
    }
    else if(dir == 2){ // 서
        for(int j = J - 1 ; j >= 0 ; j--){
            if(arr[I][j] != 0) return false;
        }
    }
    else{ // 북
        for(int i = I - 1 ; i >= 0 ; i--){
            if(arr[i][J] != 0) return false;
        }
    }
    return true;
}

void DFS(int idx, int cnt){
    if(idx == core.size()) return;

    qwe[cnt] = min(qwe[cnt], num);
    ans_cnt = max(ans_cnt, cnt);

    for(int i = idx + 1 ; i < core.size() ; i ++){
        int I = core[i].first;
        int J = core[i].second;
        for(int j = 0 ; j < 4 ; j++){
            if(is_dir_fine(j, I, J)){
                set_line(j, I, J);
                DFS(i, cnt + 1);
                delete_line(j, I, J);
            }
        }
    }
}

void _solve(){
    DFS(-1, 0);
}
void _input(){
    cin >> N;
    core.clear();
    for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < N ; j++){
            cin >> arr[i][j];
            if(arr[i][j] == 1){
                if( i == 0 || i == N-1 || j == 0 || j == N-1) continue;
                else core.push_back({i,j});
            }
        }
    }
    for(int i = 0 ; i < 13 ; i++){
        qwe[i] = 98765432;
    }
    ans_cnt = -98765432;
    num = 0;
}
void _output(int test_case){
    cout << "#" << test_case << " " << qwe[ans_cnt] << "\n";
}

int main(){
    int T; cin >> T;
    for(int t = 1 ; t <= T; t++){
        _input();
        _solve();
        _output(t);
    }
}