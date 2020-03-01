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
        cout << dq[0].first << "," << dq[0].second << "/";
    cout << dq[1].first << "," << dq[1].second << "/";
    cout << dq[2].first << "," << dq[2].second << "/";
    cout << dq[3].first << "," << dq[3].second << "\n";
    for(int i = 0 ; i < 4 ; i++){
        int moveI = (dq.front().first - startI);
        int moveJ = (dq.front().second - startJ);
        dq.push_back(make_pair(startI + moveJ, startJ - moveI));
        // printf("기준점 : (%d, %d) / (%d, %d) -> (%d, %d)\n", startI, startJ, dq.front().first, dq.front().second, startI + moveJ, startJ - moveI);
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

    cout << dq[0].first << "," << dq[0].second << "/";
    cout << dq[1].first << "," << dq[1].second << "/";
    cout << dq[2].first << "," << dq[2].second << "/";
    cout << dq[3].first << "," << dq[3].second << "\n";
    cout << ans << "\n";
    cout << "--------" << "\n";
    ans = max(ans, sum);
}

void flip(int startI, int startJ){
    for(int i = 0 ; i < 4 ; i++){
        int I = startI - (dq.front().first - startI);
        int J = startJ;
        dq.push_back(make_pair(I,J));
        dq.pop_front();
    }
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
            tet2(i,j);
            tet3(i,j);
            tet4(i,j);
            tet5(i,j);
        }
    }
    cout << ans << "\n";
    return 0;
}
