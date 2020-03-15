#include <iostream>
#include <vector>

using namespace std;

int M, N;
char arr[2][51][51];

void show(){
    cout << endl;
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < N ; j++){
            cout << arr[0][i][j];
        }cout << endl;
    }
}
bool isSame(){
    for(int i = 0 ; i < M ; i++){
        for(int j = 0 ; j < N ; j++){
            if(arr[0][i][j] != arr[1][i][j]){
                return false;
            }
        }
    }
    return true;
}
void change(int I, int J){
    for(int i = I ; i < I + 3 ; i++){
        for(int j = J ; j < J + 3 ; j++){
            if(arr[0][i][j] == '0'){
                arr[0][i][j] = '1';
            }
            else{
                arr[0][i][j] = '0';
            }
        }
    }
}
int main(){
    int ans = 0;
    cin >> M >> N;
    for(int t = 0 ; t < 2 ; t++){
        for(int i = 0 ; i < M ; i++){
            cin >> arr[t][i];
        }
    }
    if(isSame()){
        cout << "0" << endl;
        return 0;
    }
    for(int i = 0 ; i < M - 2 ; i++){
        for(int j = 0 ; j < N - 2 ; j++){
            if(arr[0][i][j] != arr[1][i][j]){
                ans++;
                change(i,j);
                if(isSame()){
                    cout << ans << endl;
                    return 0;
                }
            }
        }
    }
    cout << "-1" << endl;
    return 0;
}
