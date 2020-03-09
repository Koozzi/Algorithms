#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int M;

vector<int> v;
vector<int> ans;

int main(){
    cin >> M;
    for(int i = 0 ; i < M ; i++){
        int a;
        cin >> a;
        v.push_back(a);
    }
    sort(v.begin(), v.end());
    
    if(v[0] != 1){
        cout << 1 << endl;
        return 0;
    }
    else{
        ans.push_back(v[0]);
    }

    for(int i = 1 ; i < v.size() ; i++){
        if(ans.back() + 1 == v[i]){
            ans.push_back(v[i]);
            int ansSize = ans.size();
            for(int j = 0 ; j < ansSize - 1 ; j++){
                if(ans[j] + v[i] > ans.back()){
                    ans.push_back(ans[j] + v[i]);
                }
            }
        }
        else{
            if(ans[0] + v[i] > ans.back() + 1){
                cout << ans.back() + 1 << endl;
                return 0;
            }
            else{
                int ansSize = ans.size();
                for(int j = 0 ; j < ansSize ; j++){
                    if(ans[j] + v[i] > ans.back()){
                        ans.push_back(ans[j] + v[i]);
                    }
                }
            }
        }
    }
    cout << ans.back() + 1 << endl;
    return 0;
}