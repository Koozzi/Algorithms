#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <stdio.h>

using namespace std;

int M, N, cnt, ans = 9999;

int map[50][50];
int cmap[50][50];

vector<pair<int ,int>> chicken;
vector<pair<int ,int>> deleteC;
vector<pair<int, int>> house;

void getDist(){
    int hcDist, totalDist = 0;
    for(int h = 0 ; h < house.size() ; h++){
        hcDist = 10000;
        for(int i = 0 ; i < M ; i++){
            for(int j = 0 ; j < M ; j++){
                if(cmap[i][j] == 2){
                    hcDist = min(hcDist, abs(house[h].first - i) + abs(house[h].second - j));
                }
            }
        }
        totalDist += hcDist;
    }
    ans = min(ans, totalDist);
}

void letDelete(int start){
    if(deleteC.size() == cnt){
        for(int a = 0 ; a < M ; a++){
            for(int b = 0 ; b < M ; b++){
                cmap[a][b] = map[a][b];
            }
        }
        for(int i = 0 ; i < deleteC.size() ; i++){
            cmap[deleteC[i].first][deleteC[i].second] = 0;
        }
        getDist();
        return;
    }
    for(int i = start+1 ; i < chicken.size() ; i++){
        deleteC.push_back(make_pair(chicken[i].first, chicken[i].second));
        letDelete(i);
        deleteC.pop_back();
    }
}

int main(){
    cin >> M >> N;
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < M ; j++){
            cin >> map[i][j];
            if(map[i][j] == 1){
                house.push_back(make_pair(i,j));
            }
            if(map[i][j] == 2){
                chicken.push_back(make_pair(i,j));
            }
        }
    }
    cnt = chicken.size() - N;
    if(cnt == 0){
        for(int i = 0 ; i < M ; i++){
            for(int j = 0 ; j < M ; j++){
                cmap[i][j] = map[i][j];
            }
        }
        getDist();
    }
    else{
    for(int i = 0 ; i < chicken.size() ; i++){
        deleteC.push_back(make_pair(chicken[i].first, chicken[i].second));
        letDelete(i);
        deleteC.pop_back();
    }}
    cout << ans << "\n";
    return 0;
}