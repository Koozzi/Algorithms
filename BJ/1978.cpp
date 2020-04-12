#include <iostream>

using namespace std;

int M, ans;

bool prime[1001];

void findPrime(){
    prime[1] = true;
    for(int i = 2 ; i * i <= 1000 ; i++){
        for(int j = i * i ; j <= 1000 ; j += i){
            if(!prime[j]) prime[j] = true;
        }
    }
}

int main(){
    findPrime();
    cin >> M;
    for(int i = 0 ; i < M ; i++){
        int a; cin >> a;
        if(!prime[a]) ans++;
    }
    cout<< ans << "\n";
    return 0;
}