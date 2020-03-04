#include <iostream>
#include <memory.h>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int dest, N;
int chennal, minNum, minSize;
bool number[10];

int minChennal, minNear = 500000;

vector<int> v;

int numSize(int n){
    int size = 0;
    if(n == 0){
        size = 1;
    }
    else{
        while(n >= 1){
            size++;
            n = n / 10;
        }
    }
    return size;
}

void letsFind(int num){
    if(v.size() == num){
        int divide = pow(10,num-1);
        chennal = 0;
        for(int i = 0 ; i < v.size() ; i++){
            chennal += divide * v[i];
            divide = divide / 10;
        }
        int near = abs(chennal - dest);
        int size = numSize(chennal);
        int ans = size + near;
        minNear = min(minNear, ans);
    }
    else{
        for(int i = 0 ; i < 10 ; i++){
            if(number[i]){
                v.push_back(i);
                letsFind(num);
                v.pop_back();
            }
        }
    }
}

int main(){
    memset(number, true, sizeof(number));
    cin >> dest >> N;
    for(int i = 0 ; i < N ; i++){
        int a;
        cin >> a;
        number[a] = false;
    }
    minNum = 500001;
    for(int t = 1 ; t < 7 ; t++){
        for(int i = 0 ; i < 10 ; i++){
            if(number[i]){
                v.push_back(i);
                letsFind(t);
                v.pop_back();
            }
        }
    }
    if(abs(dest - 100) <= minNear){
        cout << abs(dest - 100) << "\n";
    }
    else{
        cout << minNear << "\n";
    }
    return 0;
}