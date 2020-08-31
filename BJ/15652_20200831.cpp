#include <iostream>
#include <vector>
using namespace std;

int N, M;
vector<int> v;

void func(int start){
    if(v.size() == M){
        for(int i = 0 ; i < v.size() ; i++){
            cout << v[i] << " ";
        }cout << "\n";
        return;
    }
    for(int i = start ; i <= N ; i++){
        v.push_back(i);
        func(i);
        v.pop_back();
    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> N >> M;
    for(int i = 1 ; i <= N ; i++){
        v.push_back(i);
        func(i);
        v.pop_back();
    }
    return 0;
}