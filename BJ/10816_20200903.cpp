#include <iostream>
#include <set>
#include <map>
using namespace std;

int N, M;
multiset<int> ms;
map<int, int> m;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> N;
    for(int i = 0 ; i < N ; i++){
        int a; cin >> a;
        int cnt = m.count(a);
        if(cnt == 0){
            m.insert({a, 1});
        }
        else{
            m.insert({a, cnt + 1});
        }
    }
    cin >> M;
    for(int i = 0 ; i < M ; i ++){
        int a; cin >> a;
        cout << m.count(a) << " ";
    }cout << "\n";
    return 0;
}