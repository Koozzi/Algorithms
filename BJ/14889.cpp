#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool T[21];
int stat[21][21];
int N;
int ans = 1001;
void makeScore(){
    int teamTrue = 0, teamFalse = 0;
    int gap;
    for(int i = 1 ; i <= N ; i++){
        if(T[i]){
            for(int j = 1; j <= N ; j++){
                if(j != i && T[j]){
                    teamTrue += stat[i][j];
                }
            }
        }
        else{
            for(int j = 1; j <= N ; j++){
                if(j != i && !T[j]){
                    teamFalse += stat[i][j];
                }
            }
        }
    }
    gap = abs(teamTrue - teamFalse);
    ans = min(ans, gap);
}

void makeTeam(int start){
    int cnt = 0; 
    for(int i = 1 ; i <= N ; i++){
        if(T[i]){
            cnt++;
        }
    }
    if(cnt == N/2){
        makeScore();
        return;
    }
    else{
        for(int i = start + 1 ; i <= N ; i++){
            T[i] = true;
            makeTeam(i);
            T[i] = false;
        }
    }
}

int main(){
    cin >> N;
    for(int i = 1 ; i <= N ; i++){
        for(int j = 1 ; j <= N ; j++){
            cin >> stat[i][j];
        }
    }
    for(int i = 1 ; i <= N ; i++){
        T[i] = true;
        makeTeam(i);
        T[i] = false;
    }
    cout << ans << "\n";
    return 0;
}