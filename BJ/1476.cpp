#include <iostream>

using namespace std;

int main(){
    int a, b, c;
    cin >> a >> b >> c;

    int A = 1, B = 1, C = 1;
    int ans = 1;
    while(1){
        if(a == A && b == B && c == C){
            break;
        }
        A++; B++; C++;
        if(A > 15) A = 1;
        if(B > 28) B = 1;
        if(C > 19) C = 1;
        ans++;
    }
    cout << ans << "\n";
    return 0;
}