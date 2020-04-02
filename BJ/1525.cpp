#include <iostream>
#include <queue>
#include <string>

using namespace std;

string str;

int main(){
    for(int i = 0 ; i < 9 ; i++){
        char a; cin >> a;
        str.push_back(a);
    }
    string s1 = "1234";

    int a = stoi(s1);

    string s2 = to_string(a);

    cout << a << "\n";
    cout << s2[0] << "\n";
    cout << s2[1] << "\n";
    cout << s2[2] << "\n";
    cout << s2[3] << "\n";
}