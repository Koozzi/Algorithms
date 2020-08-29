#include <iostream>

#define MAX_NUM 1e9
using namespace std;

int M;
int min_ans = MAX_NUM;
int max_ans = -MAX_NUM;
int Operand[11];
int Operator[4];

void func(int cnt, int ans, int plu, int sub, int mul, int div){
    if(cnt == M){
        max_ans = max(max_ans, ans);
        min_ans = min(min_ans, ans);
        return;
    }
    if(plu > 0) func(cnt + 1, ans + Operand[cnt], plu - 1, sub, mul, div);
    if(sub > 0) func(cnt + 1, ans - Operand[cnt], plu, sub - 1, mul, div);
    if(mul > 0) func(cnt + 1, ans * Operand[cnt], plu, sub, mul - 1, div);
    if(div > 0) func(cnt + 1, ans / Operand[cnt], plu, sub, mul, div - 1);
}

int main(){
    cin >> M;
    for(int i = 0 ; i < M ; i++){
        cin >> Operand[i];
    }
    for(int i = 0 ; i < 4 ; i++){
        cin >> Operator[i];
    }
    func(1, Operand[0], Operator[0], Operator[1], Operator[2], Operator[3]);
    cout << max_ans << "\n" << min_ans << "\n";
    return 0;
}