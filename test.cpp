#include <iostream>
#include <set>
#include <string>
#include <vector>

using namespace std;

int main(){
    vector<string> v;
    v.push_back("test");
    char c = 'A';
    for(int i = 0 ; i < 26 ; i++){
        string newStr = "";
        newStr.push_back(char(c + i));
        v.push_back(newStr);
    }
    for(int i = 1 ; i <= 26 ; i++){
        cout << v[i][0] << "\n";
    }
    return 0;
}