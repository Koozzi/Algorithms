#include <iostream>
#include <string>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

string str[10];

int alphabet[26];

int main(){
    int M; cin >> M;
    for(int i = 0 ; i < M ; i++){
        cin >> str[i];
        for(int j = 0 ; j < str[i].size() ; j++){
            alphabet[str[i][j] - 65] += pow(10, str[i].size() - 1 - j);
        }
    }

    vector<int> v;

    for(int i = 0 ; i < 26 ; i++){
        if(alphabet[i] != 0){
            v.push_back(alphabet[i]);
        }
    }

    sort(v.begin(), v.end(), greater<>());

    int mul = 9;
    int ans = 0;
    for(int i = 0 ; i < v.size() ; i++){
        ans += v[i] * mul;
        mul--;
    }
    cout << ans << "\n";
    return 0;
}