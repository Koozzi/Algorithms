#include <iostream>

using namespace std;

int k;
int num[14];
bool check[14];

void lotto(int cnt){
    if(cnt == 6){
        for(int i = 1 ; i <= k ; i++){
            if(check[i]){
                cout << num[i] << " ";
            }
        }
        cout << "\n";
        return;
    }
    for(int i = 1 ; i <= k ; i++){
        if(!check[i]){
            check[i] = true;
            lotto(cnt + 1);
            check[i] = false;
        }
    }
}

int main(){
    while(1){
        cin >> k;
        for(int i = 1 ; i <= k ; i++){
            cin >> num[i];
            check[i] = false;
        }
        for(int i = 1 ; i <= k-5 ; i++){
            check[i] = true;
            lotto(1);
        }
    }
    return 0;
}