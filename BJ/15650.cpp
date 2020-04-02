#include <iostream>
#include <vector>

using namespace std;

int M, N;

vector<int> v;

void func(int start){
    if(v.size() == N){
        for(int i = 0 ; i < v.size() ; i++){
            cout << v[i] << " ";
        }cout << "\n";
        return;
    }
    for(int i = start + 1 ; i <= M ; i++){
        v.push_back(i);
        func(i);
        v.pop_back();
    }
}

int main(){
    cin >> M >> N;
    for(int i = 1 ; i <= M ; i++){
        v.push_back(i);
        func(i);
        v.pop_back();
    }
    return 0;
}