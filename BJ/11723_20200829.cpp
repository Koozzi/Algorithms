#include <iostream>
#include <string>
using namespace std;

int M, a;
bool used[21];

void all(){
    for(int i = 1 ; i < 21 ; i++){
        used[i] = true;
    }
}

void empty(){
    for(int i = 1 ; i < 21 ; i++){
        used[i] = false;
    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> M;
    for(int i = 0 ; i < M ; i++){
        string s; cin >> s; 
        if(s == "add") {cin >> a; used[a] = true;}
        if(s == "check") {cin >> a; cout << used[a] << "\n";}
        if(s == "remove") {cin >> a; used[a] = false;}
        if(s == "toggle") {cin >> a; used[a] = !used[a];}
        if(s == "all") all();
        if(s == "empty") empty();
    }
}