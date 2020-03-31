#include <iostream>
#include <string>
#include <cstring>

using namespace std;

int M;
bool check[26];

int main(){
    int ans = 0;
    cin >> M;
    for(int i = 0 ; i < M ; i++){
        string str; cin >> str;
        memset(check, false, sizeof(check));
        check[str[0] - 97] = true;
        bool forBreak = false;
        for(int j = 1 ; j < str.size() ; j++){
            if(!check[str[j] - 97]){
                check[str[j] - 97] = true;
            }
            else{
                if(str[j-1] != str[j]){
                    forBreak = true;
                    break;
                }
            }
        }
        if(!forBreak){
            ans++;
        }
    }
    cout << ans << "\n";
}