#include <iostream>
#include <vector>
using namespace std;

int main(){
    vector<char> a;
    vector<char> b[10];
    a.push_back('b');
    cout << a[0] << "\n";

    char A = 'c';
    a.push_back(A);
    cout << a[1] << "\n";

    a[1] = 'G';
    cout << a[1] << "\n";   

    a.erase(a.begin() + 1);
    


    b[5].push_back(A);
    cout << b[5][0] << "\n";

    b[5][0] = 'H';
    cout << b[5][0] << "\n";

    
    return 0;
}