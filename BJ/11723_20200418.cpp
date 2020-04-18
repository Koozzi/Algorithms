#include <iostream>
#include <string>
using namespace std;

int M, a;
bool arr[21];

int main(){
    cin >> M;
    while(M--){
        string str;
        cin >> str;
        if(str == "add"){
            cin >> a;
            arr[a] = true;
        }
        else if(str == "remove"){
            cin >> a;
            arr[a] = false;
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
                arr[a] = true;
            }
        }
        else{
            for(int i = 1 ; i <= 20 ; i++){
                arr[a] = false;
            }
        }
    }
    return 0;
}