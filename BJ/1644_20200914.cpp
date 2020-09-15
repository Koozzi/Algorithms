#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int N;
bool prime[4000001];
vector<int> primeNum;

void make_prime_number(){
    prime[1] = true;
    for(int i = 2 ; i * i <= N ; i++){
        for(int j = i * i ; j <= N ; j += i){
            if(!prime[j]) prime[j] = true;
        }
    }
    for(int i = 1 ; i <= N ; i++){
        if(!prime[i]) primeNum.push_back(i);
    }
}

int main(){
    cin >> N;
    make_prime_number();
    // Prime# => False
    // Non-Prime# => True
    
    int left = 0;
    int right = 0;
    int sum = 0;
    int cnt = 0;

    while(1){
        if(sum == N){
            cnt++;
            sum -= primeNum[left++];
        }
        else if(sum > N) sum -= primeNum[left++];
        else if(right == primeNum.size()) break;
        else sum += primeNum[right++];
    }
    cout << cnt << "\n";
    return 0;
}