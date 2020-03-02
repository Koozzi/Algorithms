#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int M, N, ans = 0;
int card[100];
vector<int> v;
vector<int> vecAns;
void solve(int start){
    int sum = 0;
    if(v.size() == 3){
        for(int i = 0 ; i < v.size() ; i++){
            sum += v[i];
        }
        if(sum <= N){
            ans = max(ans, sum);
        }
    }
    else{
        for(int i = start + 1 ; i < M ; i++){
            v.push_back(card[i]);
            solve(i);
            v.pop_back();        
        }
    }
}

int main(){
    cin >> M >> N;
    for(int i = 0 ; i < M ; i++){
        cin >> card[i];
    }
    for(int i = 0 ; i < M ; i++){
        v.push_back(card[i]);
        solve(i);
        v.pop_back();
    }
    cout << ans << "\n";
    return 0;
}