#include <iostream>
#include <vector>

using namespace std;

int N;

vector<int> lotto;
vector<int> selected;

void SELECT(int startIdx){
    if(selected.size() == 6){
        for(int i = 0 ; i < selected.size() ; i++){
            cout << selected[i] << " ";
        }
        cout << "\n";
    }
    for(int i = startIdx + 1 ; i < N ; i++){
        selected.push_back(lotto[i]);
        SELECT(i);
        selected.pop_back();
    }
}

int main(){
    while(1){
        cin >> N;
        if(N == 0){
            return 0;
        }
        for(int i = 0 ; i < N ; i++){
            int a;
            cin >> a;
            lotto.push_back(a);
        }
        for(int i = 0 ; i < N ; i++){
            selected.push_back(lotto[i]);
            SELECT(i);
            selected.pop_back();
        }
        cout << "\n";
        lotto.clear();
        selected.clear();
    }
}