#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    stack<int> s;
    int M, a;
    cin >> M;

    for(int i = 0 ; i < M ; i++){
        string str; cin >> str;
        if(str == "push"){
            cin >> a;
            s.push(a);
        }
        else if(str == "pop"){
            if(!s.empty()){
                cout << s.top() << "\n";
                s.pop();
            }
            else{
                cout << -1 << "\n";
            }
        }
        else if(str == "size"){
            cout << s.size() << "\n";
        }
        else if(str == "empty"){
            cout << s.empty() << "\n";
        }
        else{
            if(!s.empty()){
                cout << s.top() << "\n";
            }
            else{
                cout << -1 << "\n";
            }
        }
    }
    return 0;
}