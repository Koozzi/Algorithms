#include <iostream>
#include <vector>

using namespace std;

vector<int> v;

int main(){
    for(int i = 0 ; i < 10 ; i++){
        v.push_back(i);
    }
    for(int i = 0 ; i < 10 ; i++){
        cout << v[i] << " ";
    }cout << "\n";
    for(int i = 4 ; i < 10 ; i++){
        v.erase(v.begin() + 4);
    }
    for(int i = 0 ; i < 10 ; i++){
        cout << v[i] << " ";
    }cout << "\n";
}