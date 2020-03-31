#include <iostream>
#include <string>
#include <cmath>

using namespace std;

string num1;
string num2;
string tmp;

int intNum1;
int intNum2;

int charTOint(string str){
    int mul = pow(10, 2);
    int num = 0;
    for(int i = 0 ; i < str.size() ; i++){
        num += ((str[i] - 48) * mul);
        mul /= 10;
    }
    return num;
}

int main(){
    cin >> num1 >> num2;

    for(int i = 2 ; i >= 0 ; i--){
        tmp.push_back(num1[i]);
    }
    intNum1 = charTOint(tmp);

    tmp.clear();

    for(int i = 2 ; i >= 0 ; i--){
        tmp.push_back(num2[i]);
    }
    intNum2 = charTOint(tmp); 

    cout << max(intNum1, intNum2) << "\n";

    return 0;
}