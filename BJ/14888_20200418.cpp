#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#define MAX_NUM 1000000000
using namespace std;

int M, Operand[11];
int minAns = MAX_NUM;
int maxAns = -MAX_NUM;
bool used[50];
vector<int> v;
vector<int> oper;
set<string> s;
void func(){
    if(oper.size() == M - 1){
        string str = "";
        for(int i = 0 ; i < oper.size() ; i++){
            str.push_back(oper[i] + '0');
        }
        if(s.count(str) == 0){
            s.insert(str);
            int sum = Operand[0];
            for(int i = 0 ; i < oper.size() ; i++){
                if(oper[i] == 0){
                    sum += Operand[i+1];
                }
                else if(oper[i] == 1){
                    sum -= Operand[i+1];
                }
                else if(oper[i] == 2){
                    sum *= Operand[i+1];
                }
                else{
                    sum /= Operand[i+1];
                }
            }
            maxAns = max(maxAns, sum);
            minAns = min(minAns, sum);
        }
        return;
    }
    for(int i = 0 ; i < v.size() ; i++){
        if(!used[i]){
            oper.push_back(v[i]);
            used[i] = true;
            func();
            oper.pop_back();
            used[i] = false;
        }
    }
}

int main(){
    cin >> M;
    for(int i = 0 ; i < M ; i++){
        cin >> Operand[i];
    }
    for(int i = 0 ; i < 4 ; i++){
        int a; cin >> a;
        for(int j = 0 ; j < a ; j++){
            v.push_back(i);
        }
    }
    func();
    cout << maxAns << "\n" << minAns << "\n";
    return 0;
}