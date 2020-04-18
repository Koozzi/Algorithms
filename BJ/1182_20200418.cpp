#include <iostream>
#include <vector>

using namespace std;

int M, N, sum, ans, arr[20];
vector<int> v;
void func(int start){
    if(sum == N){
        ans++;
        /*
        4 0 
        2 -2 2 -2
        arr[0] + arr[1] 를 헤서 0 을 구하고 ans++ 해줬음
        return 을 해버리면 arr[0] + arr[1] + arr[2] + arr[3] 의 경우를
        count 하지 못함.
        */
    }
    for(int i = start + 1 ; i < M ; i++){
        sum += arr[i];
        func(i);
        sum -= arr[i];
    }
}

int main(){
    cin >> M >> N;
    for(int i = 0 ; i < M ; i++){
        cin >> arr[i];
    }
    for(int i = 0 ; i < M ; i++){
        sum += arr[i];
        func(i);
        sum -= arr[i];
    }
    cout << ans << "\n";
    return 0;
}