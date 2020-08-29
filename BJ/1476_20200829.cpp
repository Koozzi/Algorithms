#include <iostream>

using namespace std;

int main(){
    int E, S, M;
    int e = 1, s = 1, m = 1, year = 1; 
    cin >> E >> S >> M;
    while(E != e || S != s || M != m){
        e++; s++, m++, year++;
        if(e > 15) e = 1;
        if(s > 28) s = 1;
        if(m > 19) m = 1;
    }
    cout << year << "\n";
    return 0;
}