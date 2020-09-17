#include <algorithm>
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int N, M, K, A, B, end_cnt, sum;
int cus[1001], rep[21], rec[21];

vector<pair<int, int>> customer(1001, {-1, -1}); // 접수창구, 정비창구
vector<pair<int, int>> reception(21, {-1,-1}); // 현재고객, 끝나는 시간
vector<pair<int, int>> repair(21, {-1,-1}); // 현재고객, 끝나는 시간

queue<pair<int, int>> reception_queue;
queue<int> repair_queue;

void repair_out(int current_time){ 
    for(int i = 1 ; i <= M ; i++){
        int current_customer = repair[i].first;
        int end_time = repair[i].second;
        if(end_time == current_time){
            int a = customer[current_customer].first;
            int b = customer[current_customer].second;

            if(a == A && b == B) sum += current_customer;

            repair[i].first = -1;
            repair[i].second = -1;
            end_cnt++;
        }
    }
}

void reception_out(int current_time){
    for(int i = 1 ; i <= N ; i++){
        int current_customer = reception[i].first;
        int end_time = reception[i].second;
        if(end_time == current_time){

            repair_queue.push(current_customer);
            reception[i].first = -1;
            reception[i].second = -1;
        }
    }
}

void repair_in(int current_time){
    for(int i = 1 ; i <= M ; i++){
        if(repair_queue.empty()) return;    
        int current_customer = repair[i].first;
        int new_customer = repair_queue.front();
        // printf("정비 대기 : %d\n", new_customer);
        if(current_customer == -1){ // i번 째 창구는 현재 비어있음
            repair_queue.pop();
            repair[i].first = new_customer;
            repair[i].second = current_time + rep[i];
            customer[new_customer].second = i;
        }
    }
}

void reception_in(int current_time){
    for(int i = 1 ; i <= N ; i++){
        if(reception_queue.empty()) return;
        int current_customer = reception[i].first;
        int new_customer = reception_queue.front().first;
        int arrive_time = reception_queue.front().second;
        if(arrive_time <= current_time && current_customer == -1){
            reception_queue.pop();
            reception[i].first = new_customer;
            reception[i].second = current_time + rec[i];
            customer[new_customer].first = i;
        }
    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    int T; cin >> T;
    for(int t = 1 ; t <= T ; t++){
        cin >> N >> M >> K >> A >> B;
        end_cnt = 0;
        sum = 0;
        for(int i = 1 ; i <= N ; i++){
            cin >> rec[i];
        }
        for(int i = 1 ; i <= M ; i++){
            cin >> rep[i];
        }
        for(int i = 1 ; i <= K ; i++){
            cin >> cus[i];
            reception_queue.push({i, cus[i]});
        }
        for(int time = 0 ;; time++){
            if(end_cnt == K) break; 
            repair_out(time);
            reception_out(time);
            reception_in(time);
            repair_in(time);
        }
        if(sum == 0) printf("#%d %d\n", t, -1);
        else printf("#%d %d\n", t, sum);
    }

    return 0;
}