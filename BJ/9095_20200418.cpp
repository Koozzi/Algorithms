#include <iostream>
using namespace std;

int T, M;

int func(int a){
    if(a == 1) return 1;
    if(a == 2) return 2;
    if(a == 3) return 4;
    return func(a-1) + func(a-2) + func(a-3);
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> T;
    while(T--){
        cin >> M; cout << func(M) << "\n";
    }
    return 0;
}