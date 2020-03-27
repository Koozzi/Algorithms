#include <iostream>
#include <cmath>

using namespace std;

long long int M, I, J, ans = 0;

typedef struct{
    long long int moveI, moveJ;
}Dir;
Dir moveDir[3] = {{0,1}, {1,0}, {1,1}};

int main(){
    cin >> M >> I >> J;
    long long int i, j, A = pow(2, M);
    for(i = 0 ; i < A ; i += 2){
        for(j = 0 ; j < A ; j += 2){
            if(i != I || j != J){
                ans++;
            }
            else{
                cout << ans << "\n";
                return 0;
            }
            for(int k = 0 ; k < 3 ; k++){
                long long int nextI = i + moveDir[k].moveI;
                long long int nextJ = j + moveDir[k].moveJ;
                if(nextI != I || nextJ != J){
                    ans++;
                }
                else{
                    cout << ans << "\n";
                    return 0;
                }
            }
        }
    }
}