#include <iostream>
#include <string>
#include <map>

using namespace std;

int N, M;
map<int, string> m1;
map<string, int> m2;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> N >> M;
    for(int i = 1 ; i <= N ; i++){
        string s; cin >> s;
        m1.insert({i, s});
        m2.insert({s, i});
    }
    for(int i = 0 ; i < M ; i++){
        string s; cin >> s;
        if(s[0] < 'A'){ // 숫자
            int a = stoi(s);
            cout << m1[a] << "\n";
        }
        else{ // 스트링
            cout << m2[s] << "\n";
        }
    }
    return 0;
}