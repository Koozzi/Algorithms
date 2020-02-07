#include <iostream>

using namespace std;

int main(){
    int T;
    cin >> T;
    for(int t = 1 ; t <= T ; t++){
        long long int N;
        cin >> N;
        if(N % 2 == 1){
            cout << "#" << t << " " << "NO" << "\n";
        }
        else{
            while(N > 1){
                N = N / 2;
                if(N % 2 == 1){
                    break;
                }
            }
            if(N == 1){
                cout << "#" << t << " " << "YES" << "\n";
            }
            else{
                cout << "#" << t << " " << "NO" << "\n";
            }
        }
    }
    return 0;
}