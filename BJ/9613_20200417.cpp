#include <iostream>
#include <vector>

using namespace std;

int T, M;
int arr[100];
long long ans;
vector<int> v;

int GCD(int a, int b){
    int c;
    while(b != 0){
        c = a % b;
        a = b;
        b = c;
    }
    return a;
}

void func(int start){
    if(v.size() == 2){
        ans += GCD(v[0], v[1]);
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
    cin >> T;
    while(T--){
        ans = 0;
        cin >> M;
        for(int i = 0 ; i < M ; i++){
            cin >> arr[i];
        }
        for(int i = 0 ; i < M ; i++){
            v.push_back(arr[i]);
            func(i);
            v.pop_back();
        }
        cout << ans << "\n";
    }
    return 0;
}