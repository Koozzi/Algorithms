#include <iostream>
#include <vector>

using namespace std;

int main(){
    int N, M;
    int arr[11][31] = {0};

    cin >> N >> M;
    
    for(int i = 1 ; i <= M ; i++){
        arr[1][i] = 1;
        arr[2][i] = i - 1;
    }

    for(int i = 3 ; i < N+1 ; i++){
        for(int j = i ; j < M+1 ; j++){
            for(int k = i-1 ; k < j ; k++){
                arr[i][j] += arr[i-1][k];
            }
        }
    }

    cout << arr[N][M] << "\n";
    return 0;
}