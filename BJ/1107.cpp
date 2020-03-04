#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <memory.h>

using namespace std;

int dest, M, cnt, chennalCnt;
int near = 500001;
bool number[10];
bool visited[10];
vector<int> v;

void solve(int start){
    if(v.size() == cnt){
        int chennal = 0;
        int mult = pow(10, cnt-1);
        for(int i = 0 ; i < v.size() ; i++){
            chennal += mult * v[i];
            mult = mult / 10;
        }
        near = min(near, abs(chennal - dest));
        return;
    }
    else{
        for(int i = 0 ; i < 10 ; i++){
            if(number[i]){
                v.push_back(i);
                solve(i);
                v.pop_back();     
            }         
        }
    }
}

int main(){
    memset(number, true, sizeof(number));
    cin >> dest >> M;
    int howLong = dest;
    cnt = 0;
    while(howLong >= 1){
        howLong = howLong / 10;
        cnt++;
    }
    if(dest == 0){
        cnt = 1;
    }
    for(int i = 0 ; i < M ; i++){
        int a;
        cin >> a;
        number[a] = false;
    }
    if(dest == 0 && number[0]){
        cout << 1 << "\n";
        return 0;
    }
    for(int i = 0 ; i < 10 ; i++){
        if(number[i]){
            v.push_back(i);
            solve(i);
            v.pop_back();
        }
    }
    
    if(abs(dest - 100) <= near + cnt){
        cout << abs(dest - 100);
    }
    else{
        cout << near + cnt << "\n";
    }
    return 0;
}
