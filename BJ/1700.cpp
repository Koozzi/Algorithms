#include <iostream>
#include <vector>

using namespace std;

int N, K, lastIdx, cnt = 0;
int arr[101];
vector<pair<int, int>> numInfo[101];
vector<int> v;

int main(){
    cin >> N >> K;
    for(int i = 1 ; i <= K ; i++){
        cin >> arr[i];
        numInfo[arr[i]].push_back(make_pair(0,0));
        numInfo[arr[i]][0].first++;
        numInfo[arr[i]][0].second = i;
    }
    for(int i = 1 ; i <= K ; i++){
        // 빈 멀티텝에 기기를 꽂자
        bool forBreak = false;
        for(int j = 0 ; j < v.size() ; j++){
            if(arr[i] == v[j]){
                // 내가 지금 꽂으려고 하는 기기가
                // 이미 멀티텝에 꽂혀있군.
                numInfo[v[j]][0].first--;
                forBreak = true;
                break;
            }
        }
        if(!forBreak){
            // 내가 지금 꽂으려고 하는 기기가
            // 멀티텝에 꽂혀 있지 않다.
            // 그럼 꽂자
            v.push_back(arr[i]);
            numInfo[arr[i]][0].first--;
        }
        if(v.size() == N){
            // 가장 마지막으로 꽂은 기기 번호를 lastIdx 변수에 저장
            lastIdx = i;
            break;
        }
    }
    for(int i = lastIdx + 1 ; i <= K ; i++){
        bool forBreak = false;
        // 꽂으려고 하는 기기가 현재 멀티템에 꽂혀 있는지 검색
        for(int j = 0 ; j < v.size() ; j++){
            if(arr[i] == v[j]){
                numInfo[arr[i]][0].first--;
                forBreak = true;
                break;
            }
        } 
        if(forBreak){
            // 어라? 이미 사용 중이군. 
            continue;
        } 
        // 어라? 뭐 하나 뽑아야되는구나.
        // 현재 멀티텝에 꽂혀 있는 기기 중 뒤에 쓸 계획이 없는 기기 빼버리셈
        forBreak = false;
        for(int j = 0 ; j < v.size() ; j++){
            if(numInfo[v[j]][0].first == 0){ 
                //더이상 쓸 계획이 없는 기기가 꽂혀 있구만
                forBreak = true;
                v[j] = arr[i]; // 뽑아서 갈아 끼우고
                numInfo[v[j]][0].first--; // 남아 있는 갯수 줄이고
                cnt++; // 뽑은 횟수 더해주고
                break;
            }
        }
        if(forBreak){ 
            continue; 
        }
        // 보니까 지금 멀티텝에 꽂혀 있는 기기들이 나중에도 다 쓰이나 봄.
        // 그러면 그 중에서 가장 늦게까지 사용하는 기기를 뽑자.
        // 현재 멀티텝에 꽂혀 있는 기기 중 가장 늦게 쓰기 시작하는 기기 탐색
        int maxIdx = 0;
        int deleteNum = 0;
        for(int j = 0 ; j < v.size() ; j++){
            for(int k = i ; j <= K ; k++){
                if(arr[k] == v[j]){
                    numInfo[v[j]][0].second = k;
                    if(numInfo[v[j]][0].second >= maxIdx){
                        maxIdx = numInfo[v[j]][0].second;
                        deleteNum = j;
                    }
                    break;
                }
            }
        }
        v[deleteNum] = arr[i];
        numInfo[arr[i]][0].first--;
        cnt++;
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