#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int arr[11] = {0};
int loc[11] = {0};
bool visited[11];

int main(){
    int N;
    cin >> N;
    for(int i = 1 ; i <= N ; i++){
        cin >> arr[i];
    }
    loc[arr[1]+1] = 1;
    for(int i = 2 ; i <= N ; i++){
        int cnt = 0;
        for(int j = 1 ; j <= N ; j++){
            if(loc[j] == 0){
                loc[j] = cnt;
                visited[j] = true;
                cnt++;
                if(loc[j] == arr[i]){
                    loc[j] = i;
                    visited[j] = false;
                    break;
                }
            }
        }
        for(int j = 1 ; j <= N ; j++){
            if(visited[j]){
                loc[j] = 0;
            }
            visited[j] = false;
        }
    }
    for(int i = 1 ; i <= N ; i++){
        cout << loc[i] << " ";
    }
    cout << "\n";
    return 0;
}