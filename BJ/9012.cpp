#include <iostream>
#include <string>
#include <stack>

using namespace std;

int main(){
    int M; cin >> M;
    for(int i = 0 ; i < M ; i++){
        stack<int> s;
        string str; cin >> str;
        bool whileBreak = false;
        for(int i = 0 ; i < str.size() ; i++){
            if(str[i] == '('){
                s.push(0);
            }
            else{
                if(s.empty()){
                    cout << "NO" << "\n";
                    whileBreak = true;
                    break;
                }
                s.pop();
            }
        }
        if(whileBreak) continue;
        if(s.empty()){
            cout << "YES" << "\n";
        }
        else{
            cout << "NO" << "\n";
        }
    }
    return 0;
}