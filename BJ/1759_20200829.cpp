#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int M, N;
char arr[15];
string s;

bool mo(){
    for(int i = 0 ; i < s.size() ; i++){
        if(s[i] == 'a') return true;
        if(s[i] == 'e') return true;
        if(s[i] == 'i') return true;
        if(s[i] == 'o') return true;
        if(s[i] == 'u') return true;
    } return false;
}

bool ja(){
    int cnt = s.size();
    for(int i = 0 ; i < s.size() ; i++){
        if(s[i] == 'a') cnt--;
        if(s[i] == 'e') cnt--;
        if(s[i] == 'i') cnt--;
        if(s[i] == 'o') cnt--;
        if(s[i] == 'u') cnt--;
        if(cnt < 2) return false;
    } return true;
}

void func(int start){
    if(s.size() == M && mo() && ja()){
        cout << s << "\n";
        return;
    }
    for(int i = start + 1 ; i < N ; i++){
        s.push_back(arr[i]);
        func(i);
        s.pop_back();
    }
}

int main(){
    cin >> M >> N;
    for(int i = 0 ; i < N ; i++){
        cin >> arr[i];
    } sort(arr, arr + N);

    func(-1);
    return 0;
}