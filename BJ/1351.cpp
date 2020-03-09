#include <iostream>
#include <vector>

using namespace std;

long long int N, P, Q;
vector<long long int> ans;

int main(){
    cin >> N >> P >> Q;
    ans.push_back(1);
    ans.push_back(2);
    int idx = 2;
    while(idx <= N){
        idx++;
    }
    for(int i = 0 ; i < ans.size() ; i++){
        printf("%d : %lld\n", i, ans[i]);
    }
    return 0;
}