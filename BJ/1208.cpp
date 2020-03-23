#include <iostream>
#include <vector>

using namespace std;

vector<int> total(40);
vector<int> leftS;
vector<int> rightS;

int M, N, ans;
int sumL, sumR;

void solveL(int start){
    if(sumL == N){
        ans++;
    }
    leftS.push_back(sumL);
    for(int i = start + 1 ; i < M / 2 ; i++){
        sumL += total[i];
        solveL(i);
        sumL -= total[i];
    }
}

void solveR(int start){
    if(sumR == N){
        ans++;
    }
    rightS.push_back(sumR);
    for(int i = start + 1 ; i < M ; i++){
        sumR += total[i];
        solveR(i);
        sumR -= total[i];
    }
}

int main(){
    cin >> M >> N;
    for(int i = 0 ; i < M ; i++){
        cin >> total[i];
    }

    for(int i = 0 ; i < M / 2 ; i++){
        sumL += total[i];
        solveL(i);
        sumL -= total[i];
    }
    for(int i = M / 2 ; i < M ; i++){
        sumR += total[i];
        solveR(i);
        sumR -= total[i];
    }

    for(int i = 0 ; i < leftS.size() ; i++){
        for(int j = 0 ; j < rightS.size() ; j++){
            int sumLR = leftS[i] + rightS[j];
            if(sumLR == N){
                ans++;
            }
        }
    }

    cout << ans << endl;
    return 0;
}