#include <iostream>

using namespace std;

int GCD(int a, int b){
    int c;
    while(b != 0){
        c = a % b;
        a = b;
        b = c;
    }
    return a;
}

int main(){
    int T; cin >> T;
    while(T--){
        int a, b; cin >> a >> b;
        cout << a * b / GCD(a, b) << "\n";
    }
    return 0;
}