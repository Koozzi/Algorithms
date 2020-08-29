#include <iostream>

using namespace std;

bool isPrime[1001];

void findPrime(){
    isPrime[1] = true;
    for(int i = 2 ; i * i < 1001 ; i++){
        for(int j = i * i ; j < 1001 ; j += i){
            if(!isPrime[j]) isPrime[j] = true;
        }
    }
}

int main(){
    findPrime();
    int N, ans = 0;
    cin >> N;
    for(int i = 0 ; i < N ; i++){
        int a; cin >> a;
        if(!isPrime[a]) ans++;
    }
    cout << ans << "\n";
    return 0;
}