#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int finalScore = 98765432;
int N ,cnt;
int map[21][21];
bool used[21];

vector<int> t1;
vector<int> t2;

int getScore(){
    int score1 = 0;
    int score2 = 0;
    
    for(int i = 1 ; i <= N ; i++){
        if(used[i]){
            for(int j = 1 ; j <= N ; j++){
                if(used[j] && i != j){
                    score1 += map[i][j];
                }
            }
        }
        else{
            for(int j = 1 ; j <= N ; j++){
                if(!used[j] && i != j){
                    score2 += map[i][j];
                }
            }
        }
    }
    return abs(score1 - score2);
}

void func(int start){
    if(cnt == N/2){
        finalScore = min(finalScore, getScore());
        return;
    }
    for(int i = start + 1 ; i <= N ; i++){
        used[i] = true;
        cnt++;
        func(i);
        cnt--;
        used[i] = false;
    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> N;
    for(int i = 1 ; i <= N ; i++){
        for(int j = 1 ; j <= N ; j++){
            cin >> map[i][j];
        }
    }
    func(0);
    cout << finalScore << "\n";
    return 0;
}