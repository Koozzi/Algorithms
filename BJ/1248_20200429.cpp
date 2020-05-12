#include <iostream>
#include <vector>
using namespace std;

int M;
char map[11][11];
vector<int> v;

bool poss(int idx){
    int sum = 0;
    for(int i = idx ; i >= 0 ; i--){
        sum += v[i];

        if(map[i][idx] == '+' && sum <= 0) return false;
        if(map[i][idx] == '-' && sum >= 0) return false;
        if(map[i][idx] == '0' && sum != 0) return false;
    }

    return true;
}
void func(int idx){
    if(idx == M){
        for(int i = 0 ; i < v.size() ; i++){
            cout << v[i] << " ";
        }cout << "\n";
        exit(0);
    }
    for(int i = -10 ; i <= 10 ; i++){
        v.push_back(i);
        if(poss(idx)){
            func(idx + 1);
        }
        v.pop_back();
    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> M;
    for(int i = 0 ; i < M ; i++){
        for(int j = i ; j < M ; j++){
            cin >> map[i][j];
        }
    }
    func(0);
}


































// #include <iostream>
// #include <string>
// #include <vector>
// using namespace std;

// int M;
// char map[11][11];

// string str;
// vector<int> v;


// bool possible(int idx){
//     int sum = 0;
//     for(int i = idx ; i >= 0 ; i--){
//         sum += v[i];

//         if(map[i][idx] == '+' && sum <= 0) return false;
//         if(map[i][idx] == '-' && sum >= 0) return false;
//         if(map[i][idx] == '0' && sum != 0) return false;
//     }

//     return true;
// }

// void func(int idx){
//     if(idx == M){
//         for(int i = 0 ; i < v.size() ; i++){
//             cout << v[i] << " ";
//         }cout << "\n";
//         exit(0);
//     }

//     for(int i = -10 ; i <= 10 ; i++){
//         v.push_back(i);
//         if(possible(idx)){
//             func(idx + 1);
//         }
//         v.pop_back();
//     }
// }

// int main(){
//     ios_base::sync_with_stdio(0);
//     cin.tie(0);
//     cout.tie(0);

//     cin >> M >> str;    
//     int idx = 0;
//     for(int i = 0 ; i < M ; i++){
//         for(int j = i ; j < M ; j++){
//             map[i][j] = str[idx++];
//         }
//     }
//     func(0);
//     return 0;
// }