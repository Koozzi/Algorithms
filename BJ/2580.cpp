#include <iostream>
#include <cstring>
#include <vector>
using namespace std;

int map[9][9];
int zeroCount;
vector<pair<int, int>> zeroLocation;
vector<int> possibleNum[81];
void showAns(){
    for(int i = 0 ; i < 9 ; i++){
        for(int j = 0 ; j < 9 ; j++){
            cout << map[i][j] << " ";
        }cout << endl;
    }
}
bool isEnd(){
    bool checkNum[10];
    for(int i = 0 ; i < 9 ; i++){
        memset(checkNum, false, sizeof(checkNum));
        for(int j = 0 ; j < 9 ; j++){
            if(map[i][j] == 0){
                return false;
            }
            if(!checkNum[map[i][j]]){
                checkNum[map[i][j]] = true;
                continue;
            }
            else{
                return false;
            }
        }
    }
    return true;
}
void fineNum(int I, int J, int idx){
    bool checkNum[10];
    memset(checkNum, true, sizeof(checkNum));
    // 가로 줄
    for(int i = 0 ; i < 9 ; i++){
        if(map[I][i] != 0){
            if(checkNum[map[I][i]]){
                checkNum[map[I][i]] = false;
            }
        }
    }
    // 세로 중
    for(int i = 0 ; i < 9 ; i++){
        if(map[i][J] != 0){
            if(checkNum[map[i][J]]){
                checkNum[map[i][J]] = false;
            }
        }
    }

    // 3.3 정사각형
    if(I < 3){
        if(J < 3){
            for(int i = 0 ; i < 3 ; i++){
                for(int j = 0 ; j < 3 ; j++){
                    if(map[i][j] != 0){
                        if(checkNum[map[i][j]]){
                            checkNum[map[i][j]] = false;
                        }
                    }
                }
            }
        }
        else if(J > 2 && J < 6){
            for(int i = 0 ; i < 3 ; i++){
                for(int j = 3 ; j < 6 ; j++){
                    if(map[i][j] != 0){
                        if(checkNum[map[i][j]]){
                            checkNum[map[i][j]] = false;
                        }
                    }
                }
            }
        }
        else{
            for(int i = 0 ; i < 3 ; i++){
                for(int j = 6 ; j < 9 ; j++){
                    if(map[i][j] != 0){
                        if(checkNum[map[i][j]]){
                            checkNum[map[i][j]] = false;
                        }
                    }
                }
            }
        }
    }
    else if(I > 2 && I < 6){ // 4,
        if(J < 3){
            for(int i = 3 ; i < 6 ; i++){
                for(int j = 0 ; j < 3 ; j++){
                    if(map[i][j] != 0){
                        if(checkNum[map[i][j]]){
                            checkNum[map[i][j]] = false;
                        }
                    }
                }
            }
        }
        else if(J > 2 && J < 6){
            for(int i = 3 ; i < 6 ; i++){
                for(int j = 3 ; j < 6 ; j++){
                    if(map[i][j] != 0){
                        if(checkNum[map[i][j]]){
                            checkNum[map[i][j]] = false;
                        }
                    }
                }
            }
        }
        else{
            for(int i = 3 ; i < 6 ; i++){
                for(int j = 6 ; j < 9 ; j++){
                    if(map[i][j] != 0){
                        if(checkNum[map[i][j]]){
                            checkNum[map[i][j]] = false;
                        }
                    }
                }
            }            
        }
    }
    else{
        if(J < 3){
            for(int i = 6 ; i < 9 ; i++){
                for(int j = 0 ; j < 3 ; j++){
                    if(map[i][j] != 0){
                        if(checkNum[map[i][j]]){
                            checkNum[map[i][j]] = false;
                        }
                    }
                }
            }
        }
        else if(J > 2 && J < 6){
            for(int i = 6 ; i < 9 ; i++){
                for(int j = 3 ; j < 6 ; j++){
                    if(map[i][j] != 0){
                        if(checkNum[map[i][j]]){
                            checkNum[map[i][j]] = false;
                        }
                    }
                }
            }
        }
        else{
            for(int i = 6 ; i < 9 ; i++){
                for(int j = 6 ; j < 9 ; j++){
                    if(map[i][j] != 0){
                        if(checkNum[map[i][j]]){
                            checkNum[map[i][j]] = false;
                        }
                    }
                }
            }            
        }
    }
    for(int i = 1 ; i < 10 ; i++){
        if(checkNum[i]){
            possibleNum[idx].push_back(i);
            checkNum[i] = false;
        }
    }
    if(possibleNum[idx].size() == 1){
        map[I][J] = possibleNum[idx][0];
        return;
    }
}
void sudoku(int I, int J, int cnt){
    if(cnt == zeroLocation.size() - 1){
        if(isEnd()){
            cout << endl;
            showAns();
            exit(0);
        }
    }
    else{
        for(int i = cnt + 1 ; i < zeroLocation.size() ; i++){
            int nextI = zeroLocation[i].first;
            int nextJ = zeroLocation[i].second;
            for(int j = 0 ; j < possibleNum[i].size() ; j++){
                map[nextI][nextJ] = possibleNum[i][j];
                sudoku(nextI, nextJ, i);
            }
        }
    }
}
int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    for(int i = 0 ; i < 9 ; i++){
        for(int j = 0 ; j < 9 ; j++){
            cin >> map[i][j];
            if(map[i][j] == 0){
                zeroLocation.push_back(make_pair(i,j));
            }
        }
    }

    if(zeroLocation.size() == 0){
        cout << endl;
        showAns();
        return 0;
    }

    for(int i = 0 ; i < zeroLocation.size() ; i++){
        fineNum(zeroLocation[i].first, zeroLocation[i].second, i);
    }

    for(int i = 0 ; i < possibleNum[0].size() ; i++){
        map[zeroLocation[0].first][zeroLocation[0].second] = possibleNum[0][i];
        sudoku(zeroLocation[0].first, zeroLocation[0].second, 0);
    }
    return 0;
}


/*
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0

1 2 3 4 5 6 7 8 9 
4 5 6 7 8 9 1 2 3 
7 8 9 1 2 3 4 5 6 
2 1 4 3 6 5 8 9 7 
3 6 5 8 9 7 2 1 4 
8 9 7 2 1 4 3 6 5 
5 3 1 6 4 2 9 7 8 
6 4 2 9 7 8 5 3 1 
9 7 8 5 3 1 6 4 2

-----------------
*/