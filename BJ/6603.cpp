#include <iostream>
#include <vector>

using namespace std;

int M; 
int arr[13];

vector<int> v;

void func(int start){
    if(v.size() == 6){
        for(int i = 0 ; i < 6 ; i++){
            cout << v[i] << " ";
        }cout << "\n";
        return;
    }
    for(int i = start + 1 ; i < M ; i++){
        v.push_back(arr[i]);
        func(i);
        v.pop_back();
    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    while(1){
        cin >> M;

        if(M == 0){
            break;
        }

        for(int i = 0 ; i < M ; i++){
            cin >> arr[i];
        }
        v.clear();
        for(int i = 0 ; i < M ; i++){
            v.push_back(arr[i]);
            func(i);
            v.pop_back();
        }
        cout << "\n";
    }
}
// #include <iostream>
// #include <vector>

// using namespace std;

// int N;

// vector<int> lotto;
// vector<int> selected;

// void SELECT(int startIdx){
//     if(selected.size() == 6){
//         for(int i = 0 ; i < selected.size() ; i++){
//             cout << selected[i] << " ";
//         }
//         cout << "\n";
//     }
//     for(int i = startIdx + 1 ; i < N ; i++){
//         selected.push_back(lotto[i]);
//         SELECT(i);
//         selected.pop_back();
//     }
// }

// int main(){
//     while(1){
//         cin >> N;
//         if(N == 0){
//             return 0;
//         }
//         for(int i = 0 ; i < N ; i++){
//             int a;
//             cin >> a;
//             lotto.push_back(a);
//         }
//         for(int i = 0 ; i < N ; i++){
//             selected.push_back(lotto[i]);
//             SELECT(i);
//             selected.pop_back();
//         }
//         cout << "\n";
//         lotto.clear();
//         selected.clear();
//     }
// }