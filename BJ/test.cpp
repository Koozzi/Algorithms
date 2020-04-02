#include <iostream>
#include <set>

using namespace std;

int main(){
    set<int> s;
    set<int>::iterator iter;
    for(int i = 1; i <= 10 ; i++){
        s.insert(i);
    }
    iter = s.find(10);
    cout << *iter << "\n";

    iter = s.end();
    cout << *iter << "\n";

    iter = s.find(11);
    cout << *iter << "\n";
}