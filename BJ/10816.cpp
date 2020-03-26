#include <iostream>

using namespace std;

int M, N;
int check[20000001];

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> M;
    for(int i = 0 ; i < M ; i++){
        int a; cin >> a;
        check[10000000 + a]++;
    }
    
    cin >> N;
    for(int i = 0 ; i < N ; i++){
        int a; cin >> a;
        if(check[10000000 + a] != 0){
            cout << check[10000000 + a] << " ";
        }
        else{
            cout << 0 << " ";
        }
    }
    return 0;
}