#include <iostream>
#include <vector>
#include <algorithm>
#include <deque>
#include <cmath>
#include <stdio.h>

using namespace std;

int M, N, ans = 0;

int map[500][500];

vector<pair<int, int>> v;

deque<pair<int, int>> dq;



void rotate(int startI, int startJ){
    int sum = 0;
    for(int i = 0 ; i < 4 ; i++){
        int moveI = (startJ - dq.front().second);
        int moveJ = (startI - dq.front().first);
        dq.push_back(make_pair(startI - moveI, startJ + moveJ));
        dq.pop_front();
    }
    for(int i = 0 ; i < 4 ; i++){
        int I = dq[i].first;
        int J = dq[i].second;
        if(I >= 0 && I < M && J >= 0 && J < N){
            sum += map[I][J];
        }
        else{
            return;
        }
    }
    ans = max(ans, sum);
}

void flip(int startI, int startJ){
    for(int i = 0 ; i < 4; i++){
    dq.push_back(make_pair(startI - (dq.front().first - startI) , dq.front().second));
    dq.pop_front();}
}

void solve(int startI, int startJ){
    for(int i = 0 ; i < 4; i++){
        rotate(startI, startJ);
    }    
    flip(startI, startJ);
    for(int i = 0 ; i < 4 ; i++){
        rotate(startI, startJ);
    }
}

void tet1(int startI, int startJ){
    dq.push_back(make_pair(startI, startJ));
    dq.push_back(make_pair(startI, startJ + 1));
    dq.push_back(make_pair(startI + 1, startJ));
    dq.push_back(make_pair(startI + 1, startJ + 1));
    solve(startI, startJ);
}

void tet2(int startI, int startJ){
    dq.push_back(make_pair(startI, startJ));
    dq.push_back(make_pair(startI, startJ + 1));
    dq.push_back(make_pair(startI, startJ + 2));
    dq.push_back(make_pair(startI, startJ + 3));
    solve(startI, startJ);
}

void tet3(int startI, int startJ){
    dq.push_back(make_pair(startI, startJ));
    dq.push_back(make_pair(startI + 1, startJ));
    dq.push_back(make_pair(startI + 2, startJ));
    dq.push_back(make_pair(startI + 2, startJ + 1));
    solve(startI, startJ);
}

void tet4(int startI, int startJ){
    dq.push_back(make_pair(startI, startJ));
    dq.push_back(make_pair(startI + 1, startJ));
    dq.push_back(make_pair(startI + 1, startJ + 1));
    dq.push_back(make_pair(startI + 2, startJ + 1));
    solve(startI, startJ);
}

void tet5(int startI, int startJ){
    dq.push_back(make_pair(startI, startJ));
    dq.push_back(make_pair(startI, startJ + 1));
    dq.push_back(make_pair(startI, startJ + 2));
    dq.push_back(make_pair(startI + 1, startJ + 1));
    solve(startI, startJ);
}

int main(){
    cin >> M >> N;
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < N ; j++){
            cin >> map[i][j];
        }
    }
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < N ; j++){
            tet1(i,j);
            dq.clear();
            tet2(i,j);
            dq.clear();
            tet3(i,j);
            dq.clear();
            tet4(i,j);
            dq.clear();
            tet5(i,j);
            dq.clear();
        }
    }
    cout << ans << "\n";
    return 0;
}
