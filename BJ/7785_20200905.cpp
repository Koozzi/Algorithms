#include <iostream>
#include <string>
#include <map>
using namespace std;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int  N; cin >> N;
    map<string, int, greater<>> m;
    for(int i = 0 ; i < N ; i++){
        string s, a; cin >> s >> a;
        if(a == "enter"){
            m[s] = 1;
        }
        else{
            m[s] = 0;
        }
    }
    map<string, int>::iterator iter;
    for(iter = m.begin() ; iter != m.end() ; iter++){
        if((*iter).second == 1){
            cout << (*iter).first << "\n";
        }
    }cout << "\n";
}