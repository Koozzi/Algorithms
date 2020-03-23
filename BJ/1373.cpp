#include <iostream>
#include <string>
#include <stack>

using namespace std;

string str;
stack<int> s;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cin >> str;
    for(int i = str.length() - 1 ; i >= 0 ; i = i - 3){
        int mult = 1;
        int sum = 0;
        for(int j = i ; j > i - 3 ; j--){
            if(j < 0){
                break;
            }
            sum = sum + (str[j] - 48) * mult;
            mult = mult * 2;
        }
        s.push(sum);
    }
    while(!s.empty()){
        cout << s.top();
        s.pop();
    }
    return 0;
}