// #include <iostream>

// using namespace std;

// int gcd(int a, int b){
//     int c;
//     while(b != 0){
//         c = a % b;
//         a = b;
//         b = c;
//     }
//     return a;
// }

// int main(){
//     int T; cin >> T;
//     while(T--){
//         int M, N; cin >> M >> N;
//         cout << M * N / gcd(M, N) << "\n";
//     }
//     return 0;
// }

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
    int T; cin >> T;
    while(T--){
        int a, b; cin >> a >> b;
        cout << a * b / gcd(a, b) << "\n";
    }
    return 0;
}