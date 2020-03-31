#include <iostream>
#include <string>
#include <vector>
#include <string.h>

using namespace std;

int main(){
    char c[1000001];
    
    scanf("%[^\n]s", c);
    
    int ans = 0;
    bool flag = false;
    for(int i = 0 ; i < strlen(c) ; i++){
        if(!flag && c[i] != ' '){
            ans++;
            flag = true;
        }
        else if(flag && c[i] == ' '){
            flag = false;
        }
    }

    cout << ans << "\n";
}