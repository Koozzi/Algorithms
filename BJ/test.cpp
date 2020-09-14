#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <unordered_map>
#include <set>
#include <time.h>

using namespace std;

int main(){
    unordered_map<int, int> m;
    for(int i = 0 ; i < 10 ; i++){
        m.insert({i,i});
    }
    for(auto iter = m.begin() ; iter != m.end() ; iter++){
        cout << iter->first << "\n";
    }

    vector<string> v;
    v.push_back("AVSC");

    sort(v[0].begin(), v[0].end());
    cout << v[0] << "\n";
}