#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int M, N;
int a, b; // 모음, 자음 갯수 
char alp[16];

vector<char> v;

void func(int start){
    if(v.size() == M && a >= 1 && b >= 2){
        for(int i = 0 ; i < v.size() ; i++){
            cout << v[i];
        }cout << "\n";
        return;
    }
    for(int i = start + 1 ; i < N ; i++){
        if(alp[i] == 'a' || alp[i] == 'e' || alp[i] == 'i' || alp[i] == 'o' || alp[i] == 'u'){
            a++;
            v.push_back(alp[i]);
            func(i);
            a--;
            v.pop_back();            
        }
        else{
            b++;
            v.push_back(alp[i]);
            func(i);
            b--;
            v.pop_back();             
        }
        
    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> M >> N;
    for(int i = 0 ; i < N ; i++){
        cin >> alp[i];
    }sort(alp, alp+N);
    func(-1);
    return 0;
}