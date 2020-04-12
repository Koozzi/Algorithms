#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int M; cin >> M;

    string s;
    for(int i = 1 ; i <= M ; i++){
        cout << i << " ";
        s.push_back(i + 48);
    }cout << "\n";
    
    while(next_permutation(s.begin(), s.end())){
        for(int i = 0 ; i < s.size() ; i++){
            cout << s[i] << " ";
        }cout << "\n";
    }

    return 0;
}

// #include <iostream>
// #include <algorithm>
// #include <vector>

// using namespace std;

// int M;
// bool visited[9];

// vector<int> v;

// void permutation(){
//     if(v.size() == M){
//         for(int i = 0 ; i < v.size() ; i++){
//             cout << v[i] << " ";
//         }cout << "\n";
//         return;
//     }
//     for(int i = 1 ; i <= M ; i++){
//         if(!visited[i]){
//             v.push_back(i);
//             visited[i] = true;
//             permutation();
//             v.pop_back();
//             visited[i] = false;        
//         }
//     }
// }

// int main(){
//     ios_base::sync_with_stdio(0);
//     cin.tie(0);
//     cout.tie(0);

//     cin >> M;
//     for(int i = 1 ; i <= M ; i++){
//         v.push_back(i);
//         visited[i] = true;
//         permutation();
//         v.pop_back();
//         visited[i] = false;
//     }

//     return 0;
// }