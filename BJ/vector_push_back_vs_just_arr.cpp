#include <iostream>
#include <vector>
#include <ctime>
#include <algorithm>

using namespace std;

int main(){
    
    clock_t start1, end1;
    
    cout << "Vector push_back 10만개" << "\n";
    start1 = clock();
    vector<int> v;
    for(int i = 0 ; i < 1000000 ; i++){
        v.push_back(i);
    }
    end1 = clock();
    cout << end1 - start1 << "ms\n";

    
    cout << "Vector size 정해두고 10만개" << "\n";
    start1 = clock();
    vector<int> v1(1000000);
    for(int i = 0 ; i < 1000000 ; i++){
        v[i] = i;
    }
    end1 = clock();
    cout << end1 - start1 << "ms\n";

    
    cout << "기본 배열 size 정해두고 10만개" << "\n";
    start1 = clock();
    int arr[1000000] = {0};
    for(int i = 0 ; i < 1000000 ; i++){
        arr[i] = i;
    }
    end1 = clock();
    cout << end1 - start1 << "ms\n";
    
    return 0;
}