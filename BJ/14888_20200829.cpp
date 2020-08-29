#include <iostream>
#include <algorithm>
#include <vector>
#define MAX_NUM 98765432
#define MIN_NUM -98765432
using namespace std;

int N, ans, Operand[11];
int min_ans = MAX_NUM, max_ans = MIN_NUM;

vector<int> Operator;

void get_ans(){
    ans = Operand[0];
    for(int i = 0 ; i < N-1 ; i++){
        if(Operator[i] == 0){
            ans += Operand[i+1];
        }
        else if(Operator[i] == 1){
            ans -= Operand[i+1];
        }
        else if(Operator[i] == 2){
            ans *= Operand[i+1];
        }
        else{
            ans /= Operand[i+1];
        }
    }
    min_ans = min(min_ans, ans);
    max_ans = max(max_ans, ans);
}

int main(){
    cin >> N;
    for(int i = 0 ; i < N ; i++){
        cin >> Operand[i];
    } 
    
    for(int i = 0 ; i < 4 ; i++){
        int a; cin >> a;
        for(int j = 0 ; j < a ; j++){
            Operator.push_back(i);
        }
    }
    
    sort(Operator.begin(), Operator.end());

    
    get_ans();

    while(next_permutation(Operator.begin(), Operator.end())){
        get_ans();
    }
    
    cout << max_ans << "\n";
    cout << min_ans << "\n";
    return 0;
}