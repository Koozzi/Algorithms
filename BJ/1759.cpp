#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int M, N;
int cnt1 = 0, cnt2 = 0;

vector<int> v;
vector<int> newV;

void solve(int start){
    if(newV.size() == M){
        if(cnt1 >= 1 && cnt2 >= 2){
            for(int i = 0 ; i < newV.size() ; i++){
                cout << char(newV[i] + 97);
            }cout << endl;
        }
    }
    else{
        for(int i = start + 1 ; i < N ; i++){
            if(v[i] == 0 || v[i] == 4 || v[i] == 8 || v[i] == 14 || v[i] == 20){
                cnt1++;
                newV.push_back(v[i]);
                solve(i);
                newV.pop_back();
                cnt1--;
            }
            else{
                cnt2++;
                newV.push_back(v[i]);
                solve(i);
                newV.pop_back();  
                cnt2--;          
            }
        }
    }
}

int main(){
    cin >> M >> N;
    for(int i = 0 ; i < N ; i++){
        char a;
        cin >> a;
        v.push_back(a - 97);
    }
    sort(v.begin(), v.end());
    for(int i = 0 ; i < v.size() ; i++){
        if(v[i] == 0 || v[i] == 4 || v[i] == 8 || v[i] == 14 || v[i] == 20){
            cnt1++;
            newV.push_back(v[i]);
            solve(i);
            newV.pop_back();
            cnt1--;
        }
        else{
            cnt2++;
            newV.push_back(v[i]);
            solve(i);
            newV.pop_back();  
            cnt2--;          
        }
    }
    return 0;
}