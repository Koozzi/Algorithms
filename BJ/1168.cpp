#include <iostream>
#include <vector>

using namespace std;

int M, N;

vector<int> answer;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> M >> N;
    vector<int> arr(M);
    for(int i = 0 ; i < M ; i++){
        arr[i] = i + 1;
    }
    int index = 0;
    while(!arr.empty()){
        index = (index + N - 1) % arr.size();
        answer.push_back(arr[index]);
        arr.erase(arr.begin() + index);
    }
    cout << "<";
    for(int i = 0 ; i < M ; i++){
        cout << answer[i];
        if(i < M - 1){
            cout << ", ";
        }
    }
    cout << ">\n";
    return 0;
}