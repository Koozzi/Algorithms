#include <iostream>
#include <vector>

using namespace std;

int N, K, lastIdx, cnt = 0;
int arr[101];
int numCount[101];
int lastIndex[101];

vector<int> v;

int main(){
    cin >> N >> K;
    for(int i = 0 ; i < K ; i++){
        cin >> arr[i];
        numCount[arr[i]]++;
        lastIndex[arr[i]] = i;
    }
    for(int i = 0 ; i < K ; i++){
        bool forBreak = false;
        for(int j = 0 ; j < v.size() ; j++){
            if(arr[i] == v[j]){
                numCount[v[j]]--;
                forBreak = true;
                break;
            }
        }
        if(!forBreak){
            lastIdx = i;
            v.push_back(arr[i]);
            numCount[arr[i]]--;
        }
        if(v.size() == N){
            break;
        }
    }
    for(int i = lastIdx + 1 ; i < K ; i++){
        bool forBreak = false;
        // 꽂으려고 하는 기기가 현재 멀티템에 꽂혀 있는지 검색
        for(int j = 0 ; j < v.size() ; j++){
            if(arr[i] == v[j]){
                numCount[v[j]]--;
                forBreak = true;
                break;
            }
        } // 어라? 이미 사용 중이군.
        if(forBreak){
            continue;
        } 
        else{ // 어라? 뭐 하나 뽑아야되는구나.
            // 현재 멀티텝에 꽂혀 있는 기기 중 뒤에 쓸 계획이 없는 기기 빼버리셈
            bool forBreak1 = false;
            for(int j = 0 ; j < v.size() ; j++){
                if(numCount[v[j]] == 0){ // 어랍쇼 더이상 쓸 계획이 없는 기기가 꽂혀 있구만
                    forBreak1 = true;
                    v[j] = arr[i]; // 뽑아서 갈아 끼우고
                    numCount[v[j]]--; // 남아 있는 갯수 줄이고
                    cnt++; // 뽑은 횟수 더해주고
                    break;
                }
            }
            if(forBreak1){ 
                continue; 
            }
            // 보니까 지금 멀티텝에 꽂혀 있는 기기들이 나중에도 다 쓰이나 봄.
            // 그러면 그 중에서 가장 늦게까지 사용하는 기기를 뽑자.
            // 현재 멀티텝에 꽂혀 있는 기기 중 가장 늦게까지 쓰는 기기 탐색
            int maxIdx = 0;
            int deleteNum = 0;
            for(int j = 0 ; j < v.size() ; j++){
                if(lastIndex[v[j]] >= maxIdx){
                    maxIdx = lastIndex[v[j]];
                    deleteNum = j;
                }
            }
            for(int j = 0 ; j < v.size() ; j++){
                if(j == deleteNum){ 
                    v[j] = arr[i]; // 뽑아서 갈아 끼우고
                    numCount[v[j]]--; // 남아 있는 갯수 줄이고      
                    cnt++; // 뽑은 횟수 더해주고     
                    break;         
                }
            }
        }
    }
    cout << cnt << endl;
    return 0;
}

/*
2 7
2 3 2 3 1 2 7
-> 2

3 7
2 3 1 1 4 2 7
-> 2

2 3
1 2 3  
-> 1

1 1
1
-> 0

4 7
1 1 1 1 1 1 1
-> 0

4 7
2 1 1 1 1 1 1
-> 0

4 7
1 1 1 1 1 1 2
-> 0

3 1
1
-> 0

3 2
1 2
-> 0

4 6
1 2 3 4 5 6
-> 2

2 11
1 2 3 4 5 1 1 1 2 2 2
-> 4

3 9
1 2 3 4 1 1 1 1 3
-> 1

3 14
1 4 3 2 5 4 3 2 5 3 4 2 3 4
-> 5

3 11 
11 8 11 7 2 8 2 7 5 10 2
-> 3

2 5
5 2 2 3 5
-> 1

2 4
5 3 1 5
-> 1

3 6
1 1 1 1 2 3
-> 0

3 8
1 2 3 4 1 1 1 2
-> 1

2 15
3 2 1 2 1 2 1 2 1 3 3 3 3 3 3
-> 2

2 5
5 2 2 3 5
-> 1

1 3
1 2 1
-> 2

3 8 
1 2 3 4 1 1 1 2
-> 1

3 6
1 1 1 1 2 3
-> 0
*/