#include <iostream>

using namespace std;

bool prime[1000000];
int M;

void getPrime(){
    prime[1] = true;
    for(int i = 2 ; i * i < 1000000 ; i++){
        for(int j = i * i ; j < 1000000 ; j += i){
            prime[j] = true;
        }
    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    getPrime();
    while(1){
        bool flag = false;
        cin >> M;
        if(M == 0) break;
        for(int i = 3 ; i < M ; i += 2){
            if(!prime[i] && !prime[M - i]){
                printf("%d = %d + %d\n", M, i, M - i);
                flag = true;
                break;
            }
        }
        if(!flag){
            cout << "Goldbach's conjecture is wrong.\n";
        }
    }
    return 0;
}