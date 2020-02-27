#include <iostream>

using namespace std;

int main(){
    int N, M = 1;
    cin >> N;
    while(M <= 1000000){
        int Num = 0;
        int Div = 100000;
        int tmp = M;
        Num += M;
        while(Div >= 1){
            Num += M / Div;
            M = M - (M / Div) * Div;
            Div /= 10;
        }
        M = tmp;
        M++;
        if(Num == N){
            cout << tmp << "\n";
            return 0;
        }
    }
    cout << 0 << "\n";
    return 0;
}