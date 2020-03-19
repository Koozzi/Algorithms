#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

vector<int> v;

int main(){
    vector<int> v;
    // for(int i = 1 ; i < 11 ; i++){
    //     v.push_back(i);
    // }
    v.push_back(1);
    v.push_back(3);
    v.push_back(5);
    v.push_back(7);

    int tmp = v.size() - (lower_bound(v.begin(), v.end(), 5) - v.begin());
    cout << tmp << endl;
}