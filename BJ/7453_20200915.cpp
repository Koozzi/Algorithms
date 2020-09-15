#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int N;
long long ans;
long long A[4000];
long long B[4000];
long long C[4000];
long long D[4000];

vector<long long> C_D;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    cin >> N;
    for(int i = 0 ; i < N ; i++){
        cin >> A[i] >> B[i] >> C[i] >> D[i];
    }

    for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < N ; j++){
            C_D.push_back(C[i] + D[j]);
        }
    } sort(C_D.begin(), C_D.end());

    for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < N ; j++){
            long long sum = -(A[i] + B[j]);
            auto low_iter = lower_bound(C_D.begin(), C_D.end(), sum);
            auto upp_iter = upper_bound(C_D.begin(), C_D.end(), sum);
            if(*low_iter == sum) ans += (upp_iter-low_iter);
        }
    }
    cout << ans << "\n";
    return 0;
}