#include <iostream>
#include <string>

using namespace std;

int ans[26];

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    string str;
    cin >> str;
    for(int i = 0 ; i < str.size() ; i++){
        if(str[i] >= 97){ // 소문자
            ans[str[i] - 97]++;
        }
        else{ // 대문자
            ans[str[i] - 65]++;
        }
    }
    int maxCnt = 0;
    int maxIdx = 0;
    for(int i = 0 ; i < 26 ; i++){
        if(ans[i] >= maxCnt){
            maxCnt = ans[i];
            maxIdx = i;
        }
    }
    int sameCnt = 0;
    for(int i = 0 ; i < 26 ; i++){
        if(ans[i] == maxCnt){
            sameCnt++;
        }
        if(sameCnt >= 2){
            cout << "?\n";
            return 0;
        }
    }
    cout << char(maxIdx + 65) << "\n";
    return 0;
}