#include <iostream>
#include <string>
#include <stack>

using namespace std;

string str;
stack<int> s;

bool flag;

void change8to2(int N){
    if(N == 0){
        if(flag){
            cout << 0 << 0 << 0;
        }
        else{
            cout << 0;
        }
        return;
    }
    if(N == 1){
        if(flag){
            cout << 0 << 0 << 1;
        }
        else{
            cout << 1;
        }
        return;
    }
    
    while(1){
        s.push(N % 2);
        N = N / 2;
        if(N == 1){
            s.push(1);
            break;
        }
    }

    if(flag){ 
        int size = s.size();
        for(int i = 0 ; i < 3 - size ; i++){
            cout << 0;
        }
    }

    while(!s.empty()){
        cout << s.top();
        s.pop();
    }
}

int main(){
    cin >> str; 
    for(int i = 0 ; i < str.length() ; i++){
        if(i != 0) flag = true;
        int num = str[i] - 48;
        change8to2(num);       
    }
    return 0;
}