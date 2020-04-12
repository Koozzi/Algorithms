#include <iostream>
#include <string>
#include <cstring>

using namespace std;

int M, a;
bool s[21];

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> M;
    for(int i = 0 ; i < M ; i++){
        string str; cin >> str;
        if(str == "add"){
            cin >> a;
            if(!s[a]) s[a] = true;
        }
        else if(str == "remove"){
            cin >> a;
            if(s[a]) s[a] = false;
        }
        else if(str == "check"){
            cin >> a;
            cout << s[a] << "\n";
        }
        else if(str == "toggle"){
            cin >> a;
            if(s[a]){
                s[a] = false;
            }
            else{
                s[a] = true;
            }
        }
        else if(str == "all"){
            memset(s, true, sizeof(s));
        }
        else{
            memset(s, false, sizeof(s));
        }
    }
    return 0;
}

// #include <iostream>
// #include <string>

// using namespace std;

// int M;
// bool check[21];

// int main(){
//     ios_base::sync_with_stdio(0);
//     cin.tie(0);
//     cout.tie(0);
    
//     cin >> M;
//     while(M--){
//         int a;
//         string str;
//         cin >> str;
//         if(str[0] == 'a'){
//             if(str[1] == 'd'){ // add
//                 cin >> a;
//                 check[a] = true;
//             }
//             else{ // all
//                 for(int i = 1 ; i <= 21 ; i++){
//                     check[i] = true;
//                 }
//             }
//         }
//         else if(str[0] == 'r'){ // remove
//             cin >> a;
//             check[a] = false;
//         }
//         else if(str[0] == 'c'){ // check
//             cin >> a;
//             if(check[a]){
//                 cout << 1 << "\n";
//             }
//             else{
//                 cout << 0 << "\n";
//             }
//         }
//         else if(str[0] == 't'){ // toggle
//             cin >> a;
//             if(check[a]){
//                 check[a] = false;
//             }
//             else{
//                 check[a] = true;
//             }
//         }
//         else{ // empty
//             for(int i = 1 ; i <= 21 ; i++){
//                 check[i] = false;
//             }
//         }
//     }
//     return 0;
// }