#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int main(){
    vector<int> v;
    v.push_back(7);
    v.push_back(4);
    v.push_back(2);
    sort(v.begin(), v.end());
    for(int i = 0 ; i < v.size() ; i++){
        cout << v[i] << " ";
    }
    cout << "\n";
    return 0;
}