#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int M, a;
int maxAns = -1000000000; 
int minAns = 1000000000;
bool used[10];
bool operate[4];
vector<int> v1;
vector<int> v2;
vector<int> ans;

void solve(){
    if(ans.size() == M - 1){
        int answer = v1[0];
        for(int i = 0 ; i < ans.size() ; i++){
            if(ans[i] == 0){
                answer = answer + v1[i+1];
            }
            else if(ans[i] == 1){
                answer = answer - v1[i+1];
            }
            else if(ans[i] == 2){
                answer = answer * v1[i+1];
            }
            else{
                answer = answer / v1[i+1];
            }
        }
        maxAns = max(maxAns, answer);
        minAns = min(minAns, answer);
        return;
    }

    for(int i = 0 ; i < v2.size() ; i++){
        if(!used[i]){
            ans.push_back(v2[i]);
            used[i] = true;
            solve();
            ans.pop_back();
            used[i] = false;
        }
    }
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cin >> M;

    for(int i = 0 ; i < M ; i++){
        cin >> a;
        v1.push_back(a);
    }

    for(int i = 0 ; i < 4 ; i++){
        cin >> a;
        for(int j = 0 ; j < a ; j++){
            v2.push_back(i);
        }
    }

    for(int i = 0 ; i < v2.size() ; i++){
        ans.push_back(v2[i]);
        used[i] = true;
        solve();
        ans.pop_back();
        used[i] = false;
    }

    cout << maxAns << "\n";
    cout << minAns << "\n";

    return 0;
}

// 재귀 -> 항상 중복되는 연산이 있는지 확인해야 함.

// #include <cstdio>

// int n;
// int num[11], op[4];
// int mx = -1e9, mn = 1e9;

// void solve(int count, int ans, int add, int sub, int mul, int div) {
// 	if (count == n) {
// 		if (ans > mx) mx = ans;
// 		if (ans < mn) mn = ans;
// 		return;
// 	}
// 	if (add > 0) solve(count + 1, ans + num[count], add - 1, sub, mul, div);
// 	if (sub > 0) solve(count + 1, ans - num[count], add, sub - 1, mul, div);
// 	if (mul > 0) solve(count + 1, ans * num[count], add, sub, mul - 1, div);
// 	if (div > 0) solve(count + 1, ans / num[count], add, sub, mul, div - 1);
// }

// int main() {
// 	scanf("%d", &n);
// 	for (int i = 0; i < n; i++) scanf("%d", &num[i]);
// 	for (int i = 0; i < 4; i++) scanf("%d", &op[i]);
// 	solve(1, num[0], op[0], op[1], op[2], op[3]);
// 	printf("%d\n%d\n", mx, mn);
// 	return 0;
// }