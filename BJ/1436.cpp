#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int numSize(int num){
    int size = 0;
    int n = num;
    while(n >= 1){
        n = n / 10;
        size++;
    }
    return size;
}

bool isTrue(int num){
    vector<int> v;
    vector<int> ans;
    int size = numSize(num);
    int div = pow(10, size-1);
    while(num > 0){
        v.push_back(num / div);
        num = num - (num / div) * div;
        div = div / 10;
    }
    for(int i = 0 ; i < v.size() ; i++){
        if(v[i] == 6){
            ans.push_back(v[i]);
        }
        else{
            ans.clear();
        }
    }
    if(ans.size() >= 3){
        return true;
    }
    else{
        return false;
    }
}

int main(){
    int N;
    cin >> N;
    int n = 1;
    vector<int> realAns;
    while(1){
        if(isTrue(n)){
            realAns.push_back(n);
        }
        if(realAns.size() == N){
            cout << realAns.back() << "\n";
            break;
        }
        n++;
    }
    return 0;
}