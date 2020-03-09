#include <iostream>
#include <deque>

using namespace std;

deque<int> dq;

int N;

int main(){
    cin >> N;
    for(int i = 1 ; i <= N ; i++){
        dq.push_back(i);
    }
    while(dq.size() > 1){
        dq.pop_front();
        int A = dq.front();
        dq.push_back(A);
        dq.pop_front();
    }
    cout << dq[0] << endl;
    return 0;
}