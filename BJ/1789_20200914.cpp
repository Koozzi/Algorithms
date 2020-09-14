#include <iostream>
using namespace std;

int main(){
    long long S;
    cin >> S;

    int num = 1;
    int result = 0;
    long long sum = 0;

    while(1){
        sum += num;
        result++;
        if(sum > S){
            result--;
            break;
        }
        num++;
    }
    cout << result << "\n";
    return 0;
}