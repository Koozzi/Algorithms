#include <iostream>

using namespace std;

int gcd(int a, int b){
    int c;
    while(b != 0){
        c = a % b;
        a = b;
        b = c;
    }
    return a;
}

int main(){
    int A, B;
    cin >> A >> B;
    cout << gcd(A, B) << "\n";
    cout << A * B / gcd(A, B) << "\n";
    return 0;
}