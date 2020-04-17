#include <iostream>
#define MAX_NUM 1000001
using namespace std;

bool prime[MAX_NUM];

void findPrime(){
    prime[1] = true;
    for(int i = 2 ; i * i < MAX_NUM ; i++){
        for(int j = i * i ; j < MAX_NUM ; j += i){
            if(!prime[j]) prime[j] = true;
        }
    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    findPrime();
    while(1){
        bool flag = false;
        int a; cin >> a;
        if(a == 0) break;

        for(int i = 2 ; i < a ; i++){
            if(!prime[i] && !prime[a - i]){
                cout << a << " = " << i << " + " << a - i << "\n";
                flag = true;
                break;
            }
        }
        if(!flag) cout << "Goldbach's conjecture is wrong." << "\n";
    }
    return 0;
}