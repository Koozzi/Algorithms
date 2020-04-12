#include <iostream>

using namespace std;

int M;
int Operand[11];
int Operator[4];

int maxAns = -1e9;
int minAns = 1e9;

void func(int cnt, int ans, int plu, int sub, int mul, int div){
    if(cnt == M){
        maxAns = max(maxAns, ans);
        minAns = min(minAns, ans);
        return;
    }
    if(plu > 0) func(cnt + 1, ans + Operand[cnt], plu - 1, sub, mul, div);
    if(sub > 0) func(cnt + 1, ans - Operand[cnt], plu, sub - 1, mul, div);
    if(mul > 0) func(cnt + 1, ans * Operand[cnt], plu, sub, mul - 1, div);
    if(div > 0) func(cnt + 1, ans / Operand[cnt], plu, sub, mul, div - 1);
}

int main(){
    cin >> M;
    for(int i = 0 ; i < M ; i++){
        cin >> Operand[i];
    }
    for(int i = 0 ; i < 4 ; i++){
        cin >> Operator[i];
    }
    func(1, Operand[0], Operator[0], Operator[1], Operator[2], Operator[3]);
    cout << maxAns << "\n" << minAns << "\n";
    return 0;
}

// #include <iostream>
// #include <algorithm>
// #include <vector>
// #include <set>

// using namespace std;

// int M;
// int minAns = 1000000000;
// int maxAns = -1000000000;
// int Operand[11];
// bool used[88];

// string str;
// string Operator;
// set<string> ans;

// int getSum(){
//     int sum = Operand[0];
//     for(int i = 0 ; i < str.size() ; i++){
//         if(str[i] == '0'){
//             sum += Operand[i+1];
//         }
//         else if(str[i] == '1'){
//             sum -= Operand[i+1];
//         }
//         else if(str[i] == '2'){
//             sum *= Operand[i+1];
//         }
//         else{
//             sum /= Operand[i+1];
//         }
//     }
//     return sum;
// }  

// void func(){
//     if(str.size() == M - 1){
//         if(ans.count(str) == 0){
//             ans.insert(str);
//             int sum = getSum();
//             minAns = min(minAns, sum);
//             maxAns = max(maxAns, sum);
//         }
//         return;
//     }
//     for(int i = 0 ; i < Operator.size() ; i++){
//         if(!used[i]){
//             str.push_back(Operator[i]);
//             used[i] = true;
//             func();
//             str.pop_back();
//             used[i] = false;
//         }
//     }
// }

// int main(){
//     cin >> M;
//     for(int i = 0 ; i < M ; i++){
//         cin >> Operand[i];
//     }

//     for(int i = 0 ; i < 4 ; i++){
//         int a; cin >> a;
//         for(int j = 0 ; j < a ; j++){
//             Operator.push_back(i + '0');
//         }
//     }

//     func();

//     cout << maxAns << "\n" << minAns << "\n";
//     return 0;
// }

// #include <iostream>
// #include <vector>
// #include <algorithm>

// using namespace std;

// int M, a;
// int maxAns = -1000000000; 
// int minAns = 1000000000;
// bool used[10];
// bool operate[4];
// vector<int> v1;
// vector<int> v2;
// vector<int> ans;

// void solve(){
//     if(ans.size() == M - 1){
//         int answer = v1[0];
//         for(int i = 0 ; i < ans.size() ; i++){
//             if(ans[i] == 0){
//                 answer = answer + v1[i+1];
//             }
//             else if(ans[i] == 1){
//                 answer = answer - v1[i+1];
//             }
//             else if(ans[i] == 2){
//                 answer = answer * v1[i+1];
//             }
//             else{
//                 answer = answer / v1[i+1];
//             }
//         }
//         maxAns = max(maxAns, answer);
//         minAns = min(minAns, answer);
//         return;
//     }

//     for(int i = 0 ; i < v2.size() ; i++){
//         if(!used[i]){
//             ans.push_back(v2[i]);
//             used[i] = true;
//             solve();
//             ans.pop_back();
//             used[i] = false;
//         }
//     }
// }

// int main(){
//     ios_base::sync_with_stdio(0);
//     cin.tie(0);
//     cin >> M;

//     for(int i = 0 ; i < M ; i++){
//         cin >> a;
//         v1.push_back(a);
//     }

//     for(int i = 0 ; i < 4 ; i++){
//         cin >> a;
//         for(int j = 0 ; j < a ; j++){
//             v2.push_back(i);
//         }
//     }

//     for(int i = 0 ; i < v2.size() ; i++){
//         ans.push_back(v2[i]);
//         used[i] = true;
//         solve();
//         ans.pop_back();
//         used[i] = false;
//     }

//     cout << maxAns << "\n";
//     cout << minAns << "\n";

//     return 0;
// }

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



// #include <cstdio>
// #include <iostream>

// using namespace std;
// int n;
// int num[11], op[4];
// int mx = -1e9, mn = 1e9;

// void solve(int count, int ans, int add, int sub, int mul, int div) {
//     cout << add << "  " << sub << "  " << mul << "  " << div << "\n";
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