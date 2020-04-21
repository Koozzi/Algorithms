#include <iostream>
#include <string>
using namespace std;

int M, a;
bool arr[21];

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> M;
    while(M--){
        string str;
        cin >> str;
        if(str == "add"){
            cin >> a;
            if(!arr[a]) arr[a] = true;
        }
        else if(str == "remove"){
            cin >> a;
            if(arr[a]) arr[a] = false;
        }   
        else if(str == "check"){
            cin >> a;
            cout << arr[a] << "\n";
        }
        else if(str == "toggle"){
            cin >> a;
            if(arr[a]) arr[a] = false;
            else arr[a] = true;
        }
        else if(str == "all"){
            for(int i = 1 ; i <= 20 ; i++){
                arr[i] = true;
            }
        }
        else{
            for(int i = 1 ; i <= 20 ; i++){
                arr[i] = false;
            }
        }
    }
    return 0;
}