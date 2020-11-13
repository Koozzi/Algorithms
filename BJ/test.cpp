#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
    int arr[3] = {1,2,3};
    int a = *max_element(arr, arr+3);
    cout << a << "\n";
}