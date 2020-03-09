#include <iostream>
#include <vector>
#include <algorithm>
#include <memory.h>

using namespace std;

int M, N, ans = 0;
char inputData[51][17];
bool check[26];
vector<char> v[51];
vector<int> alpabet;

void select(int start){
    if(alpabet.size() == N){
        int cnt = 0;
        for(int i = 0 ; i < M ; i++){
            bool forBreak = false;
            for(int j = 0 ; j < v[i].size() ; j++){
                if(!check[v[i][j] - 97]){
                    forBreak = true;
                    break;
                }
            }
            if(!forBreak){
                cnt++;
            }
        }
        ans = max(ans, cnt);
    }
    else{
        for(int i = start + 1 ; i < 26 ; i++){
            if(i != ('a' - 97) && i != ('c' - 97) && i != ('i' - 97) && i != ('n' - 97) && i != ('t' - 97)){
                alpabet.push_back(i);
                check[i] = true;
                select(i);
                alpabet.pop_back();
                check[i] = false;
            }
        }
    }
}

int main(){
    cin >> M >> N;
    for(int i = 0 ; i < M ; i++){
        cin >> inputData[i];
    }
    for(int i = 0 ; i < M ; i++){
        int idx = 0;
        while(1){
            if(inputData[i][idx] == '\0'){
                break;
            }
            v[i].push_back(inputData[i][idx]);
            idx++;
        }
    }
    if(N < 5){
        cout << 0 << "\n";
        return 0;
    }
    
    check['a' - 97] = true;
    check['c' - 97] = true;
    check['i' - 97] = true;
    check['n' - 97] = true;
    check['t' - 97] = true;
    alpabet.push_back('a' - 97);
    alpabet.push_back('c' - 97);
    alpabet.push_back('i' - 97);
    alpabet.push_back('n' - 97);
    alpabet.push_back('t' - 97);

    if(N == 5){
        int cnt = 0;
        for(int i = 0 ; i < M ; i++){
            bool forBreak = false;
            for(int j = 0 ; j < v[i].size() ; j++){
                if(!check[v[i][j] - 97]){
                    forBreak = true;
                    break;
                }
            }
            if(!forBreak){
                cnt++;
            }
        }
        cout << cnt << "\n";
        return 0;
    }

    for(int i = 0 ; i < 26 ; i++){
        if(i != ('a' - 97) && i != ('c' - 97) && i != ('i' - 97) && i != ('n' - 97) && i != ('t' - 97)){
            alpabet.push_back(i);
            check[i] = true;
            select(i);
            alpabet.pop_back();
            check[i] = false;
        }
    }
    cout << ans << "\n";
    return 0;
}