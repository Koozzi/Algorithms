#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int N;
bool prime[4000001];

vector<int> primeNum;

void getPrime(int n){
    prime[1] = true;
    for(int i = 2 ; i * i <= n ; i++){
        for(int j = i * i ; j <= n ; j = j + i){
            prime[j] = true;
        }
    }
    
    for(int i = 1 ; i <= n ; i++){
        if(!prime[i]){
            primeNum.push_back(i);
        }
    }
}

int main(){
    cin >> N;
    getPrime(N);

    int ans = 0;
    int sum = 0;
    int lo = 0;
    int hi = 0;

    while(1){
        if(sum > N) sum = sum - primeNum[lo++];
        else if(hi == primeNum.size()) break;
        else sum += primeNum[hi++];
        if(sum == N) ans++;
    }


    cout << ans << endl;

    return 0;
}