#include <iostream>
#include <vector>

using namespace std;

vector<int> arr(100);
vector<int> ans;

int M;
long long int sum;

int gcd(int a, int b){
    int c;
    while(b != 0){
        c = a % b;
        a = b;
        b = c;
    }
    return a;
}

void sumGCD(int start){
    if(ans.size() == 2){
        sum += gcd(ans[0], ans[1]);
        return;
    }

    for(int i = start + 1 ; i < M ; i++){
        ans.push_back(arr[i]);
        sumGCD(i);
        ans.pop_back();
    }
}

int main(){
    int T;  cin >> T;
    while(T--){
        cin >> M;
        
        for(int i = 0 ; i < M ; i++){
            cin >> arr[i];
        }

        sum = 0;

        for(int i = 0 ; i < M ; i++){
            ans.push_back(arr[i]);
            sumGCD(i);
            ans.pop_back();
        }

        cout << sum << "\n";
    }
    return 0;
}