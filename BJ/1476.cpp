#include <iostream>

using namespace std;

int main(){
    int E, S, M, year = 1;
    int e = 1;
    int s = 1;
    int m = 1;
    cin >> E >> S >> M;
    while(e != E || s != S || m != M){
        e++;
        s++;
        m++;
        if(e > 15){
            e = 1;
        }
        if(s > 28){
            s = 1;
        }
        if(m > 19){
            m = 1;
        }
        year++;
    }
    cout << year << endl;
    return 0;
}