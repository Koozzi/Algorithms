#include <iostream>
#include <vector>
using namespace std;

int N, M;
bool used[9];
vector<int> v;

void func(){
    if(v.size() == M){
        for(int i = 0 ; i < v.size() ; i++){
            cout << v[i] << " ";
        }cout  << "\n";
        return;
    }
    for(int i = 1 ; i <= N ; i++){
        if(!used[i]){
            v.push_back(i);
            used[i] = true;
            func();
            used[i] = false;
            v.pop_back();
        }
    }
}  

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> M;
    
    func();
}