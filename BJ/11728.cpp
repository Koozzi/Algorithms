#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int A, B, a;

int arrA[1000000];
int arrB[1000000];

// vector<int> ans;

int main(){
    cin >> A >> B;

    for(int i = 0 ; i < A ; i++){
        cin >> arrA[i];
    }

    for(int i = 0 ; i < B ; i++){
        cin >> arrB[i];
    }

    int i = 0;
    int j = 0;
    int check = 0;

    while(1){
        if(arrA[i] < arrB[j]){
            cout << arrA[i] << " ";
            // ans.push_back(arrA[i]);
            i++;
        }
        else if(arrA[i] > arrB[j]){
            cout << arrB[j] << " ";
            // ans.push_back(arrB[j]);
            j++;
        }
        else{
            cout << arrA[i] << " ";
            cout << arrB[j] << " ";
            // ans.push_back(arrA[i]);
            // ans.push_back(arrB[j]);
            i++;
            j++;
        }
        if(i >= A || j >= B){
            if(i >= A){
                check = 1;
            }
            else if(j >= B){
                check = 2;
            }
            break;
        }
    }

    if(check == 1){
        while(j < B){
            cout << arrB[j] << " ";
            // ans.push_back(arrB[j]);
            j++;
        }
    }
    else if(check == 2){
        while(i < A){
            cout << arrA[i] << " ";
            // ans.push_back(arrA[i]);
            i++;
        }
    }

    // for(int i = 0 ; i < ans.size() ; i++){
    //     cout << ans[i] << " ";
    // }cout << endl;

    return 0;
}