#include <iostream>
#include <string>

using namespace std;

int cnt[26];

string str;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> str;

    for(int i = 0 ; i < 26 ; i++){
        cnt[i] = -1;
    }
    for(int i = 0 ; i < str.size() ; i++){
        if(cnt[str[i] - 97] == -1){
            cnt[str[i] - 97] = i;
        }
    }
    for(int i = 0 ; i < 26 ; i++){
        cout << cnt[i] << " ";
    }cout << "\n";

    return 0;
}