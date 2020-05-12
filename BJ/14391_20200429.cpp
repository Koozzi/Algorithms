
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int M, N, ans1, ans2;
string str[4];

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> M >> N;

    for(int i = 0 ; i < M ; i++){
        cin >> str[i];
        ans1 += stoi(str[i]);
    }

    for(int j = 0 ; j < N ; j++){
        string newStr;
        for(int i = 0 ; i < M ; i++){
            newStr.push_back(str[i][j]);
        }
        ans2 += stoi(newStr);
    }

    cout << max(ans1, ans2) << "\n";
    return 0;
}
/*
1000
0001
0000
1000
-> 2010 (Not 20001)
*/