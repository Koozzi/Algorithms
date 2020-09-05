#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <string>
using namespace std;

unordered_map<string, int> hm;
unordered_set<string> hs;

int main(){
    hm["asd"] = 1;
    cout << hm["asd"] << "\n";

    hs.insert("asd");
    hs.insert("asd");
    hs.insert("ff");
    cout << hs.size() << "\n";
    hs.clear();
    cout << hs.size() << "\n";

    // DIA DIA EMERALD SAPPHIRE
    hs.insert("DIA");
    hs.insert("DIA");
    hs.insert("EMERALD");
    hs.insert("SAPPHIRE");
    cout << hs.size() << "\n";
    
    hs.clear();

    vector<string> v;
    v.push_back("DIA");
    v.push_back("DIA");
    v.push_back("EMERALD");
    v.push_back("SHPPHIRE");
    for(int i = 0 ; i < v.size() ; i++){
        string s = v[i];
        hs.insert(s);
    } 
    cout << hs.size() << "\n";
}