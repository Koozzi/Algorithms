#include <iostream>
#include <deque>

using namespace std;

int M, N, ans = 0;

deque<int> dq;
deque<int> popOut;

void show(){
    for(int i = 0 ; i < dq.size() ; i++){
        cout << dq[i] << " ";
    }cout << "\n";
}

void goLeft(){
    int a = dq.front();
    dq.pop_front();
    dq.push_back(a);
}

void goRight(){
    int a = dq.back();
    dq.pop_back();
    dq.push_front(a);
}

int main(){
    cin >> M >> N;

    for(int i = 1 ; i <= M ; i++){
        dq.push_back(i);
    }

    for(int i = 0 ; i < N ; i++){
        int a;
        cin >> a;
        popOut.push_back(dq[a-1]);
    }

    for(int i = 0 ; i < N ; i++){
        int leftCount = 0;
        int rightCount = 0;
        while(1){
            if(dq.front() == popOut[i]){
                break;
            }
            goLeft();
            leftCount++;
        }
        for(int j = 0 ; j < leftCount ; j++){
            goRight();
        }
        while(1){
            if(dq.front() == popOut[i]){
                break;
            }
            goRight();
            rightCount++;
        }
        dq.pop_front();
        ans += min(leftCount, rightCount);
    }
    cout << ans << "\n";
    return 0;
}