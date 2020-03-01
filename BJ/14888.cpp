#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <memory.h>

using namespace std;

int M;
int maxAns = -1000000000;
int minAns = 1000000000;

vector<int> v;
vector<int> Operand;
vector<int> Operator;
vector<int> Operate;

bool visited[99];

void letOperate(){
    if(Operate.size() == M-1){
        int Num = Operand[0];
        // cout << Num << " ";
        for(int i = 0 ; i < M-1 ; i++){
            if(Operate[i] == 0){
                Num = Num + Operand[i+1];
            } 
            else if(Operate[i] == 1){
                Num = Num - Operand[i+1];
            }
            else if(Operate[i] == 2){
                Num = Num * Operand[i+1];
            }
            else{
                Num = Num / Operand[i+1];
            }
            // cout << Operate[i] << " ";
            // cout << Operand[i+1] << " ";
        }
        // cout << "\n";
        maxAns = max(maxAns, Num);
        minAns = min(minAns, Num);
    }
    else{
        for(int i = 0 ; i < Operator.size() ; i++){
            if(!visited[i]){
                Operate.push_back(Operator[i]);
                visited[i] = true;
                letOperate();
                Operate.pop_back();
                visited[i] = false;
            }
        }
    }
}

int main(){
    cin >> M;
    for(int i = 0 ; i < M ; i++){
        int a;
        cin >> a;
        Operand.push_back(a);
    }
    for(int i = 0 ; i < 4 ; i++){
        int a;
        cin >> a;
        for(int j = 0 ; j < a ; j++){
            Operator.push_back(i);
        }
    }
    for(int i = 0 ; i < Operator.size() ; i++){
        Operate.push_back(Operator[i]);
        visited[i] = true;
        letOperate();
        Operate.pop_back();
        visited[i] = false;
    }
    cout << maxAns << "\n";
    cout << minAns << "\n";
    return 0;
}
