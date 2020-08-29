#include <iostream>

using namespace std;

int T, Time[16], Price[16], arr[16];

int main(){
    cin >> T;
    for(int i = 1 ; i <= T ; i++){
        cin >> Time[i] >> Price[i];
    }
    if(Time[T] == 1){
        arr[T] = Price[T];
    }
    for(int i = T - 1 ; i > 0 ; i--){
        if(Time[i] + i <= T+1) arr[i] = max(arr[i+1], arr[i + Time[i]] + Price[i]);
        else arr[i] = arr[i+1];
    }
    cout << arr[1] << "\n";
    return 0;
}