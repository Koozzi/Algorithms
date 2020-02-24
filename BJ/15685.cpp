#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int N;
vector<pair<pair<int, int>, pair<int, int>>> v;
vector<pair<int ,int>> location;
bool visitied[101][101];

void moveClock(int startI, int startJ, int fixI, int fixJ){
    int I = startI - fixI;
    int J = startJ - fixJ;
    int afterMoveI, afterMoveJ;
    afterMoveI = fixI + J;
    afterMoveJ = fixJ - I;
    visitied[afterMoveI][afterMoveJ] = true;
    location.push_back(make_pair(afterMoveI, afterMoveJ));
}

void makeCurve(int startI, int startJ, int dirc, int feature){
    location.clear();
    int endI, endJ, endPoint;
    visitied[startI][startJ] = true;
    location.push_back(make_pair(startI,startJ));
    if(dirc == 0){
        location.push_back(make_pair(startI,startJ+1));
        visitied[startI][startJ+1] = true;
    }
    else if(dirc == 1){
        location.push_back(make_pair(startI-1,startJ));
        visitied[startI-1][startJ] = true;
    }
    else if(dirc == 2){
        location.push_back(make_pair(startI,startJ-1));
        visitied[startI][startJ-1] = true;
    }
    else{
        location.push_back(make_pair(startI+1,startJ));
        visitied[startI+1][startJ] = true;
    }
    int T = 1;
    while(feature--){
        endI = location.back().first;
        endJ = location.back().second;
        endPoint = location.size() - 1;
        for(int i = endPoint-1 ; i >= 0 ; i--){
            moveClock(location[i].first, location[i].second, endI, endJ);
        }
        T++;
    }
}

int main(){
    int ans = 0;
    cin >> N;
    for(int i = 0 ; i < N ; i++){
        int a, b, c, d;
        cin >> a >> b >> c >> d;
        makeCurve(b,a,c,d);
    }
    for(int i = 0 ; i < 100 ; i++){
        for(int j = 0 ; j < 100 ; j++){
            if(visitied[i][j]){
                if(visitied[i][j+1]){
                    if(visitied[i+1][j]){
                        if(visitied[i+1][j+1]){
                            ans++;
                        }
                    }
                }
            }
        }
    }
    cout << ans << "\n";
    return 0;
}