#include <iostream>
#include <list>
#include <string>

using namespace std;

list<int> lt;
list<int>::iterator iter;
string inputStr;

int M, cur;
char a, b;

int main(){
    cin >> inputStr;
    for(int i = 0 ; i < inputStr.size() ; i++){
        lt.push_back(inputStr[i]);
    }
    lt.push_back('0');
    cur = inputStr.size();
    cin >> M;
    for(int i = 0 ; i < M ; i++){
        cin >> a;
        if(a == 'P'){
            cin >> b;
        }
        else if(a == 'L'){
            if(cur != 0){
                cur--;
            }
        }
        else if(a == 'D'){
            if(cur != inputStr.size()){
                cur++;
            }
        }
        else if(a == 'B'){
            iter = lt.begin();
            advance(iter, cur);
            lt.erase(iter);
        }
    }
}