#include <iostream>

using namespace std;

bool notPrime[246913];

void primeNum(){
    for(int i = 2 ; i < 246913 ; i += 2){
        notPrime[i] = true;
    }
    for(int i = 3 ; i*i < 246913 ; i++){
        if(!notPrime[i]){
            for(int j = i*i ; j < 246913 ; j += i){
                if(!notPrime[j]){
                    notPrime[j] = true;
                }
            }
        }
    }
}

int main(){
    primeNum();
    while(1){
        int A;
        cin >> A;
        if(A == 0){
            break;
        }
        int countF = 0;
        int countS = 0;
        for(int i = 1 ; i <= A * 2 ; i++){
            if(!notPrime[i]){
                countF++;
            }
            if(i == A){
                countS = countF;
            }
        }
        if(A == 1){
            cout << 1 << "\n";
        }else{
        cout << countF - countS << "\n";}
    }
    return 0;
}