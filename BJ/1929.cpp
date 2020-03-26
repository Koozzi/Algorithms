#include <iostream>

using namespace std;

int M, N;
bool check[1000001];

int main(){
    cin >> M >> N;

    check[1] = true;

    for(int i = 2 ; i * i <= N ; i++){
        if(!check[i]){
            for(int j = i * i ; j <= N ; j += i){
                check[j] = true;
            }
        }
    }

    for(int i = M ; i <= N ; i++){
        if(!check[i]){
            cout << i << "\n";
        }
    }

    return 0; 
}