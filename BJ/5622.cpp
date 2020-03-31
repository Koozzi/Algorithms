#include <iostream>
#include <string>

using namespace std;

string str;

int main(){
    int ans = 0;
    cin >> str;
    for(int i = 0 ; i < str.size() ; i++){
        int a = str[i] - 65;
        if(a < 3){
            ans += 3;
        }
        else if(a >= 3 && a < 6){
            ans += 4;
        }
        else if(a >= 6 && a < 9){
            ans += 5;
        }
        else if(a >= 9 && a < 12){
            ans += 6;
        }
        else if(a >= 12 && a < 15){
            ans += 7;
        }
        else if(a >= 15 && a < 19){
            ans += 8;
        }
        else if(a >= 19 && a < 22){
            ans += 9;
        }
        else if(a >= 22){
            ans += 10;
        }
    }
    cout << ans << "\n";
}