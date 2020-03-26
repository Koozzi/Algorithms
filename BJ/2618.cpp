#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

int M, N, a, b, sum = 0;
int map[1001][1001];

vector<int> ans;

int main(){
    cin >> M >> N;
    int oneI = 1;
    int oneJ = 1;
    int twoI = M;
    int twoJ = M;
    for(int i = 0 ; i < N ; i++){
        cin >> a >> b;
        if(abs(a - oneI) + abs(b - oneJ) > abs(a - twoI) + abs(b - twoJ)){
            sum += abs(a - twoI) + abs(b - twoJ);
            twoI = a;
            twoJ = b;
            ans.push_back(2);
        }
        else{
            sum += abs(a - oneI) + abs(b - oneJ);
            oneI = a;
            oneJ = b;
            ans.push_back(1);
        }
    }
    cout << sum << endl;
    for(int i = 0 ; i < ans.size() ; i++){
        cout << ans[i] << endl;
    }
    return 0;
}