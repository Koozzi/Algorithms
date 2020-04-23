#include <iostream>
using namespace std;

int M, N, arr[2001];
bool check[2001][2001];

void palindrome(){
    for(int i = 1 ; i <= M ; i++){
        check[i][i] = true;
    } // 길이가 1일 때

    for(int i = 1 ; i < M ; i++){
        if(arr[i] == arr[i+1]){
            check[i][i+1] = true;
        }
    } // 길이가 2일 때

    for(int length = 3 ; length < M+1 ; length++){
        for(int i = 1 ; i+length-1 <= M ; i++){
            if(arr[i] == arr[i+length-1] && check[i+1][i+length-2]){
                check[i][i+length-1] = true;
            }
        }
    } // 길이가 3 이상일 때
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    
    cin >> M;
    for(int i = 1 ; i < M+1 ; i++){
        cin >> arr[i];
    }

    palindrome();

    cin >> N;
    for(int i = 0 ; i < N ; i++){
        int a, b; 
        cin >> a >> b;
        cout << check[a][b] << "\n";
    }

    return 0;
}