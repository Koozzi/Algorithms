#include <iostream>

using namespace std;

int A, B, C, a, b, c, ans;

int main(){
    cin >> a >> b >> c;
    while(1){
        ans++; A++, B++; C++;

        if(A > 15) A = 1;

        if(B > 28) B = 1;

        if(C > 19) C = 1;

        if(A == a && B == b && C == c) break;
    }
    cout << ans << "\n";
    return 0;
}