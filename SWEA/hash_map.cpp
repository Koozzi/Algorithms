#include <iostream>
#include <string>
#include <map>
#include <set>
using namespace std;

int main(){
    map<string, int> m;
    
    m.insert({"key1", 1});
    m.insert({"key2", 2});
    
    cout << m["key1"] << "\n";

    set<int> s;
    set<int>::iterator iter = s.begin();
    s.insert(1);
    s.insert(1);
    s.insert(1);
    s.insert(1);
    for(iter ; iter != s.end() ; iter++){
        cout << *iter << "\n";
    }
    
    return 0;
}