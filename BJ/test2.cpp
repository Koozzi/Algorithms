#include <iostream>
#include <vector>
using namespace std;

int M, N, H, CNT;
int appendCnt = 0;
int ans;
bool check;
int map[31][11];

void show(){
    cout << endl;
    for(int i = 1 ; i <= M ; i++){
        for(int j = 1 ; j <= N ; j++){
            cout << map[i][j] << " ";
        }cout << endl;
    }
}
bool move(int start){
    int I = 1;
    int J = start;
    while(1){
        if(map[I][J] == 1){
            I++;
            J++;
        }
        else if(map[I][J] == 0){
            if(map[I][J-1] == 1){
                I++;
                J--;
            }
            else{
                I++;
            }
        }
        if(I == M+1){
            if(J == start){
                return true;
            }
            else{
                return false;
            }
        }
    }
}
bool CHECK(){
    int cnt = 0;
    for(int i = 1 ; i <= N ; i++){
        if(move(i)){
            cnt++;
        }
    }
    if(cnt == N){
        return true;
    }
    else{
        return false;
    }
}

void ladder(){
    if(appendCnt == 1){
        if(CHECK()){
            check = true;
            ans = appendCnt;
            return;
        }
    }
    else{
    for(int i = 1 ; i <= M ; i++){
        for(int j = 1 ; j < N ; j++){
            if(map[i][j] == 0){
                if(map[i][j+1] == 0){
                    map[i][j] = 1;
                    appendCnt++;
                    if(CHECK()){
                        ans = appendCnt;
                        check = true;
                        return;
                    }
                    ladder();
                    map[i][j] = 0;
                    appendCnt--;
                }
            }
        }
    }
    }
}
int main(){
    cin >> N >> H >> M;
    for(int i = 0 ; i < H ; i++){
        int a, b;
        cin >> a >> b;
        map[a][b] = 1;
    }
    if(CHECK()){
        cout << 0 << "\n";
        return 0;
    }
    for(CNT = 1 ; CNT <= 3 ; CNT++){
        for(int i = 1 ; i <= M ; i++){
            for(int j = 1 ; j < N ; j++){
                if(map[i][j] == 0){
                    if(map[i][j+1] == 0){
                        map[i][j] = 1;
                        appendCnt++;
                        if(CHECK()){
                            cout << appendCnt << endl;
                            return 0;
                        }
                        ladder();
                        map[i][j] = 0;
                        appendCnt--;
                    }
                }
            }
        }
    }
    if(!check){
        cout << -1 << "\n";
    }
    else{
        cout << ans << endl;
    }
    return 0;
}