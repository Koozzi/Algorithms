#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main(){
    int M; 
    cin >> M;
    string bufferflush;
    getline(cin, bufferflush);
    while(M--){
        string str;
        getline(cin, str);
        string tmp;
        for(int i = 0 ; i < str.size() ; i++){
            if(str[i] != ' '){
                tmp.push_back(str[i]);
            }
            else{
                reverse(tmp.begin(), tmp.end());
                cout << tmp << " ";
                tmp.clear();
            }
        }
        reverse(tmp.begin(), tmp.end());
        cout << tmp << "\n";
    }
    return 0;
}