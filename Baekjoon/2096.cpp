#include <iostream>
#include <algorithm>
#include <vector>
#include <stdio.h>

using namespace std;

int main(){
    int n, a, b, c;
    int input_data[3] = {0};
    int arr_max[3] = {0};
    int arr_min[3] = {0};

    cin >> n;
    for(int i = 0 ; i < 3 ; i++){
        cin >> input_data[i];
        arr_max[i] = input_data[i];
        arr_min[i] = input_data[i];
    }
    if(n == 1){
        cout << *max_element(input_data, input_data+3) << " ";
        cout << *min_element(input_data, input_data+3);
    }

    for(int i = 1 ; i < n ; i++){
        cin >> a >> b >> c;
        int tmp1, tmp2, tmp3;
        
        tmp1 = max(arr_max[0], arr_max[1]);
        tmp2 = *max_element(arr_max, arr_max+3);
        tmp3 = max(arr_max[1], arr_max[2]);

        arr_max[0] = tmp1 + a;
        arr_max[1] = tmp2 + b;
        arr_max[2] = tmp3 + c;

        tmp1 = min(arr_min[0], arr_min[1]);
        tmp2 = *min_element(arr_min, arr_min+3);
        tmp3 = min(arr_min[1], arr_min[2]);

        arr_min[0] = tmp1 + a;
        arr_min[1] = tmp2 + b;
        arr_min[2] = tmp3 + c;   
    }
    if(n != 1){
        cout << *max_element(arr_max, arr_max+3) << " ";
        cout << *min_element(arr_min, arr_min+3);
    }

    return 0;
}