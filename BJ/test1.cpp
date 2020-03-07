#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int M, N, H, CNT;
int appendCnt = 0;
int ans = 4;
bool check;
int map[31][11];
bool Tlqkf[31][11];
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
        if(I == M+1){
            if(J == start){
                return true;
            }
            else{
                return false;
            }
        }
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
    }
}
void CHECK(){
    for(int i = 1 ; i < N ; i++){
        if(!move(i)){
            return;
        }
    }
    // cout << appendCnt << endl;
    ans = min(ans, appendCnt);
    // exit(0);
    // return;
}
void ladder(){
    for(int i = 1 ; i <= M ; i++){
        for(int j = 1 ; j < N ;){
            if(map[i][j] == 0){
                if(map[i][j+1] == 0){
                    if(!Tlqkf[i][j]){
                        map[i][j] = 1;
                        appendCnt++;
                        CHECK();
                        if(appendCnt < 3) ladder();
                        map[i][j] = 0;
                        appendCnt--;
                    }
                    j++;
                }
                else{
                    j+=3;
                }
            }
            else{
                if(map[i][j] == 1){
                    j+=2;
                }
                else{
                j++;
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
    CHECK();
    if(ans == 0){
        cout << 0 << "\n";
        return 0;
    }
    for(int i = 1 ; i <= M ; i++){
        for(int j = 1 ; j < N ;){
            if(map[i][j] == 0){
                if(map[i][j+1] == 0){
                    Tlqkf[i][j] = true;
                    map[i][j] = 1;
                    appendCnt++;
                    CHECK();
                    ladder();
                    map[i][j] = 0;
                    appendCnt--;
                    j++;
                }
                else{
                        j+=3;
                    }
            }
            else{
                if(map[i][j] == 1){
                    j+=2;
                }  
                else{
                    j++;
                }
            }
        }
    }
    if(ans == 4){
        cout << -1 << "\n";    
    }
    else{
        cout << ans << "\n";
    }
    return 0;
}