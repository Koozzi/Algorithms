#include <iostream>
#include <vector>

using namespace std;

int M, N;

vector<int> v;

void func(){
    if(v.size() == N){
        for(int i = 0 ; i < v.size() ; i++){
            cout << v[i] << " ";
        }cout << "\n";
        return;
    }
    for(int i = 1 ; i <= M ; i++){
        v.push_back(i);
        func();
        v.pop_back();
    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> M >> N;

    for(int i = 1 ; i <= M ; i++){
        v.push_back(i);
        func();
        v.pop_back();
    }
    return 0;
}