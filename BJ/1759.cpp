#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

string str;
string ans;
int M, N;
bool alphabet[26];

bool check(){
    int a = 0;
    int b = 0;
    for(int i = 0 ; i < ans.size() ; i++){
        if(ans[i] == 'a' || ans[i] == 'e' || ans[i] == 'i' || ans[i] == 'o' || ans[i] == 'u'){
            a++;
        }
        else{
            b++;
        }
    }
    if(a >= 1 && b >= 2){
        return true;
    }
    else{
        return false;
    }
}

void func(int start){
    if(ans.size() == M){
        if(check()){
            for(int i = 0 ; i < ans.size() ; i++){
                cout << ans[i];
            }cout << "\n";
        }
        return;
    }
    for(int i = start + 1 ; i < str.size() ; i++){
        ans.push_back(str[i]);
        func(i);
        ans.pop_back();
    }
}

int main(){
    cin >> M >> N;
    for(int i = 0 ; i < N ; i++){
        char a; cin >> a;
        str.push_back(a);
    }
    sort(str.begin(), str.end());
    for(int i = 0 ; i < str.size() ; i++){
        ans.push_back(str[i]);
        func(i);
        ans.pop_back();   
    }
    return 0;
}
// #include <iostream>
// #include <vector>
// #include <algorithm>

// using namespace std;

// int M, N;
// int cnt1 = 0, cnt2 = 0;

// vector<int> v;
// vector<int> newV;

// void solve(int start){
//     if(newV.size() == M){
//         if(cnt1 >= 1 && cnt2 >= 2){
//             for(int i = 0 ; i < newV.size() ; i++){
//                 cout << char(newV[i] + 97);
//             }cout << endl;
//         }
//     }
//     else{
//         for(int i = start + 1 ; i < N ; i++){
//             if(v[i] == 0 || v[i] == 4 || v[i] == 8 || v[i] == 14 || v[i] == 20){
//                 cnt1++;
//                 newV.push_back(v[i]);
//                 solve(i);
//                 newV.pop_back();
//                 cnt1--;
//             }
//             else{
//                 cnt2++;
//                 newV.push_back(v[i]);
//                 solve(i);
//                 newV.pop_back();  
//                 cnt2--;          
//             }
//         }
//     }
// }

// int main(){
//     cin >> M >> N;
//     for(int i = 0 ; i < N ; i++){
//         char a;
//         cin >> a;
//         v.push_back(a - 97);
//     }
//     sort(v.begin(), v.end());
//     for(int i = 0 ; i < v.size() ; i++){
//         if(v[i] == 0 || v[i] == 4 || v[i] == 8 || v[i] == 14 || v[i] == 20){
//             cnt1++;
//             newV.push_back(v[i]);
//             solve(i);
//             newV.pop_back();
//             cnt1--;
//         }
//         else{
//             cnt2++;
//             newV.push_back(v[i]);
//             solve(i);
//             newV.pop_back();  
//             cnt2--;          
//         }
//     }
//     return 0;
// }