#include <iostream>
#include <queue>
#include <vector>
#include <memory.h>

using namespace std;

int N, ans, checkCount;
char arr[9][9];

void searchDown(int startI, int startJ){
    checkCount = 0;
    if(startI + N > 8){
        // cout << startI << " " << startJ << "\n";
        return;
    }
    vector<char> v;
    for(int i = startI ; i < startI + N ; i++){
        v.push_back(arr[i][startJ]);
    }
    for(int i = 0 ; i < N/2 ; i++){
        if(v[i] == v[N-1-i]){
            checkCount++;
        }
    }
    if(checkCount == N/2){
        ans++;
    }
    // cout << startI << " " << startJ << " " << checkCount << " ";
    // for(int i =  0 ; i < v.size() ; i++){
    //     cout << v[i]; 
    // }
    // cout <<"\n";
}

void searchRight(int startI, int startJ){
    checkCount = 0;
    if(startJ + N > 8){
        // cout << startI << " " << startJ << "\n";
        return;
    }
    vector<char> v;
    for(int i = startJ ; i < startJ + N ; i++){
        v.push_back(arr[startI][i]);
    }
    for(int i = 0 ; i < N/2 ; i++){
        if(v[i] == v[N-1-i]){
            checkCount++;
        }
    }
    if(checkCount == N/2){
        ans++;
    }
    // cout << startI << " " << startJ << " " << checkCount << " ";
    // for(int i =  0 ; i < v.size() ; i++){
    //     cout << v[i]; 
    // }
    // cout <<"\n";
}

int main(){
    for(int t = 1; t <= 10 ; t++){
        cin >> N;
        ans = 0;
        for(int i = 0 ; i < 8 ; i++){
            cin >> arr[i];
        }
        for(int i = 0 ; i < 8 ; i++){
            for(int j = 0 ; j < 8 ; j++){
                searchRight(i,j);
                searchDown(i,j);
            }
        }
        if(N == 1){
            cout << "#" << t << " " << 64 << "\n";
        }
        else{
            cout << "#" << t << " " << ans << "\n";
        }
    }
    return 0;
}
